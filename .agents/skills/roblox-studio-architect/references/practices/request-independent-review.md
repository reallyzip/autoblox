# Request Independent Review — Roblox Studio Architect

Origin reviewed: Superpowers/requesting-code-review
Activate when: Before significant commits, merges or game release milestones
Outcome: Find defects that the implementer may have normalized.

## Original Roblox production method

1. Give reviewers requirements, base/head revisions, changed files, verified cases and the areas where confidence is low.
2. Use at least one reviewer focused on exploits, persistent data and concurrency for consequential multiplayer changes.
3. Ask for file-and-line-grounded findings with severity, reproduction or reasoning and test recommendations.
4. Reconcile feedback against the actual source; fix critical/high issues and rerun tests.
5. For a release review, examine end-to-end first-session play and studio/publication parity, not just code style.

## Evidence required

- Independent review summary, issue dispositions and final pass/fail gate.
- Explicit statement of coverage limits and reviewer independence.

## Guardrail

Do not use an agent thumbs-up as proof that actual multiplayer or mobile tests ran.

Other skills are optional sources of inspiration; this playbook is original project guidance, not a vendored copy.
