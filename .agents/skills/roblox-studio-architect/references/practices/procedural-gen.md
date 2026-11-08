# Procedural Gen — Roblox Studio Architect

Origin reviewed: awesome-gamedev/procedural-gen
Activate when: Random maps, spawns, encounters, loot or rotating content
Outcome: Make procedural content reproducible, fair and verifiable.

## Original Roblox production method

1. Specify the seed source and ownership: match/server, player-specific, or common daily/weekly; never trust a client-chosen authoritative seed.
2. Generate pure data from a seeded RNG before instantiating geometry, then validate safety rules and budgets.
3. Check reachability, spawn clearance, loot distributions, enemy capacity and player-count adaptations.
4. Separate cosmetic variety from consequential randomness; use server-adjudicated outcomes and documented weighting.
5. Save the seed/parameters for reproducing difficult bug reports and retain deterministic fixture seeds.

## Evidence required

- Replay identical seeds with matching content and alternate seeds without invalid geometry.
- Automate distribution and reachability checks across many representative seeds.

## Guardrail

Never let unbounded random retries or global RNG create irreproducible soft-locks.

Other skills are optional sources of inspiration; this playbook is original project guidance, not a vendored copy.
