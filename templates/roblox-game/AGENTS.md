# {{GAME_NAME}} — Codex/agent authority

Use the local `.agents/skills/roblox-studio-architect/SKILL.md` when developing or auditing this Roblox game. Read only relevant references and the project decisions. The design meeting and final directive require explicit owner approval before executing major development.

## Source of truth
- `docs/DESIGN_DECISIONS.md` — concept and scope, status before implementation.
- `docs/FINAL_DIRECTIVE.md` — approved task authority.
- `docs/PROGRESS.md` — task ledger and checkpoint identities.
- `docs/VERIFICATION.json` — evidence-based release gates.
- `docs/CAPABILITY_REGISTRY.md` — tool/connectors and actual availability.
- `docs/ASSET_MANIFEST.json` — source ownership and licensing.
- `default.project.json` — Rojo mapping; Studio objects not synced here may be transient.

## Boundaries
This is a new original Roblox game, not a fork of Upkeep or another gameplay product. Never copy proprietary assets, game scripts, characters, names or maps from an unrelated project. Keep the Roblox experience PRIVATE by default. Do not spend, change account permissions, activate paid products, publish publicly, force push or delete unrelated work without explicit approval. Git pushes are separate from Roblox publication.

## Working agreements
First complete and verify a polished vertical slice. Maintain server authority over consequential gameplay and player data; clients request intent and render presentation. Favor built-in Roblox APIs, existing code, and source-owned Blender assets where useful. No automatic hooks or tool installation. Use one editor per file and one Studio operator. At task finish record code changes, tests, limitations, Git SHA and precise resume point. Do not assert runtime validation from static tests.

## Universal agent first-run setup
This workspace supports Codex, Claude Code, Cursor, Gemini CLI, GitHub Copilot/VS Code, and generic stdio-MCP-capable agents. Their instruction files are adapters; the single canonical workflow is `.agents/skills/roblox-studio-architect/SKILL.md`.

At the first new-project session, **before the design meeting**, inspect the environment with `python3 scripts/setup_environment.py --project . --agent auto`. If Studio or Blender are missing, offer the official downloads and assistance to install them. Ask permission before running `--interactive` configuration, installing community Blender MCP or changing any agent settings. Prefer Roblox Studio's built-in MCP and optional reviewed Blender MCP. Within the chosen agent perform actual read-only tool calls against Studio and Blender, and record evidence in `docs/TOOL_CONNECTION_EVIDENCE.md`. A config/registration check alone is NOT a connected MCP verification. If tools cannot connect, explain the blocker and continue with offline design/source work only. See `docs/MCP_SETUP.md`.
