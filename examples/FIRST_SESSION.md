# Example: First game creation session

This is a **sample interaction**, not a transcript of a completed game.

**You:** "I want a four-player game where people repair a stranded space station. I like short rounds, a funny tone and accessible mobile controls."

**AutoBlox agent:** "We should decide whether the fun is coordinated repairs under time pressure, puzzle-solving, or combat. I'd recommend timed repairs with shared resource shortages for a one-building first release. Would you rather emphasize teamwork or chaos?"

**You:** "Teamwork with chaos, but I want to enjoy it solo too."

**AutoBlox agent:** "Then I'll design a small, soloable 6–10 minute shift loop with three failure types, readable station layouts and optional co-op roles. Before writing production code, I'll present a complete directive with what is excluded, the art direction, controls, repeat-play goals and testable milestones."

**You:** "Approved. Build it."

**AutoBlox agent:** "I'll start with one fully playable, testable shift and expand only approved systems. I will report actual Rojo builds and Studio multiplayer results, distinguish untested devices, and retain private publishing controls."

## The output that matters

- `docs/DESIGN_DECISIONS.md`: user-approved product identity and core-loop decisions.
- `docs/FINAL_DIRECTIVE.md`: implementation scope, tasks, acceptance checks, exclusions and publishing gates.
- `docs/PROGRESS.md`: milestone state, file ownership, blockers and commits.
- `docs/VERIFICATION.json`: actual tests and environments.
- Source files and editable Blender assets where needed.
- Saved PRIVATE release candidate only when verified and authorized.

A concept meeting should improve the idea, not stall it in endless questioning; a build should produce playable evidence, not just more documentation.
