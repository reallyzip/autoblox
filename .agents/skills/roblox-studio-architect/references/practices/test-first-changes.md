# Test First Changes — Roblox Studio Architect

Origin reviewed: Superpowers/test-driven-development
Activate when: Feature logic, behavior changes, bug fixes or contract refactors
Outcome: Define behavior in executable checks before trusting implementation.

## Original Roblox production method

1. State the user-visible behavior and server invariants; choose a small automated or isolated Studio fixture suited to the risk.
2. Create an initial check that fails for the intended reason or capture an existing failing reproduction.
3. Implement the minimum change, rerun the failing test, then run nearby regression cases.
4. Refactor duplication only after the behavior passes and remains understandable.
5. Where Studio-only visual behavior cannot be unit tested, define explicit manual/automated viewport acceptance before editing.

## Evidence required

- Failing baseline and passing follow-up with actual run output, plus runtime verification where required.
- No false report of a failing test when the test never executed.

## Guardrail

Tests that assert internal implementation details cannot substitute for gameplay or networking correctness.

Other skills are optional sources of inspiration; this playbook is original project guidance, not a vendored copy.
