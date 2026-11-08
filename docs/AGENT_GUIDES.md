# Copy-paste setup for AI coding platforms

**First create a game project** using [INSTALL.md](INSTALL.md). All prompts below assume your AI coding tool has the **generated game project folder open**. A pasted prompt cannot install software, add MCP permissions, or grant unavailable actions on its own.

## Codex

Recommended: canonical `.agents/skills/roblox-studio-architect/SKILL.md`, root `AGENTS.md`, and optional Codex-native skill discovery. Open the game folder in Codex, then paste:

```text
Use $roblox-studio-architect. Inspect this game's source and read AGENTS.md.
Check whether Roblox Studio and Blender are installed and connected through MCP.
Offer setup for missing tools with my consent, and verify both through real
read-only agent-side calls. Lead an end-to-end Roblox game design meeting with
me. Challenge scope and originality, prepare a complete final directive, and
wait for my approval. After approval build one polished playable vertical slice,
then complete the game using delegated domain work, verified milestones, real
Studio multiplayer testing, source-controlled Blender assets, and a PRIVATE
release-candidate handoff. Do not publish publicly or spend money without asking.
```

Use `python3 scripts/setup_environment.py --project . --agent codex --interactive` if needed. Codex CLI MCP configuration differs from generic JSON; follow the wizard output and official Codex documentation.

## Claude Code

Use the generated `CLAUDE.md` and `.claude/skills/roblox-studio-architect/SKILL.md` bridge. In the project directory:

```text
Read CLAUDE.md and the canonical .agents/skills/roblox-studio-architect/SKILL.md.
Apply AutoBlox. Check existing Roblox Studio and Blender installs and MCP
connections before proposing any install. Ask my permission before changes and
verify both tool connections from this Claude session. Then run a professional
design meeting, produce one final game directive, and request my approval. Once
approved, build in recoverable milestones, review implementation with actual
tests and peer agents where possible, and deliver an independently checked
PRIVATE Roblox release candidate.
```

Run `python3 scripts/setup_environment.py --project . --agent claude --interactive` after reviewing the first-run checklist.

## Cursor

Use `.cursor/rules/roblox-architect.mdc`, `AGENTS.md`, and the canonical skill:

```text
Read .cursor/rules/roblox-architect.mdc, AGENTS.md and
.agents/skills/roblox-studio-architect/SKILL.md. Use AutoBlox to inspect the
project, offer Roblox Studio and Blender MCP setup safely, and test the real
connections. Conduct the game design council; get my approval of the final
specification; then implement only the approved game with Studio and multiplayer
verification before reporting completion.
```

Run the wizard using `--agent cursor` when ready; check the actual Cursor MCP UI after a restart.

## Gemini CLI

Use `GEMINI.md`, `AGENTS.md`, and the canonical skill:

```text
Read GEMINI.md, AGENTS.md, and .agents/skills/roblox-studio-architect/SKILL.md.
Follow AutoBlox: check local tools, offer opt-in MCP setup, verify agent-to-Studio
and agent-to-Blender calls, conduct a Roblox concept meeting, and write an
approved final directive. Develop the approved game through tested milestones
and deliver an honest private release-candidate report.
```

Run the wizard with `--agent gemini`, then verify the Gemini CLI MCP configuration in the actual client.

## GitHub Copilot and VS Code

Use `.github/copilot-instructions.md`, `AGENTS.md`, and the canonical skill. Agents may differ in their ability to read `SKILL.md` and run tools:

```text
Read .github/copilot-instructions.md, AGENTS.md and
.agents/skills/roblox-studio-architect/SKILL.md. Apply AutoBlox, starting with a
read-only Studio/Blender environment check and opt-in MCP onboarding. Verify
real tool calls before relying on them. Run a complete game design meeting,
obtain final approval, then implement and test the specified game. Maintain
Git, assets, multiplayer verification, and a private-by-default release gate.
```

For MCP, choose `--agent vscode` for VS Code's `.vscode/mcp.json` style or `--agent copilot` for a project `.mcp.json` path where supported. Review your installed extension's current MCP documentation; not every Copilot mode provides equivalent tool access.

## Other AI coding agents

If your agent supports no skill directory convention, ask it to read the canonical skill explicitly:

```text
Use the AutoBlox project instructions in AGENTS.md and
.agents/skills/roblox-studio-architect/SKILL.md. Follow its references only as
needed. First inspect installed tools and permissions, offer safe MCP onboarding,
run a complete Roblox game concept meeting, and create an owner-approved design.
After approval, implement the smallest enjoyable complete game first and grow
only approved features. Validate with actual Roblox Studio runtime evidence;
keep publication and money decisions under my control.
```

**Capability differences matter.** A CLI agent without filesystem access cannot install the skill. A coding agent without Roblox Studio MCP cannot claim real Studio testing. A background agent cannot legitimately publish or run indefinitely unless its host allows it.
