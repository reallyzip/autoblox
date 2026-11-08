# Capability and playbook routing

## Installed versus available versus proven

For each provider record whether a capability is present, authenticated, usable with the specific project and actually tested. Tool exposure alone proves none of the latter. Never create credentials or fake an installed connector. Optional connectors can include GitHub, Roblox Studio MCP/Studio AI, browsing, documentation retrieval and research services.

A baseline local toolchain can use Git, Python, Rokit, Rojo, StyLua, Selene, Luau LSP, official Roblox Studio and Blender. Versions are project-pinned only after testing and do not need repeated installation. No requirement to install Node/npm, Figma, Wally, TestEZ or any specific provider merely to follow this system.

## Routine selection

Classify the task by impact: UI/art, gameplay, multiplayer trust, persistent data, security, external action or release. Start with a single domain playbook. Add secondary playbooks only for distinct risks, such as character animation combined with networking. Apply evidence gating before marking done.

For new game development, inspect whether a runtime exists. Do not copy code from another game to save time without reviewing its license, design fit and underlying assumptions. A studio skill is workflow guidance, not a dependency installer.

## Registry record

Every tool row should include tool name, why used, permission scope, install state, auth state, runtime smoke test, version or source, alternatives, and conflicts. Update only when materially changed. Prefer using existing project capability registry rather than redoing a comprehensive survey every task.

## Original source inspiration

All 41 practice modules in `practices/` are newly authored Roblox-focused methods. They map to reviewed upstream concepts but are not copies. `coverage.json` contains exact source-to-module mapping and distinguishes read sources from the uninspected 'Impeccable' mention.
