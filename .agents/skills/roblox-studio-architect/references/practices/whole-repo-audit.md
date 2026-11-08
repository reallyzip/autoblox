# Whole Repo Audit — Roblox Studio Architect

Origin reviewed: Ponytail/ponytail-audit
Activate when: Auditing a full Roblox project or inherited repository
Outcome: Identify product, architectural and production risks in ranked order.

## Original Roblox production method

1. Start with README, AGENTS, Rojo mapping, build tools, critical gameplay flows, profiles, remotes, CI and private publication trail.
2. Map modules and their ownership to reveal duplicated managers, circular requires, dead assets and unbounded services.
3. Sample high-consequence code deeply: authoritative combat/rewards, client remotes, data stores, loops, memory and asset provenance.
4. Distinguish confirmed defects from concerns requiring Studio reproduction. Avoid a superficial list of everything that could happen.
5. Give a ranked repair backlog with a concise deletion/merge suggestion only where behavior can be preserved.

## Evidence required

- Audit scope, commit inspected, missing evidence and priority-ranked findings.
- A regression plan for any recommended deletion or major consolidation.

## Guardrail

Never rewrite an entire game merely because its original organization differs from your preferred architecture.

Other skills are optional sources of inspiration; this playbook is original project guidance, not a vendored copy.
