# Quality ladder and release-candidate gate

Use the verification record in `docs/VERIFICATION.json` and additional evidence artifacts in `docs/evidence/`. A script can check report completeness but cannot attest that Studio tests actually happened.

## L0 — Source and reproducibility

Git worktree state, dependencies pinned, Rojo mapping parsed, code formatted/linted and static tests run. Record a full command with exit code, date and revision. Fail here if paths cannot be reproduced.

## L1 — Single-client runtime

Real Studio execution of the entire first-session loop, expected menu/input flow, gameplay outcome, teardown, first respawn and repeated round. No console errors or broken visible assets. Do not claim Studio test from source-only scripts.

## L2 — Multiplayer runtime

Actual Server & Clients simulation with 2 and intended maximum players, simultaneous actions, contested targets, join/leave/rejoin, latency where testable, reconnect and malformed remotes. Clients agree on authoritative outcomes.

## L3 — Player data and risk

Schema migration, production/test store isolation, failed writes, purchase duplication, remote flood, unintended object ownership, private info and asset permissions. Use isolated test keys. Never reset live data to 'fix' a test.

## L4 — Device, experience and performance

Keyboard, phone/touch, controller focus; representative avatar rigs; motion/accessibility; actual Roblox renderer and memory/frame/network metrics where accessible. Mark emulator-only and owner-waived checks accurately. Gameplay feedback and replay motivation are inspected, not inferred from passing tests.

## L5 — Private cloud parity

Verify correct universe/place and PRIVATE audience, source SHA, count/hash of production scripts and assets, saved/published version if permitted. Keep Git push and Roblox publication identity distinct.

## Verdicts

`BLOCKED`: critical/high issue, destructive risk, permission issue, broken core loop or missing critical evidence. `READY_FOR_OWNER_PLAYTEST`: available gates pass or appropriately documented limitations do not hide core correctness. `PUBLIC_RELEASE_APPROVED`: additionally requires explicit creator authorization and current Roblox eligibility/commercial/content compliance gates. No automation may upgrade the latter on its own.
