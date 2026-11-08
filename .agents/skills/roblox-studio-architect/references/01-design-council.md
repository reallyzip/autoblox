# Design Council — professional preproduction meeting

The meeting is for making choices, not running down a generic questionnaire. First inspect the game's existing files, screenshots, reference art, or description. If the user provided enough to proceed, propose options directly. Ask one consequential question at a time where needed.

## Agenda

1. **Experience promise:** who plays, why they click, and the enjoyable action in the first minute. Identify cooperative/competitive/solo expectations.
2. **Core loop:** input -> immediate feedback -> challenge -> outcome -> earned change -> compelling replay. Write it as a 30-second explanation.
3. **Game identity:** genre plus a clear original differentiator. Compare comparable games for patterns, not copied visuals, names, systems, maps, code or copyrighted material.
4. **Gameplay depth:** mechanics, controls, edge cases, character abilities, progression, content variety, economy and social requirements. Keep the smallest compelling vertical slice.
5. **Player & device fit:** age suitability, mobile/controller/PC, accessibility, voice/text chat and Roblox permission limits, server size and low-end budget.
6. **World & art:** game-specific visual bible, production references, characters, silhouettes, color/material constraints and Blender-versus-native authoring decisions.
7. **Technical viability:** server authority, streaming, persistent saves, exploit model, asset ownership, Rojo/project source, Studio test feasibility and Git recovery.
8. **Enjoyment and retention:** first-session comprehension, meaningful rewards, repeatable variation, friends, fairness, no manipulative dark patterns. Research claims must be sourced and assessed.
9. **Business & compliance:** public name conflicts, Roblox Community Standards/maturity, audio/IP, creator account assets, moderation, monetization posture and explicit launch permission.
10. **Boundaries:** what is not included, known risks, budget/time limit and evidence needed before release.

## Output contract

Produce one approved `docs/DESIGN_DECISIONS.md` containing the product pitch, core loop, input/platform matrix, content budget, art bible, multiplayer design, economy, target devices, security assumptions, measurable vertical-slice gates, final release candidate criteria, non-goals, rejected alternatives, decision date and owner approval status. Include `docs/FINAL_DIRECTIVE.md` as a concise implementation authority only after the user approves the design. Mark speculative ideas as `PROPOSED`, not `APPROVED`.

## Autonomy boundary

The user can authorize the **whole approved scope** once; after that, autonomous task-by-task execution should proceed without repetitive approval requests. Preserve explicit gates for money, external publishing, deleting data, changing public audience, secret management or changing a material game design decision.
