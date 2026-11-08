# Roblox Physics — Roblox Studio Architect

Origin reviewed: awesome-gamedev/roblox-physics
Activate when: Assemblies, raycasts, overlap queries, collision flags, network ownership
Outcome: Make geometric interactions safe, precise and affordable.

## Original Roblox production method

1. Choose raycast, overlap, constraints or contact events according to required accuracy and trust, not convenience.
2. Create a clear collision matrix; distinguish CanCollide, CanTouch and CanQuery for every important part.
3. Filter raycasts/overlap targets to valid gameplay objects and check distances and line of sight on the server where needed.
4. Keep cosmetic meshes noncollidable when dedicated bounds/collision proxies provide the actual gameplay geometry.
5. Bound query frequency and instance lifetimes, and test moving assemblies at expected speeds.

## Evidence required

- Server/client geometry agreement and no unexpected collisions in critical routes.
- Confirm physics ownership, constraints and reset cleanup in multi-client Studio.

## Guardrail

Never use Workspace visual prop placement as an authoritative gameplay hitbox by accident.

Other skills are optional sources of inspiration; this playbook is original project guidance, not a vendored copy.
