# Save Systems — Roblox Studio Architect

Origin reviewed: awesome-gamedev/save-systems
Activate when: Schema evolution, backups, restore, settings or checkpoint persistence
Outcome: Make saved state small, versioned, migratable and recoverable.

## Original Roblox production method

1. Separate transient session state from durable server-owned state and identify data-loss impact of every change.
2. Define schema version, default policy, validation and pure migration functions before adding new fields.
3. Use idempotent writes and version-aware conflict handling; for Roblox online progression, defer to Roblox DataStore semantics rather than filesystem rename patterns.
4. Create backup/restore and rollback plans for incompatible changes. Avoid storing Instance references as profile data.
5. Use load failure and stale-data states in UI rather than silently resetting a profile.

## Evidence required

- Test fresh, old schema, malformed, missing, partial-failure and rollback scenarios.
- Verify cross-server re-entry and saved inventory invariants under duplicate operations.

## Guardrail

Never confuse local file durability with Roblox cloud persistence or assume a DataStore outage is a new-user profile.

Other skills are optional sources of inspiration; this playbook is original project guidance, not a vendored copy.
