# Roblox Studio Workflow — Roblox Studio Architect

Origin reviewed: awesome-gamedev/roblox-studio-workflow
Activate when: Editing live Studio places, Rojo mapping, imported assets or publishing private QA
Outcome: Keep one source of truth and distinguish actual runtime evidence from offline success.

## Original Roblox production method

1. Before modifying a place identify active DataModel, universe/place identity, audience and authoritative source (Rojo versus Studio).
2. Keep production code and templates in source control; treat disposable Studio fixtures and temporary Workspace assets as transient.
3. Use native Studio for hierarchy, import, input simulation, runtime Output and Server & Clients validation. Map tools to correct execution contexts.
4. Preserve a one-editor/one-Studio-operator lock during automated work; reconcile saved source after native editor actions.
5. Before any private publication compare all production scripts/assets to intended source, save a recovery copy and record actual published version.

## Evidence required

- Pass a verification ladder: static/build, solo, multi-client, cross-device emulation, actual device if available, private cloud save.
- Record which environment produced each result and never promote waived tests into passes.

## Guardrail

Never publish publicly based on private QA evidence or confuse a saved local place with a published experience.

Other skills are optional sources of inspiration; this playbook is original project guidance, not a vendored copy.
