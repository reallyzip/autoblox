---
name: roblox-studio-architect
description: Use when conceiving, planning, creating, improving, debugging, testing or preparing to release a Roblox game with Codex, Claude Code, Cursor, Gemini CLI, Copilot/VS Code or other coding agents, Roblox Studio, Luau, Blender and Git. Runs a professional design meeting, turns decisions into an approved game directive, routes to original specialist playbooks, supervises implementation, and builds an evidence-gated private release candidate. Also use for reusable Roblox game templates, multi-agent development and full-game audits.
---

# Roblox Studio Architect — cross-agent, local-first production supervisor

This is a **single skill with lazy-loaded references**, not 41 competing skills or a claim that a prompt alone can finish any game. Operate as a professional game studio while preserving evidence, permissions, original art and recoverability. The creator's game specification and repository instructions outrank examples in the references.

## Invocation and modes

- **Meeting** (default for a new concept): inspect context, ask focused questions one at a time, show 2–3 credible design paths, challenge scope and originality, then obtain explicit approval of one consolidated creative brief.
- **Plan**: transform the approved brief into gameplay architecture, asset bible, vertical slice, production milestones, responsibilities, tests, budget and acceptance gates.
- **Build**: implement approved tasks autonomously in verifiable increments. Delegate independent domains if real subagent tools exist; if not, execute serially. No inventing agent activity.
- **Audit**: inspect current code/assets/data flows and the actual Studio game, rank bugs, security, usability, performance and production risks; separate evidence from opinions.
- **Release candidate**: fix blockers, test, reconcile Git and the saved PRIVATE place, deliver the full evidence package. Public launch and purchases always require separate owner authorization.
- **Resume**: read project decisions, task ledger, commits, test evidence, blockers and current source, then pick up the next uncompleted task. Never reconstruct state from memory alone.

On any mode, start from the current project HEAD and project-local `AGENTS.md`. If the user asks a narrow question, answer it instead of launching a full meeting. Never treat autonomy as permission to publish, spend, grant permissions, remove unrelated data or install hooks.

## Mandatory first-run setup (every agent)

At the start of a **new project or a new machine/AI agent**, run the **read-only** environment doctor before the design meeting and check Roblox Studio, Blender, `uvx`, and the chosen agent's MCP availability. Follow `references/08-cross-agent-environment-bootstrap.md` and, from a scaffold project, `docs/MCP_SETUP.md`. Offer to help install missing Roblox Studio and Blender from their official sources. **Ask for consent** before installing apps, enabling integrations, adding config, installing community Blender addon, starting servers or changing permissions. Roblox Studio includes its official MCP server; do not add a redundant unofficial server. Blender's MCP integration is third-party, optional and code-executing.

For supported clients, use the native adapter: `.agents/skills` for Codex/Gemini and compatible harnesses; Claude Code uses `.claude/skills/roblox-studio-architect/SKILL.md` bridge + `CLAUDE.md`; Cursor rules, Gemini `GEMINI.md`, GitHub Copilot rules and VS Code use the template's companion files. Unrecognized agents can read this `SKILL.md` directly and integrate via documented stdio MCP; avoid claims of universal automatic discovery.

From a project scaffold run `python3 scripts/setup_environment.py --project . --agent auto` (Windows: `py`), then use `--interactive` only with user permission. For a standalone skill invoke `python3 <skill-dir>/scripts/environment_setup.py --project <game-folder> --agent <selected-agent>`. **Do not call MCP READY based on CLI registration or config files.** Verify live tool calls from the active agent to an open Studio test place and Blender scene; record tool names/results in `docs/TOOL_CONNECTION_EVIDENCE.md`. Do not mark integration complete until verified. If tools unavailable, proceed with meeting/offline work but block in-Studio completion claims.

## Mandatory product-design lock

Before building an unapproved new game, apply `references/01-design-council.md`. Decide the audience, genre, social mode, core loop, hero mechanic, controls/platforms, art identity, pacing, progression/monetization posture, target devices, experience maturity, differentiators, production constraints, acceptance, and excluded features. Review Roblox policy and market facts when time-sensitive. Deliver a **Design Decision Record** and an owner-approved final directive. Do not begin major implementation before that gate.

## Source & execution discipline

1. Identify `git status`, remotes, branch, Studio place/universe (if connected), authoritative Rojo mapping, scripts/assets, current private published version and existing evidence. Preserve uncommitted work and revisions.
2. Check optional skill and tool availability **briefly once per session**; follow `references/02-capability-routing.md`. Use source-owned Luau, Git, Rojo/Rokit, Studio and Blender first; optional tools only when actually connected and authorized; a first-run environment check is mandatory.
3. Create or update a numbered work plan from `references/03-production-supervisor.md`. One owner per file, one Studio operator, isolated worktrees for conflicting independent edits, explicit interface contracts.
4. Build a small but polished end-to-end playable vertical slice first; then scale only approved mechanics and content. Adopt existing engine APIs and modules before introducing new abstractions.
5. For every task: test the precondition or bug, implement, verify static checks, run relevant Studio cases, inspect diff, record evidence and checkpoint. A completed render is not an imported/verified asset.
6. Use `references/04-quality-release-gates.md` before calling a game complete. Never equate waived tests, Git pushes, offline builds, private saves and public publication.
7. At a user-approved deadline, preserve a recoverable checkpoint, commit and push only with permission and a verified destination, report what remains, then stop and wait.

## Playbook routing

Load **one main practice and at most two domain supports** from `references/practices/`. Add evidence and security review on consequential code paths. The original project-targeted mapping is in `references/coverage.json` and `references/05-skill-coverage.md`. Do not load all playbooks into the model context by default.

- Design meeting/new direction: `concept-workshop` + `milestone-planning`
- New Luau gameplay: `roblox-luau` + `lean-implementation` + `test-first-changes`
- Remote/network/combat: `roblox-networking` + `root-cause-investigation` or `request-independent-review`
- Currency and persistence: `roblox-datastores` + `save-systems` + `evidence-gated-completion`
- Characters/animation: `roblox-characters` + `create-game-assets` + `camera-systems` when relevant
- Blender and world: `create-game-assets` + `level-design` + `visual-quality-gate`
- Controls and menus: `input-systems` + `roblox-ui` or `game-ui-ux`
- Performance: `performance-optimization` + relevant physics/audio/asset practice
- Subagents: `independent-agent-routing` + `subagent-task-loop`
- Bug: `root-cause-investigation` + domain practice + `test-first-changes`
- Final review/release: `whole-repo-audit` + `evidence-gated-completion` + `branch-closeout`

For genre-specific designs use `references/06-genre-blueprints.md` in addition to relevant domain practices. For authorized hooks and connector protocols read `references/07-tools-hooks-permissions.md`.

## Non-negotiable supervision and truthfulness

Server owns game results, player state, currency, entitlement decisions and consequential physics/combat. Clients request intent and render feedback. Test malformed, stale, spammed and cross-player requests. Preserve DataStore compatibility, original authorship and licensed asset provenance. Validate on Solo, Server & Clients, device emulators and real hardware when available. Identify what remains untested.

At final handoff provide: approved design ID; actual feature state; Git branch/commit/push; asset/Blender manifest; static and Studio test matrix; performance/security results; saved/private place identity if verified; unresolved blockers; commercial and public-release gates; next owner action. Distinguish `READY FOR OWNER PLAYTEST` from `APPROVED FOR PUBLIC LAUNCH`.

Do not automatically enable Git hooks, install connectors, write credentials, force-push, delete local files, or change Roblox audience/monetization. The system is deliberately local-first and PRIVATE by default.
