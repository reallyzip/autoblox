# Physics Tuning — Roblox Studio Architect

Origin reviewed: awesome-gamedev/physics-tuning
Activate when: Unstable objects, collision jitter, tunneling, mass or moving-platform tuning
Outcome: Make physical behavior consistent and bounded under network conditions.

## Original Roblox production method

1. Choose whether the mechanic truly needs physics or should be scripted/anchored. Specify desired failure modes and interaction limits.
2. Declare collision groups and query policy separately. Preserve predictable assemblies, attachments and constraints.
3. Use server authority for consequential physics outcomes; understand when ownership and latency affect observed motion.
4. Measure velocities, body scale, contact stability and solver behavior under expected load before introducing new forces.
5. Tune one parameter at a time and ensure cleanup for temporary assemblies and constraints.

## Evidence required

- Solo/two-client collision observation and representative low/high velocity cases.
- Check jitter after pause, respawn, teleport and ownership transfer.

## Guardrail

Never use an old physics body mover or Touched-only hit logic without justified constraints and validation.

Other skills are optional sources of inspiration; this playbook is original project guidance, not a vendored copy.
