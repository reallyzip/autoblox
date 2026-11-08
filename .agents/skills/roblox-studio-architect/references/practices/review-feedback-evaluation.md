# Review Feedback Evaluation — Roblox Studio Architect

Origin reviewed: Superpowers/receiving-code-review
Activate when: Handling peer, user or automated code-review suggestions
Outcome: Use reviewer feedback as evidence, not unquestionable authority.

## Original Roblox production method

1. Read the entire report, locate the actual code path and reproduce any claimed defect where possible.
2. Classify correctness, safety, performance, architecture and preference suggestions separately.
3. Accept valid changes, challenge unsupported refactors with measurements, and ask only for genuinely ambiguous owner choices.
4. Implement accepted findings one at a time with tests; make exceptions explicit and track rejected points.
5. Keep the reply factual and avoid performative agreement.

## Evidence required

- Traceable disposition for each issue: fixed, rejected with reason, deferred with owner decision, or blocked.
- New verification after each high-risk correction.

## Guardrail

Never add a new dependency or rewrite working code solely because a generic reviewer preferred it.

Other skills are optional sources of inspiration; this playbook is original project guidance, not a vendored copy.
