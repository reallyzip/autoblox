# Roblox Studio & Blender MCP setup

This guide is for **consent-based local setup**. Registering a tool in an MCP config is **not** evidence that the actual agent can reach the app.

## 1. Roblox Studio (official built-in MCP)

- Install Roblox Studio from [Roblox's official setup guide](https://create.roblox.com/docs/studio/setup) if missing; launch Studio and sign in.
- Open a **disposable test place** (not a public live game).
- Open Studio **Assistant → … → Manage MCP Servers**; enable **Studio as MCP server**.
- Use the Studio **Quick connect** instructions for supported coding agents; the wizard can also inspect the local launcher and suggest client-specific registration.
- Restart/reload your AI client if required. Confirm Studio's connected indicator.
- Ask the active agent to call a harmless **read-only tool** (for example list Studio instances and read a property in the open test place). Record tool, result and timestamp.

Official guide: https://create.roblox.com/docs/studio/mcp

Never install an unofficial Roblox Studio MCP server just because the official one was not detected. Diagnose the app version and built-in server first.

## 2. Blender (optional community MCP)

- Install Blender from https://www.blender.org/download/ if missing.
- Confirm Blender opens and can load a disposable scene.
- If you want MCP instead of using Blender via CLI scripts, review https://github.com/ahujasid/mcp-for-blender, its current release and dependencies.
- Installing the bridge/addon may allow an AI agent to execute Python **inside Blender**, including operations on the local file system. Approve this explicitly. Do not treat a safe-mode environment variable as an isolation boundary.
- Use its up-to-date official installation commands, rather than copying stale examples from a template. Its README currently describes `uvx mcp-for-blender install-addon` and a `uvx mcp-for-blender` MCP server.
- Start the addon/local bridge as required, restart the AI client, and ask for a harmless scene inspection from the agent. Record tool, scene summary and timestamp.

## 3. Run the environment wizard

From the newly generated Roblox game project:

```bash
python3 scripts/setup_environment.py --project . --agent auto
python3 scripts/setup_environment.py --project . --agent codex --interactive
# or select claude, cursor, gemini, vscode, copilot, other
```

The read-only doctor checks common executable paths. The optional interactive mode proposes changes, backs up supported existing MCP configuration files, and refuses conflicting entries. It cannot reliably auto-install Roblox Studio or Blender on every operating system, and it does not perform the final agent-side tool calls for you.

## 4. Verify the two independent connections

Record in `docs/TOOL_CONNECTION_EVIDENCE.md` in your generated game:

| Tool | Requirement | Evidence to record |
| --- | --- | --- |
| Roblox Studio MCP | Actual read-only agent call against the right open test place | Agent, tool, project identity, returned result, timestamp |
| Blender MCP | Actual read-only agent scene call | Agent, tool, scene identity, returned result, timestamp |
| Studio game QA | Separate Studio solo and multiplayer tests | Exact tests, results, script/Git identity |

**MCP CONNECTED** should be set only after actual calls. If a tool is unavailable, continue concept planning or offline Luau/Blender CLI work, but don't claim connected Studio integration or release-grade QA.

## Troubleshooting

- App detected, MCP launcher not found: verify the app version and official installation path.
- CLI configured, zero tools: restart the client, check its MCP permissions, inspect stdout/stderr logs; verify the launcher actually runs.
- Wrong Roblox place: open the intended disposable place and reconnect; never assume the editor target.
- Blender bridge disconnected: confirm addon installed/enabled and local server started. Do not open an untrusted .blend file or run downloaded scripts without review.
- Unsupported OS: Blender and offline work are possible on Linux, but Roblox Studio needs supported Windows/macOS access.
