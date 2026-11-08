# Root Cause Investigation — Roblox Studio Architect

Origin reviewed: Superpowers/systematic-debugging
Activate when: Bug, flake, crash, failing test, broken Studio behavior or regression
Outcome: Understand the failure before changing the code.

## Original Roblox production method

1. Reproduce the issue and record exact inputs, client count, game state, device, error and revision.
2. Trace data and control flow from symptom to source across server/client boundary; compare a known-good checkpoint if available.
3. Write one falsifiable hypothesis and minimal probe; observe whether it explains the failure.
4. Fix the responsible cause with the smallest complete change, including affected callers and cleanup.
5. Rerun the reproduction and a neighboring regression test; remove probes and temporary fixtures.

## Evidence required

- Before/after reproduction, root-cause explanation, diff and verification environment.
- Known remaining uncertainty clearly stated.

## Guardrail

Do not apply a third speculative patch without investigating why earlier hypotheses failed.

Other skills are optional sources of inspiration; this playbook is original project guidance, not a vendored copy.
