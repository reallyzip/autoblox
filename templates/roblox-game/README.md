# {{GAME_NAME}}

A new local-first Roblox project initialized using the Roblox Studio Architect starter kit.

**Genre:** {{GENRE}}

Status: PREPRODUCTION — no game design approved, no gameplay implemented, and no Roblox place published.

Open this folder in Codex and invoke `$roblox-studio-architect` to conduct the concept meeting. Codex should write `docs/DESIGN_DECISIONS.md` for approval, then `docs/FINAL_DIRECTIVE.md` and a milestone plan. Only after approval should implementation begin.

Source layout: `src/server` (authoritative game), `src/client` (input and presentation), `src/shared` (shared constants/types). `assets/blender` holds editable source, `assets/exports` portable formats, `assets/roblox` serialized templates. Use `default.project.json` for Rojo mapping.

`python3 scripts/verify_game.py` checks project structure; `python3 scripts/verify_game.py --release-candidate` checks whether evidence records claim all gates have passed with local evidence paths (a structural check, **not** runtime verification). Build/test within a real Roblox Studio session before any release claim.

No hooks, connectors, marketplaces or remote Git destination are installed by this template. Use `git init` if desired, then configure and review an explicit remote before push. The example `.githooks/pre-commit` is opt-in only.

## Cross-agent first-run setup

Works with Codex, Claude Code, Cursor, Gemini CLI, Copilot/VS Code and other agents that can read the skill and use stdio MCP. Run `python3 scripts/setup_environment.py --project . --agent auto` to inspect, or add `--interactive` to get opt-in offers for Roblox Studio, Blender and agent-specific MCP setup. The user must install/sign into Studio and enable its **built-in** MCP; third-party Blender MCP requires informed opt-in. Actual agent-side read-only tool calls are required before any connection is marked verified. Read `docs/MCP_SETUP.md` and `docs/TOOL_CONNECTION_EVIDENCE.md`.
