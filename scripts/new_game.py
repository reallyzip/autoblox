#!/usr/bin/env python3
"""Create a fresh Roblox Studio Architect project; no installs or remote actions."""
from __future__ import annotations
import argparse
import re
import shutil
import subprocess
from pathlib import Path

BUNDLE = Path(__file__).resolve().parents[1]
TEMPLATE = BUNDLE / "templates" / "roblox-game"
SKILL = BUNDLE / ".agents" / "skills" / "roblox-studio-architect"
TEXT_SUFFIXES = {".md", ".json", ".toml", ".luau", ".yml", ".yaml", ".txt", ".sh", ".py"}


def make_game(name: str, dest: Path, genre: str = "Not decided", git_init: bool = False) -> Path:
    name = name.strip()
    if not name or len(name) > 80 or any(ch in name for ch in "\r\n\x00{}"):
        raise ValueError("Game name must be one non-empty line, at most 80 characters, without braces")
    if not genre.strip() or len(genre) > 160:
        raise ValueError("Genre description must be 1–160 characters")
    dest = dest.expanduser().resolve()
    if dest.exists():
        raise FileExistsError(f"Destination already exists; refusing to overwrite: {dest}")
    if not TEMPLATE.is_dir() or not SKILL.is_dir():
        raise FileNotFoundError("The template or master skill was not found in this package")
    try:
        shutil.copytree(TEMPLATE, dest)
        dst_skill = dest / ".agents" / "skills" / "roblox-studio-architect"
        dst_skill.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(SKILL, dst_skill)
        for path in dest.rglob("*"):
            if path.is_file() and path.suffix.lower() in TEXT_SUFFIXES:
                try:
                    s = path.read_text(encoding="utf-8")
                except UnicodeDecodeError:
                    continue
                s = s.replace("{{GAME_NAME}}", name).replace("{{GENRE}}", genre.strip())
                path.write_text(s, encoding="utf-8")
        if git_init:
            subprocess.run(["git", "init", "-q", str(dest)], check=True)
    except Exception:
        if dest.exists():
            shutil.rmtree(dest)
        raise
    return dest


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--name", required=True, help="Name of the new original Roblox game")
    p.add_argument("--dest", required=True, type=Path, help="New, nonexisting destination directory")
    p.add_argument("--genre", default="Not decided", help="Initial genre; finalized in design meeting")
    p.add_argument("--git-init", action="store_true", help="Initialize local Git; never configures a remote or pushes")
    args = p.parse_args()
    try:
        created = make_game(args.name, args.dest, args.genre, args.git_init)
    except (ValueError, FileExistsError, FileNotFoundError, subprocess.CalledProcessError) as e:
        p.error(str(e))
    print(f"Scaffold created: {created}")
    print("Status: PREPRODUCTION. No gameplay, services, hooks or public place installed.")
    print("Next: open directory in Codex and invoke $roblox-studio-architect for design meeting.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
