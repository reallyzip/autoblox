#!/usr/bin/env python3
"""Convenient wrapper around the canonical, local-first Agent Skill setup wizard."""
from pathlib import Path
import runpy
import sys

TARGET = Path(__file__).resolve().parents[1] / '.agents/skills/roblox-studio-architect/scripts/environment_setup.py'
if not TARGET.is_file():
    sys.exit('Missing canonical environment setup wizard: ' + str(TARGET))
runpy.run_path(str(TARGET), run_name='__main__')
