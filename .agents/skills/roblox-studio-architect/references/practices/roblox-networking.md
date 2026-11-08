# Roblox Networking — Roblox Studio Architect

Origin reviewed: awesome-gamedev/roblox-networking
Activate when: Remotes, replication, multiplayer consistency, streaming or anti-exploit review
Outcome: Make all consequential decisions server-owned and safe under unreliable input.

## Original Roblox production method

1. Inventory every RemoteEvent/RemoteFunction and its caller; write an input and output contract with allowed types and maximum sizes.
2. For requests validate membership, phase, state, distance, ownership, cooldowns, monotonically increasing identifiers and target existence.
3. Keep arbitrary client Instances, positions, prices, damage and rewards out of authoritative trust paths; resolve targets server-side.
4. Minimize broadcast scope and frequency. Account for streaming, out-of-order messages, temporary disconnection and round resets.
5. Use idempotent and fenced operations when concurrent actions or economic writes can race.

## Evidence required

- Test expected and malicious requests, rate-limit abuse, simultaneous players, joining mid-round and disconnects.
- Validate cross-client agreement by reading server-owned state, not by trusting locally displayed UI.

## Guardrail

Never treat server-side type checks alone as authorization or let client-provided results settle wins and rewards.

Other skills are optional sources of inspiration; this playbook is original project guidance, not a vendored copy.
