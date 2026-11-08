# Roblox Datastores — Roblox Studio Architect

Origin reviewed: awesome-gamedev/roblox-datastores
Activate when: Saving player progression, inventory, unlocks, economy or settings
Outcome: Protect owned player data across failures, retries and cross-server sessions.

## Original Roblox production method

1. Define versioned server-owned schema, bounded values, migration rules and data that must never be client-trusted.
2. Use UpdateAsync transactions for mutation, appropriate session ownership/leasing, idempotent receipt identifiers and bounded retries.
3. Separate Studio test stores or test backends from production. Never accidentally modify live player data during QA.
4. Define on-join, delayed load, autosave, disconnect and shutdown behavior, including outage and owner-loss states.
5. Publish confirmed save status to UI without fabricating successful writes or discarding valid existing progress.

## Evidence required

- Migration, duplicate purchase, reconnect, cross-server, rapid leave and injected DataStore failure tests.
- Persisted totals must match transaction receipts after simulated retries and server restart.

## Guardrail

Never overwrite valid production data with empty defaults because a read failed.

Other skills are optional sources of inspiration; this playbook is original project guidance, not a vendored copy.
