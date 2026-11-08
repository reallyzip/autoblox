# Production supervisor — implement after design approval

## Milestone progression

**M0: source-safe setup.** Identify project identity, restore checkpoint, branch and Studio source owner. Set toolchain and tests; do not inherit arbitrary game-specific assets.

**M1: vertical slice.** Make the first complete loop fun: join -> clear objective -> player action -> server outcome -> responsive feedback -> result -> replay. Check solo and multiplayer assumptions early.

**M2: content systems.** Expand only approved enemies/quests/rounds/maps/abilities using reusable, bounded data definitions. Add persistence and safety while contracts are small.

**M3: production visuals.** Validate representative art in game, then scale coherent Blender/native assets, character work, animation, audio, UI and environmental detail. Keep asset manifest and import parity.

**M4: complete game.** All specified content and modes integrated; no known critical/high defect; on-device controls, onboarding and repeat sessions function.

**M5: private release candidate.** Final independent audit, static/build/Studio/security/performance tests, source and private cloud parity, explicit owner test-drive handoff. Public launch remains separate.

## Supervisor task contract

Every task has ID, goal, owner/agent, source paths, touched systems, dependencies, acceptance cases, risk, authoritative proof and fallback checkpoint. Supervisor checks changed paths for collisions and rejects any subagent's unsupported 'done' claim. Before changing an established system, compare against verified source and define rollback.

Use the task ledger at `docs/PROGRESS.md` with DONE / IN_PROGRESS / BLOCKED / UNVERIFIED. Preserve actual commands, outputs and latest commit. At the deadline, end new development with enough time for cleanup, tests and authorized commit/push; never force completion by fabricating passes.

## Supervision checklist

- Current design approved and non-goals enforced.
- Exact repository and private place identified.
- Ownership/no conflicting writes enforced.
- First playable loop remains fun and finishable.
- Security boundaries and saves protected.
- Blender sources and original asset provenance retained.
- UI, chat, controls and device fallbacks tested.
- Solo and multiplayer loop verified.
- Static, runtime and published evidence clearly separated.
- Critical/high issues closed with evidence.
- Git commit and authorized push confirmed.
- Private place source parity and save identity confirmed if accessible.
- Commercial, monetization and public-release permission still gated.
