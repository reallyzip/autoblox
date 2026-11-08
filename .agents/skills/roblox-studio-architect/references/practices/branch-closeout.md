# Branch Closeout — Roblox Studio Architect

Origin reviewed: Superpowers/finishing-a-development-branch
Activate when: Committing, pushing, merging, creating PRs or finalizing a development branch
Outcome: Preserve history and hand off a verified, reviewable change set.

## Original Roblox production method

1. Inspect git status, diff and branch tracking; run the required tests before staging.
2. Confirm destination branch and user authorization for push/PR; never infer permission to force-push or publish a Roblox place.
3. Create a focused commit with a meaningful summary and evidence reference; push only after verifying no secrets or generated junk.
4. Report commit SHA, branch, remote, push status and any known conflict. Do not erase uncommitted other-author work.
5. Keep Roblox place publication, Git push and production launch as three separate operations with separate proof.

## Evidence required

- Exact commit SHA, push output and recovery instructions.
- Post-integration regression results when merging or rebasing.

## Guardrail

Never call an unpublished place deployed, or treat a GitHub push as a Roblox production release.

Other skills are optional sources of inspiration; this playbook is original project guidance, not a vendored copy.
