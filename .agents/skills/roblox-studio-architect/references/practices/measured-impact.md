# Measured Impact — Roblox Studio Architect

Origin reviewed: Ponytail/ponytail-gain
Activate when: Assessing refactor or optimization gains
Outcome: Measure the effect of lean decisions instead of claiming imaginary savings.

## Original Roblox production method

1. Choose comparable metrics before change: file/module count, affected calls, test time, load latency, CPU, memory or frame stability.
2. Compare equal builds and scenes with consistent avatar/device/client counts.
3. Account for code removed and new maintenance burden while retaining validation and user-facing quality.
4. Record test environment and uncertainty; if metrics cannot be collected, state that they are unknown.
5. Do not perform optimization work solely to improve the scoreboard.

## Evidence required

- Table of baseline, follow-up, delta, method and any unmeasured variables.
- Reproduction commands when measurements were automatic.

## Guardrail

Never fabricate performance percentages or imply an external benchmark applies to this project.

Other skills are optional sources of inspiration; this playbook is original project guidance, not a vendored copy.
