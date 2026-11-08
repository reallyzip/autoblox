# Evidence Gated Completion — Roblox Studio Architect

Origin reviewed: Superpowers/verification-before-completion
Activate when: Before saying done, fixed, tested, deployed or ready
Outcome: Make claims no stronger than fresh evidence.

## Original Roblox production method

1. For each completion claim specify the test or artifact that could verify it and the exact expected result.
2. Run the test in the relevant environment; read the full result and check failures instead of relying on truncated output.
3. Distinguish static syntax, Rojo build, Studio simulation, multi-client runtime, physical device and published private cloud evidence.
4. When an unavailable API or human/device check blocks verification, label it unverified and leave the corresponding gate open.
5. Before a release claim cross-check latest Git source SHA against actual saved/published Studio scripts and asset templates.

## Evidence required

- Verification matrix with test, date, revision, environment, result and evidence path.
- No known blocking issues hidden behind a cumulative pass count.

## Guardrail

Never turn user-waived tests into passes or interpret absence of errors as proof of playability.

Other skills are optional sources of inspiration; this playbook is original project guidance, not a vendored copy.
