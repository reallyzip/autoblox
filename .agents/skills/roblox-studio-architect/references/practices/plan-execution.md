# Plan Execution — Roblox Studio Architect

Origin reviewed: Superpowers/executing-plans
Activate when: Implementing an accepted multi-step task plan
Outcome: Complete scoped increments with checkpoints instead of endless planning.

## Original Roblox production method

1. Confirm the approved design, current HEAD, clean or preserved worktree, environment and required dependencies.
2. For each task: reproduce expected behavior, create a failing test if practical, implement bounded changes, run tests and record proof.
3. Mark progress only after tests, diff review and source integration; keep next-step context in a durable ledger.
4. Select any optional tools once, then focus on implementation. Replan if evidence contradicts the spec rather than forcing broken work.
5. At a deadline, checkpoint partial changes safely, preserve exact resume instructions and stop further edits.

## Evidence required

- Progress ledger with complete/partial/blocked state, commit identities and commands.
- The latest working checkpoint can be restored without reconstructing conversation history.

## Guardrail

Never mark a task done because code was written, an agent said done or a local mock passed.

Other skills are optional sources of inspiration; this playbook is original project guidance, not a vendored copy.
