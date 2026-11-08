# Subagent Task Loop — Roblox Studio Architect

Origin reviewed: Superpowers/subagent-driven-development
Activate when: Delegating independent implementation tasks to coding-agent subagents
Outcome: Preserve fresh focus, source ownership and verifiable integration.

## Original Roblox production method

1. Split approved design into small deliverables with stable interfaces, filenames, test commands, and a clear handoff shape.
2. Assign one implementer and a distinct reviewer to high-risk tasks; worktrees or explicit no-overlap rules prevent collisions.
3. Require each implementer to return changed paths, tests run, unresolved failures and actual evidence.
4. Integrate only completed revisions, perform a fresh combined test, record task state and release file ownership.
5. Use sequential execution when tools cannot provide independent agents or isolation.

## Evidence required

- Progress ledger and supervisor acceptance linked to exact commits and test reports.
- No duplicate writes and no undisclosed bypass of project permissions.

## Guardrail

Never let subagent prompts grant privileges beyond the owner's approved scope.

Other skills are optional sources of inspiration; this playbook is original project guidance, not a vendored copy.
