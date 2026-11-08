# Change Review — Roblox Studio Architect

Origin reviewed: Ponytail/ponytail-review
Activate when: Reviewing a patch, PR, feature or recent commit
Outcome: Catch errors and unnecessary complexity before integration.

## Original Roblox production method

1. Identify the starting revision and proposed diff; read the full affected call chain and external contracts.
2. Check correctness, remote trust boundaries, concurrency, player profiles, initialization and teardown under expected load.
3. Look for unnecessary wrappers, duplicated state, new dependencies and abandoned flags, then propose removal only if safe.
4. Assign each finding a severity, file location, reproduction or proof, and minimally sufficient correction.
5. Review tests independently of the implementer and rerun cases after high-risk fixes.

## Evidence required

- Actionable findings with grounded paths and priority; a clean report states exactly what was checked.
- Security, persistence and multi-client risks verified independently.

## Guardrail

Do not write a style-only critique while ignoring exploitable or data-loss bugs.

Other skills are optional sources of inspiration; this playbook is original project guidance, not a vendored copy.
