# Technical Debt Ledger — Roblox Studio Architect

Origin reviewed: Ponytail/ponytail-debt
Activate when: Collecting deliberate shortcuts, waivers and post-release debt
Outcome: Make compromises visible, time-bounded and actionable.

## Original Roblox production method

1. Search TODO, FIXME, waiver records, deferred animation slots, compatibility fallbacks and release blockers.
2. For each entry record source file, reason, user impact, current risk, date, owner and objective exit criteria.
3. Separate acceptable aesthetic polish debt from security, player-data and public-release blockers.
4. Link each debt item to a tested project milestone; remove entries only after evidence of resolution.
5. Keep the list short and factual so it guides releases rather than becoming a duplicate roadmap.

## Evidence required

- Debt count by severity plus exact references and next action.
- No silent closure of waived or untested items.

## Guardrail

Never use a TODO comment to excuse a known critical release blocker.

Other skills are optional sources of inspiration; this playbook is original project guidance, not a vendored copy.
