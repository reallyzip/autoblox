# Isolated Workspaces — Roblox Studio Architect

Origin reviewed: Superpowers/using-git-worktrees
Activate when: Parallel tasks, experiments, risky refactors or branch isolation
Outcome: Keep experiments recoverable without corrupting the main working tree.

## Original Roblox production method

1. Inspect existing Git worktrees, uncommitted changes and repository policy before creating another workspace.
2. Prefer the active approved worktree; create a new one only when isolation adds value and a safe directory is available.
3. Use separate checkout/branch per isolated editor and share results through commits/patches, not simultaneous writes.
4. Run a clean baseline build and test in the new worktree before edits.
5. Keep worktrees until changes are integrated and recoverability is confirmed; clean up only with deliberate authorization.

## Evidence required

- Workspace path, branch, base SHA, baseline checks, final integration SHA.
- No data loss of existing working tree or Studio saved file.

## Guardrail

Never run broad destructive Git clean/reset commands merely to prepare a workspace.

Other skills are optional sources of inspiration; this playbook is original project guidance, not a vendored copy.
