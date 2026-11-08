# Roblox Characters — Roblox Studio Architect

Origin reviewed: awesome-gamedev/roblox-characters
Activate when: Avatars, rigs, animations, emotes, accessories, respawn and tools
Outcome: Make characters predictable across spawn cycles, supported rigs and clients.

## Original Roblox production method

1. Define R6/R15 or custom-rig support explicitly and inspect current Humanoid/Animator, default Animate and avatar settings.
2. Separate player-scoped settings from character-scoped references; cancel pending operations on CharacterRemoving and check generation tokens after yielding.
3. Use attachments/accessory fitting and compatible Animator tracks; make ownership priority explicit among movement, tools, repairs and emotes.
4. Prepare graceful fallback for unsupported rig/asset IDs, imperfect hair clearance and missing accessories.
5. Keep cosmetic animation client-side when safe; never let a visual pose decide authoritative gameplay outcomes.

## Evidence required

- Spawn, rapid respawn, death, tool swap, outfit change and peer-observer animation matrix.
- Verify in-game front/side/back silhouettes and accessory collision/clipping across representative avatars.

## Guardrail

Never capture a Humanoid once and assume it remains valid after respawn.

Other skills are optional sources of inspiration; this playbook is original project guidance, not a vendored copy.
