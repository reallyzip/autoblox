# Performance Optimization — Roblox Studio Architect

Origin reviewed: awesome-gamedev/performance-optimization
Activate when: Slow frames, memory growth, network spikes or heavy asset scenes
Outcome: Ship measurable improvements against explicit target hardware budgets.

## Original Roblox production method

1. Define target hardware tiers, scene, client count and frame/memory/network goals before optimizing.
2. Capture a baseline with Roblox MicroProfiler, Script Performance, network stats and memory tools where available.
3. Locate the dominant cost: scripts, physics, geometry/materials, UI, replication or asset loads. Fix that cost first.
4. Use pooling, event-driven updates, streaming, LOD and geometry reuse only when a measurement supports them.
5. Rerun the exact scenario after changes, preserve visual/play quality, and reject changes without convincing improvement.

## Evidence required

- Report before/after measurements, test platform, session duration and confidence limitations.
- Observe long-session join/leave/respawn and real-client frame behavior if accessible.

## Guardrail

Do not claim mobile optimization based on a powerful desktop Studio viewport.

Other skills are optional sources of inspiration; this playbook is original project guidance, not a vendored copy.
