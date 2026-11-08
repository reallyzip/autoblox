# Roblox Luau — Roblox Studio Architect

Origin reviewed: awesome-gamedev/roblox-luau
Activate when: Adding or changing Roblox Luau scripts, modules and services
Outcome: Keep a maintainable server/client/shared structure with testable contracts.

## Original Roblox production method

1. Identify execution location and authoritative owner before writing code. Inspect neighboring modules, remote definitions and conventions.
2. Use typed Luau where it improves safety and meaningful module boundaries without introducing needless wrappers.
3. Prefer events and bounded tasks over uncontrolled loops; disconnect signals and destroy temporary instances on lifecycle transitions.
4. Validate every client-to-server request and avoid trusting replicated attributes written or proposed by clients.
5. Write or adapt focused tests around state transitions and integrate via the existing Rojo/Studio source path.

## Evidence required

- StyLua/lint/type checks if available, Rojo build, Studio Output and representative Server & Clients tests.
- Report exact changed modules and replayable test cases.

## Guardrail

Never place a client-authoritative inventory, damage or currency operation in LocalScripts.

Other skills are optional sources of inspiration; this playbook is original project guidance, not a vendored copy.
