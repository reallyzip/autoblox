# Lean Implementation — Roblox Studio Architect

Origin reviewed: Ponytail/ponytail (lite-full-ultra concepts)
Activate when: Choosing implementations, dependencies, complexity and refactors
Outcome: Find the smallest end-to-end correct solution, not the smallest patch.

## Original Roblox production method

1. Before coding, trace the requested behavior across actual caller, server, client, tests, assets, UI, profile migrations and Studio deployment.
2. Compare reuse of an existing module or Roblox API against new code; choose the least complex approach that completes the contract.
3. Intensity levels are review depth, not permission to omit work: light for tiny UI text, standard for ordinary systems, intensive for risky multiplayer, persistence, migrations and release.
4. Make a bounded diff, then inspect broken callers and orphaned assets. Remove speculative abstractions and one-off libraries.
5. If a simplification reduces security, validation, accessibility, maintainability or data recoverability, reject it.

## Evidence required

- Diff reviewed for necessary changes, test evidence and rollback risk.
- Rationale for any new dependency, service or abstraction.

## Guardrail

Do not mistake fewer lines or fewer tests for better engineering.

Other skills are optional sources of inspiration; this playbook is original project guidance, not a vendored copy.
