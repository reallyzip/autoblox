# Architecture and production contract

**Canonical skill:** `.agents/skills/roblox-studio-architect/SKILL.md`. **Source-of-truth per game:** generated `AGENTS.md`, final approved directive, Git branch, Roblox Studio evidence and source-controlled Blender/Roblox assets.

AutoBlox is not a resident background service. It is an on-demand *playbook and project scaffolding system*. The coding agent chooses the relevant instructions, performs actions only within its tool/permission model, and reports results with evidence.

## Lifecycle

1. **First-run doctor:** detect tools, offer installation with consent, register MCP where supported, verify live read-only calls.
2. **Design council:** determine concept and core loop, differentiate it, set realistic MVP scope, create a written design decision record.
3. **Owner approval:** freeze a final directive with acceptance criteria and excluded features.
4. **Vertical slice:** build one actually playable, polished, tested loop before large content expansion.
5. **Production:** milestone ledger, owned workstreams, source-controlled Luau/Rojo and Blender assets, test-first changes, server-side validation.
6. **Independent QA:** static checks, Studio runtime, multiple clients, bad input, persistence, performance and UI devices. Skipped checks are never marked passed.
7. **Private release candidate:** reconcile Git SHA, saved private place and evidence. The creator approves any public publication.

## Why a single skill with 41 references?

Long, always-on prompts consume context and are hard to maintain. AutoBlox routes to small modules under `references/practices/`, loading only what each task needs. The topics cover game architecture, debugging, gameplay, camera, input, UI, economy, characters, physics, security, code review, deployment and more. They are **original Roblox-focused writeups**, not bundled copies of third-party skill files.

## Tools and connectors

- **Roblox Studio official MCP:** optional but necessary for agent-driven Studio inspection and in-app verification.
- **Blender:** source-owned assets via CLI and/or the separately reviewed optional MCP addon.
- **Git/GitHub:** version control; public creation, remote changes and release always require explicit authorization.
- **Rojo/Rokit/Luau tooling:** recommended for repeatable source builds and checks.
- **Other MCP/web research:** optional per user/tool availability. Never assume all agents share the same plugins or credentials.

No feature, test or public-repository update is considered completed solely because a subagent reported success. The coordinator verifies actual artifacts or records limitations. No changes should compromise existing games or saved player data.
