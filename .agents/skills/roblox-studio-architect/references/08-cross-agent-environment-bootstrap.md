# Cross-agent bootstrap: environment, MCP and live verification

**Trigger:** On first activation in each new project, before any significant build action; recheck when the active coding agent or computer changes. This is an interactive offer, not unattended installation.

## First-run order (Codex, Claude Code, Cursor, Gemini CLI, Copilot/VS Code, other agents)

1. **Identify agent/OS/project.** Read `AGENTS.md`, the agent's native instructions (`CLAUDE.md`, `GEMINI.md`, etc.) and current source state. Locate this skill directory. Inspect the existing setup once rather than reinstalling.
2. **Run read-only diagnostics:** `python3 .agents/skills/roblox-studio-architect/scripts/environment_setup.py --project . --agent <selected-agent>` (on Windows use `py`). Detect Roblox Studio's bundled MCP launcher, Blender executable, `uvx`, and agent CLI if present. Absence of a launcher in the expected location is **unknown/missing**, not proof that the app is uninstalled.
3. **Offer installation when needed.** If Studio missing, offer to open its **official** Windows/macOS download from `https://create.roblox.com/docs/studio/setup`; if Blender missing, offer `https://www.blender.org/download/`. Do not silently download binaries, run `curl|sh`, require passwords, or change account settings. Assist through official installer/login, then re-run diagnostics. Roblox Studio is not officially available for Linux.
4. **Offer MCP connectivity.** Roblox Studio's MCP server ships with Studio, so **do not install a third-party Studio MCP**. Open Studio > Assistant > `...` > Manage MCP Servers > `Enable Studio as MCP server`; prefer **Quick connect** for a supported installed client. If Quick connect unavailable, show the documented stdio command/path for that OS and the agent's supported setup. The user must approve each MCP configuration change.
5. **Blender bridge is OPTIONAL and third-party.** Explain that `ahujasid/mcp-for-blender` can execute Python inside Blender. Ask permission to install its addon and register its stdio MCP server. Check for `uvx` (official installer if absent). Use reviewed upstream docs and pin a tested release when preparing a public distribution; set `BLENDER_MCP_SAFE_MODE=1` as an additional precaution, not a sandbox. In Blender enable the addon and start its local server. Do not silently install/upload AI art services, marketplace assets, or keys.
6. **Agent adapters.** Codex has its own `codex mcp add` workflow, Claude Code can read project `.mcp.json`, Cursor reads `.cursor/mcp.json`, Gemini CLI reads `.gemini/settings.json`, Copilot portable config is project `.mcp.json`, VS Code Local harness uses `.vscode/mcp.json`. They have different schemas; never blindly paste one into another. For unsupported agents generate the stdio specification and ask the user to choose its documented MCP settings.
7. **Live smoke from inside the *chosen* agent (mandatory):** Confirm Roblox Studio's **green connected-client indicator**, call the real read-only `list_roblox_studios` tool or current equivalent, and retrieve harmless info from the correct open test place. In Blender, call a read-only scene-inspection MCP tool and receive genuine scene data. Check the response against the active Studio instance and Blender scene. If tools unavailable, restart client/Studio, inspect PATH/config and troubleshoot; never claim connected based on config presence, successful CLI registration or a plausible AI explanation alone.
8. **Write exact evidence:** In project `docs/TOOL_CONNECTION_EVIDENCE.md` record date/time, OS, agent, actual MCP tool names, result/Studio instance ID or Blender scene name, scopes, remaining blockers. No credentials or private tokens. Classify each component `NOT_INSTALLED`, `PRESENT`, `REGISTERED`, `CONNECTED_VERIFIED`, `UNAVAILABLE`, or `NOT_TESTED`. `CONNECTED_VERIFIED` requires actual tool-call evidence; the bootstrap script cannot grant it by itself.
9. **Choose fallback honestly:** Without Studio/Blender MCP, game-design meetings and source-only preparation can continue, but the system must not claim full environment readiness or completed in-game verification. Never bypass publisher authentication or agent tool authorization.

Run the opt-in assistant with:

```shell
python3 .agents/skills/roblox-studio-architect/scripts/environment_setup.py --project . --agent claude --interactive
```

Replace `claude` with `codex`, `cursor`, `gemini`, `vscode`, `copilot`, or `other`. The interactive mode offers installation pages, reviewed Blender-addon setup, and configuration with confirmation. It does not guarantee that an agent can call a tool; **the agent must do the live smoke test**.

Useful official sources:
- Roblox Studio install: https://create.roblox.com/docs/studio/setup
- Roblox Studio built-in MCP: https://create.roblox.com/docs/studio/mcp
- Blender download: https://www.blender.org/download/
- Community Blender bridge (not Blender Foundation): https://github.com/ahujasid/mcp-for-blender
- VS Code MCP config: https://code.visualstudio.com/docs/agents/reference/mcp-configuration
- Gemini CLI skills/MCP: https://geminicli.com/docs/cli/skills/ and https://geminicli.com/docs/tools/mcp-server/
