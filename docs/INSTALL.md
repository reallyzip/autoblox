# Install AutoBlox

AutoBlox is a local project template and AI-agent instruction set, not a binary Roblox editor or hosted service. Setup needs Python 3.9+, a terminal, and an AI coding tool capable of reading files. Git is recommended.

## Choose a package

- **Complete toolkit:** [AutoBlox full ZIP](https://github.com/reallyzip/autoblox/releases/download/v0.3.0-preview/autoblox-full-toolkit-v0.3.0-preview.zip) for starting fresh games.
- **Skill only:** [Master skill ZIP](https://github.com/reallyzip/autoblox/releases/download/v0.3.0-preview/autoblox-master-skill-v0.3.0-preview.zip) for an existing repo.
- **Git clone:** `git clone https://github.com/reallyzip/autoblox.git` then `cd autoblox`.

Both ZIP links are live in the published v0.3.0-preview release. GitHub's Code → Download ZIP is an alternative for browsing the repository source.

## macOS and Linux terminal (Python 3.9+)

```bash
git clone https://github.com/reallyzip/autoblox.git
cd autoblox
python3 -m unittest discover -s scripts/tests -v
python3 scripts/new_game.py --name "My Roblox Game" --genre "Adventure" --dest ../my-roblox-game --git-init
cd ../my-roblox-game
python3 scripts/setup_environment.py --project . --agent auto
```

**Linux note:** Roblox Studio is supported on Windows and macOS, not natively on Linux. You can use AutoBlox for design and offline source creation on Linux; final Studio integration needs a supported host.

## Windows PowerShell

```powershell
git clone https://github.com/reallyzip/autoblox.git
cd autoblox
py -m unittest discover -s scripts/tests -v
py scripts/new_game.py --name "My Roblox Game" --genre "Adventure" --dest ../my-roblox-game --git-init
cd ../my-roblox-game
py scripts/setup_environment.py --project . --agent auto
```

If `py` is unavailable, try `python`. If Git is unavailable, download/extract the ZIP, open the extracted folder, then follow steps beginning with the unit tests.

## First-run apps & MCP

Roblox Studio and Blender are **not bundled** and are never installed silently. The wizard detects common install locations and offers official downloads. Review the prompts and approve any installation, addon, CLI registration, or config change individually.

```bash
python3 scripts/setup_environment.py --project . --agent claude --interactive
```

Use `codex`, `cursor`, `gemini`, `vscode`, `copilot`, or `other` instead of `claude` to fit the active agent. Read [MCP setup](MCP_SETUP.md) before enabling the optional community Blender bridge. **Only an actual successful tool call in the chosen AI session counts as a verified MCP connection.**

## Starting a game-design meeting

Launch Codex, Claude Code or your chosen AI agent **with the generated game folder open**. Paste the corresponding prompt from [AGENT_GUIDES.md](AGENT_GUIDES.md). Before coding, the AI should lead a concept review, create a final directive, and get your approval. Avoid uploading private account data or unrelated game repositories into public repos.

## Installing the skill in an existing game

The master skill's canonical folder is `.agents/skills/roblox-studio-architect/`. Copy this folder into your existing repo, keeping the relative paths intact. Add appropriate instructions to `AGENTS.md`, `CLAUDE.md`, `GEMINI.md` or editor-specific rules so the agent reads the canonical skill. Do not overwrite existing instructions or tools.

A skill-only ZIP is suitable for extracting under `~/.agents/skills/` on a compatible agent. Claude can also load its skills through `.claude/skills/`; either point a bridge to the canonical skill or install an independently maintained copy. Skills may be discovered differently across vendors; explicitly direct the agent to the file when necessary.

## Verify and troubleshoot

```bash
python3 -m unittest discover -s scripts/tests -v
python3 scripts/verify_package.py
python3 scripts/build_release.py
```

These verify the toolkit files, not a Roblox game. For actual gameplay validation, use your game's `scripts/verify_game.py` and Studio Play/Server & Clients. Read [FAQ](FAQ.md) for connection, permission and availability issues.
