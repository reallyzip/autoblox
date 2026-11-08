# Source skill coverage and original custom replacements

This suite was reviewed against the Upkeep project on 2026-11-07 and consists of **41 original Roblox-specific practice modules**, all under `references/practices/`. The master skill loads a small selection on demand.

- **Awesome Gamedev Agent Skills:** all 19 pinned project-local SKILL.md files read, source revision `19d93f97c9c1ea0f8b306e77aa81e0d3e352d3e9`, Apache-2.0. Original counterparts retain matching topic names with entirely new Roblox-focused steps.
- **Ponytail:** public Ponytail core, review, audit, debt, gain and help SKILL.md files read from `DietrichGebert/ponytail` (MIT). New counterparts: `lean-implementation`, `change-review`, `whole-repo-audit`, `technical-debt-ledger`, `measured-impact`, `engineering-mode-guide`. The 'ultra' term denotes deeper review intensity, not a distinct installed skill.
- **Caveman:** one project-local skill read; new counterpart: `concise-final-report`, focused on evidence-preserving handoffs.
- **Superpowers:** 14 available skills read: brainstorming, dispatching-parallel-agents, executing-plans, finishing-a-development-branch, receiving-code-review, requesting-code-review, subagent-driven-development, systematic-debugging, test-driven-development, using-git-worktrees, using-superpowers, verification-before-completion, writing-plans, writing-skills. New original corresponding processes have different names in `coverage.json`.
- **Impeccable:** named in Upkeep's AGENTS.md but its exact installed source was not available for review in this session. `visual-quality-gate` is our own independently written visual-review practice; do not claim an upstream source audit was completed.
- **Additional Upkeep procedures:** Roblox networking audit, approval-gated release, concise output, root cause, supervisor checklist, Blender-first art, profiling and staged verification are woven through the master references. They are workflow concepts, not all separately installable upstream skills.

No upstream skill files, scripts, hooks or source code are redistributed in this package. Inspiration/attribution is documented separately. If later vendors change their APIs or licensing, consult their actual current source before combining code.
