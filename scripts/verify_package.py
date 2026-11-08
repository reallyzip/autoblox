#!/usr/bin/env python3
"""Validate package structure and a fresh generated game, without installing anything."""
from __future__ import annotations
import importlib.util
import json
from pathlib import Path
import tempfile

BASE = Path(__file__).resolve().parents[1]

def run() -> int:
    spec = importlib.util.spec_from_file_location("new_game", BASE / "scripts/new_game.py")
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    with tempfile.TemporaryDirectory() as temp:
        target = Path(temp)/"Demo"
        mod.make_game("Demo Game", target, "Co-op survival")
        check_path = target / "scripts/verify_game.py"
        v_spec = importlib.util.spec_from_file_location("verify_game", check_path)
        checker = importlib.util.module_from_spec(v_spec)
        assert v_spec.loader is not None
        v_spec.loader.exec_module(checker)
        assert not checker.inspect(target), "New game did not pass structural checks"
        errors = checker.inspect(target, release_candidate=True)
        assert errors, "Fresh untested game incorrectly passed release gate"
        assert (target / ".agents/skills/roblox-studio-architect/SKILL.md").is_file()
        assert (target / ".agents/skills/roblox-studio-architect/scripts/environment_setup.py").is_file()
        for rel in ("CLAUDE.md", "GEMINI.md", ".claude/skills/roblox-studio-architect/SKILL.md", ".cursor/rules/roblox-architect.mdc", ".github/copilot-instructions.md", "docs/MCP_SETUP.md", "docs/TOOL_CONNECTION_EVIDENCE.md", "scripts/setup_environment.py"):
            assert (target / rel).is_file(), rel
        assert (target / "docs/DESIGN_DECISIONS.md").read_text().count("NOT APPROVED")
        assert "Demo Game" in (target / "default.project.json").read_text()
        print(f"PASS: {len(list(target.rglob('*')))} scaffold entries; 41 practice modules; untested release blocked")
    return 0

if __name__ == '__main__':
    raise SystemExit(run())
