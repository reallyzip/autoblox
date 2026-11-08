#!/usr/bin/env python3
"""Build deterministic, inspectable AutoBlox release archives. No network access or Git writes."""
from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / ".agents" / "skills" / "roblox-studio-architect"
SKIP_DIRS = {".git", "__pycache__", ".pytest_cache", ".mypy_cache", ".venv", "venv", "dist", ".idea"}
SKIP_NAMES = {".DS_Store", ".env", ".env.local", ".env.production", ".mcp.json"}
SKIP_SUFFIXES = {".pyc", ".pyo", ".pem", ".key", ".p12"}
PRIVATE_CONFIGS = {".cursor/mcp.json", ".gemini/settings.json", ".vscode/mcp.json", ".codex/config.toml"}


def version_text() -> str:
    value = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    if not re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+(?:-[a-z0-9][a-z0-9.-]*)?", value):
        raise ValueError("Unsafe or malformed VERSION")
    return value


def safe_files(base: Path):
    for path in sorted(base.rglob("*")):
        if any(part in SKIP_DIRS for part in path.relative_to(base).parts):
            continue
        if path.is_symlink():
            raise ValueError("Refusing to package symbolic link: " + str(path))
        if not path.is_file() or path.name in SKIP_NAMES or path.suffix.lower() in SKIP_SUFFIXES:
            continue
        rel = path.relative_to(base)
        if rel.as_posix() in PRIVATE_CONFIGS or any(part.startswith(".env") for part in rel.parts):
            continue
        yield path


def zip_folder(source: Path, destination: Path, prefix: str) -> int:
    files = list(safe_files(source))
    if not files:
        raise ValueError("Package has no source files")
    with zipfile.ZipFile(destination, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for source_file in files:
            rel = source_file.relative_to(source).as_posix()
            info = zipfile.ZipInfo(prefix + "/" + rel, date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, source_file.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    with zipfile.ZipFile(destination) as archive:
        corrupt = archive.testzip()
        if corrupt:
            raise ValueError("Corrupt archive member: " + corrupt)
        if len(archive.namelist()) != len(files):
            raise ValueError("Unexpected archive size")
    return len(files)


def build_release(destination: Path) -> dict:
    destination = destination.resolve()
    destination.mkdir(parents=True, exist_ok=True)
    version = version_text()
    if not (SKILL / "SKILL.md").is_file():
        raise FileNotFoundError("Missing master SKILL.md")
    plans = [
        (ROOT, destination / ("autoblox-full-toolkit-v" + version + ".zip"), "autoblox"),
        (SKILL, destination / ("autoblox-master-skill-v" + version + ".zip"), "roblox-studio-architect"),
    ]
    output = {}
    checksum_lines = []
    for src, out, prefix in plans:
        count = zip_folder(src, out, prefix)
        sha = hashlib.sha256(out.read_bytes()).hexdigest()
        checksum_lines.append(sha + "  " + out.name)
        output[out.name] = {"sha256": sha, "files": count, "bytes": out.stat().st_size}
    (destination / "SHA256SUMS").write_text("\n".join(checksum_lines) + "\n", encoding="utf-8")
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "dist")
    args = parser.parse_args()
    try:
        info = build_release(args.output)
    except (OSError, ValueError) as exc:
        parser.error(str(exc))
    for name, item in info.items():
        print("PASS", name, item["files"], "files", item["bytes"], "bytes", item["sha256"])
    print("SHA256SUMS:", (args.output / "SHA256SUMS").resolve())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
