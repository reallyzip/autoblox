# Local capability registry — {{GAME_NAME}}

Review once per session or when capabilities change, not on every task. An installed or exposed tool is not evidence of authentication or operational availability.

| Capability | Installed | Authenticated | Verified with this project | Purpose and conflicts |
| --- | --- | --- | --- | --- |
| Roblox Studio | UNKNOWN | UNKNOWN | NO | Authoritative runtime/visual checks; private place identity required |
| Git | UNKNOWN | N/A | NO | Source history and recovery |
| Rojo / Rokit | UNKNOWN | N/A | NO | Source-owned Studio sync |
| StyLua / Selene / Luau LSP | UNKNOWN | N/A | NO | Local code quality |
| Blender | UNKNOWN | N/A | NO | Editable original 3D assets |
| GitHub remote or connector | UNKNOWN | UNKNOWN | NO | Explicit repo access and authorized push |
| Roblox Studio built-in MCP | UNKNOWN | UNKNOWN | NO | Official bundled server; require a live read-only tool call from the selected agent |
| Blender community MCP (optional) | UNKNOWN | UNKNOWN | NO | Third-party, code-executing addon; opt-in, safe-mode and live scene-inspection verification |
| Codex / Claude / other agent MCP config | UNKNOWN | UNKNOWN | NO | Registry only; never equate a config entry with actual connection |
| Docs/research connector | UNKNOWN | UNKNOWN | NO | Current official API references, cited research |

Hooks: OFF by default. Dependencies: install only with explicit permission and verified source.
