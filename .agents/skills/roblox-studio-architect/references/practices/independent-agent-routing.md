# Independent Agent Routing — Roblox Studio Architect

Origin reviewed: Superpowers/dispatching-parallel-agents
Activate when: Parallel investigations, assets or testing with non-overlapping ownership
Outcome: Get genuine independent progress without clobbering shared files.

## Original Roblox production method

1. Decompose the work into tasks with separate files, outputs and contracts; identify serial dependencies before dispatch.
2. Give each agent exact scope, baseline revision, acceptance, evidence format and prohibited changes.
3. Allow parallel analysis broadly; allow parallel edits only with isolated worktrees or explicit file ownership.
4. Centralize source integration and run a fresh combined test after all agent results arrive.
5. If subagents are unavailable, execute the same ownership plan sequentially instead of claiming parallel work.

## Evidence required

- Owner/agent matrix showing outputs, changed paths, conflicts, tests and integration commit.
- Combined regression results beyond individual agent success claims.

## Guardrail

Do not assign two editors to the same Roblox Studio place or module concurrently.

Other skills are optional sources of inspiration; this playbook is original project guidance, not a vendored copy.
