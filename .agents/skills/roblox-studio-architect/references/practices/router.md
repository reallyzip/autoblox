# Router — Roblox Studio Architect

Origin reviewed: awesome-gamedev/router
Activate when: Choosing specialist playbooks for a new task or project phase
Outcome: Load only the guidance needed rather than every reference at once.

## Original Roblox production method

1. Classify work by task risk (design, implementation, bug, security, art, release) and Roblox subsystem before selecting references.
2. Pick one primary discipline playbook plus at most two supporting ones; add security and verification for state-changing paths.
3. Reuse selection for adjacent tasks; reclassify only when the work genuinely pivots.
4. If a specialist reference or connector is unavailable, use the existing engine workflow and state the limitation rather than hunting indefinitely.
5. Never allow a generic framework recipe to override the project-specific AGENTS.md or current official Roblox API behavior.

## Evidence required

- Explain selected playbooks in one concise routing note when it materially changes the plan.
- Confirm no conflicting source ownership or duplicate tool installation was introduced.

## Guardrail

Do not load the entire playbook library into context or start from a skill search on every minor edit.

Other skills are optional sources of inspiration; this playbook is original project guidance, not a vendored copy.
