# First-run tool setup — {{GAME_NAME}}

1. Choose the coding assistant: Codex, Claude Code, Cursor, Gemini CLI, GitHub Copilot/VS Code, or a generic stdio-MCP-capable agent.
2. In this project run: `python3 .agents/skills/roblox-studio-architect/scripts/environment_setup.py --project . --agent auto --interactive` (`py` on Windows).
3. The wizard detects **Roblox Studio**, **Blender**, **uvx**, and agent CLI tools. It offers official installation pages if Studio or Blender is not found. It will ask permission before changing MCP config or installing the community Blender addon.
4. Open Roblox Studio, sign in and open a *disposable test place*. Assistant > ... > Manage MCP Servers > Enable Studio as MCP server. Prefer Roblox's built-in **Quick connect** for the selected agent; otherwise use the wizard's documented MCP launcher and config.
5. Blender: the **optional third-party** `mcp-for-blender` addon must be enabled inside Blender. Review https://github.com/ahujasid/mcp-for-blender and its security implications; it can run Python. Use the addon UI to start the server. Safe-mode env checks help but do not provide secure sandboxing.
6. Restart agent as required; **within the AI agent**, call `list_roblox_studios` (or current equivalent) then a harmless read-only Studio operation. Call the Blender read-only scene-info tool. Only a successful tool call and actual reply count as connected.
7. Record evidence in `docs/TOOL_CONNECTION_EVIDENCE.md`. If either isn't verified, classify SETUP_INCOMPLETE and continue with offline planning only until the blocker is resolved. Never invent results.

No credentials are included. Project-scope configuration is preferred. Avoid duplicate MCP registrations or overwriting existing user configuration.

## Cross-agent setup notes

- **Codex:** shared `~/.codex/config.toml`, CLI `codex mcp add` and `codex mcp list`. Changes can affect all Codex projects; obtain permission.
- **Claude Code:** `.mcp.json` at workspace root and `claude mcp list` or `/mcp` in the session. The local skill bridge is in `.claude/skills/roblox-studio-architect/`.
- **Cursor:** project `.cursor/mcp.json`, and Cursor Agent MCP settings/tool list.
- **Gemini CLI:** project `.gemini/settings.json`, `gemini mcp list`, `.agents/skills` discovery alias.
- **GitHub Copilot:** workspace-root portable `.mcp.json` (`mcpServers`); if using VS Code Local harness, `.vscode/mcp.json` uses `servers`, not `mcpServers`.
- **Other assistants:** use the MCP stdio command and agent's verified vendor documentation; `SKILL.md` is Agent Skills compatible but not all vendors implement discovery.

Official docs: https://create.roblox.com/docs/studio/mcp ; https://create.roblox.com/docs/studio/setup ; https://www.blender.org/download/
