#!/usr/bin/env python3
"""Structural-only project validation, with optional evidence-record release gate.

This does NOT run Roblox Studio and does not prove that recorded evidence is truthful.
"""
from __future__ import annotations
import argparse
import json
import re
from pathlib import Path

REQUIRED = [
    "AGENTS.md", "CLAUDE.md", "GEMINI.md", "default.project.json", "rokit.toml", "README.md",
    "docs/DESIGN_DECISIONS.md", "docs/FINAL_DIRECTIVE.md",
    "docs/PROGRESS.md", "docs/VERIFICATION.json", "docs/CAPABILITY_REGISTRY.md",
    "docs/MCP_SETUP.md", "docs/TOOL_CONNECTION_EVIDENCE.md", "scripts/setup_environment.py",
    "docs/ASSET_MANIFEST.json", ".agents/skills/roblox-studio-architect/SKILL.md",
    ".agents/skills/roblox-studio-architect/references/coverage.json",
    ".agents/skills/roblox-studio-architect/scripts/environment_setup.py",
    ".claude/skills/roblox-studio-architect/SKILL.md",
]
RELEASE_GATES = [
    "source_build", "complete_solo_loop", "multiplayer_or_na", "security",
    "persistence_or_na", "asset_integrity", "ui_controls", "device_performance",
    "private_build_parity",
]


def inspect(root: Path, release_candidate: bool = False) -> list[str]:
    errors: list[str] = []
    root = root.resolve()
    for f in REQUIRED:
        if not (root / f).is_file():
            errors.append("Missing " + f)
    for folder in ("src/server", "src/client", "src/shared"):
        directory = root / folder
        if not directory.is_dir() or not any(directory.rglob("*.luau")):
            errors.append(f"Missing Luau source in {folder}")
    if errors:
        return errors
    try:
        project = json.loads((root / "default.project.json").read_text(encoding="utf-8"))
        assert project["tree"]["$className"] == "DataModel"
        assert project["name"]
    except (ValueError, KeyError, AssertionError) as exc:
        errors.append(f"Invalid Rojo project mapping: {exc}")
    try:
        coverage = json.loads((root / ".agents/skills/roblox-studio-architect/references/coverage.json").read_text())
        if len(coverage) != 41 or len({x.get("slug") for x in coverage}) != 41:
            errors.append("Expected 41 uniquely mapped original practice modules")
        for entry in coverage:
            path = root / ".agents/skills/roblox-studio-architect/references/practices" / (entry["slug"] + ".md")
            if not path.is_file() or len(path.read_text(encoding="utf-8")) < 600:
                errors.append("Missing or incomplete practice: " + entry["slug"])
    except (ValueError, KeyError, TypeError) as exc:
        errors.append(f"Invalid playbook coverage: {exc}")
    skill = (root / ".agents/skills/roblox-studio-architect/SKILL.md").read_text(encoding="utf-8")
    if not skill.startswith("---\n") or "name: roblox-studio-architect" not in skill:
        errors.append("Master SKILL.md has invalid basic metadata")
    try:
        report = json.loads((root / "docs/VERIFICATION.json").read_text(encoding="utf-8"))
        if not isinstance(report.get("gates"), dict):
            raise TypeError("gates must be a dictionary")
    except (ValueError, TypeError) as exc:
        return errors + [f"Invalid verification record: {exc}"]
    if release_candidate:
        if report.get("status") != "READY_FOR_OWNER_PLAYTEST":
            errors.append("Release-candidate status must be READY_FOR_OWNER_PLAYTEST")
        if not report.get("source_commit") or not report.get("private_place_id") or not report.get("private_published_version"):
            errors.append("Release candidate needs Git SHA and verified private place/version identities")
        if report.get("public_release_authorized") is not False:
            errors.append("This release-candidate check must remain PRIVATE, not publicly authorized")
        if report.get("known_critical_issues") or report.get("known_high_issues"):
            errors.append("Known critical/high issues still open")
        for name in RELEASE_GATES:
            gate = report["gates"].get(name)
            if not isinstance(gate, dict):
                errors.append("Missing release gate " + name)
                continue
            status = gate.get("status")
            if status not in ("PASS", "NOT_APPLICABLE"):
                errors.append(f"Release gate {name}: {status or 'NO STATUS'}")
                continue
            if status == "NOT_APPLICABLE" and (name in ("source_build", "complete_solo_loop", "security", "asset_integrity", "ui_controls", "private_build_parity") or not gate.get("note", "").strip()):
                errors.append(f"Release gate {name}: N/A not permitted or lacks justification")
            evidence = gate.get("evidence", [])
            if status == "PASS" and (not isinstance(evidence, list) or not evidence):
                errors.append(f"Release gate {name} has no evidence links")
            if isinstance(evidence, list):
                for item in evidence:
                    if not isinstance(item, str):
                        errors.append(f"Invalid evidence path in {name}")
                    else:
                        path = (root / item).resolve()
                        if not path.is_relative_to(root) or not path.is_file():
                            errors.append(f"Evidence missing or outside project: {item}")
    return errors


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root", default=".", type=Path)
    p.add_argument("--release-candidate", action="store_true", help="Check presence of completed evidence records only")
    args = p.parse_args()
    failures = inspect(args.root, args.release_candidate)
    if failures:
        for f in failures:
            print("FAIL:", f)
        return 1
    print("PASS: structural checks" + (" and release-candidate evidence records" if args.release_candidate else ""))
    print("WARNING: No Studio runtime or authenticity checks performed by this Python script.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
