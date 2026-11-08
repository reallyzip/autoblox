# Engineering Mode Guide — Roblox Studio Architect

Origin reviewed: Ponytail/ponytail-help
Activate when: Selecting development review depth or explaining the system
Outcome: Choose the appropriate diligence without changing user permissions.

## Original Roblox production method

1. Light mode: contained copy/style edit with no persistence, networking or new authorization paths.
2. Standard mode: most implementation tasks; audit caller impact, tests, recoverability and UI parity.
3. Intensive mode: economy, anti-exploit, networking, schema migration, cross-device controls, public launch and major architecture.
4. Every mode retains correctness, security, testing, accessibility and data safety. Intensive adds independent review and broader scenarios.
5. Choose modes from task risk, not how many tokens are left.

## Evidence required

- Record risk level and why in the task plan; downgrade only after proven lower risk.

## Guardrail

Modes must never silently change hooks, marketplace permissions or publish access.

Other skills are optional sources of inspiration; this playbook is original project guidance, not a vendored copy.
