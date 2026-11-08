# Camera Systems — Roblox Studio Architect

Origin reviewed: awesome-gamedev/camera-systems
Activate when: Camera movement, framing, obstruction, motion sickness or respawn issues
Outcome: Keep important action readable while respecting default Roblox camera controls.

## Original Roblox production method

1. State the viewing contract: first or third person, action framing, allowed zoom, lock-on if any, and mobile/controller parity.
2. Use the Roblox camera module/default camera when it already satisfies the contract; add owned offsets rather than replacing the whole system.
3. Calculate damping from delta time, maintain clamped motion, and solve obstruction without piercing walls or losing aim.
4. Keep cosmetic shake and recoil independent from authoritative movement; make additive contributions reversible and coexist with other camera systems.
5. Provide reduced motion and avoid per-frame event connection churn.

## Evidence required

- Repeated jump/landing and respawn test verifies camera returns to baseline without drift.
- Observe desktop/controller/touch rotation and enclosed spaces at low and high frame rates.

## Guardrail

Never write camera offsets without an explicit restore path or treat render events as a source of gameplay truth.

Other skills are optional sources of inspiration; this playbook is original project guidance, not a vendored copy.
