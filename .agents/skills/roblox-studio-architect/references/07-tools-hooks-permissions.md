# Tools, connectors, Git hooks and permission boundaries

## Local-first defaults

All tools are optional. A basic new project needs Roblox Studio, Git, source editor, and Rojo when using this template. Blender is strongly preferred for original 3D production and retained editable sources. Rokit can pin Rojo, StyLua, Selene and Luau language tooling. Never auto-install dependencies without reviewing source and obtaining applicable permission.

## Connectors — capability registry, not automatic access

GitHub: inspect repo/branches/issues/actions and push only with user authority and a configured remote. Roblox Studio MCP/Studio AI: inspect scenes, import, run tests and save private place only when connected and authorized. Context7/official docs: check current API semantics. Firecrawl/browser: research Roblox Creator standards, developer discussion and market evidence; respect site rules and cite findings. Figma and other design tools are optional, not required. No connector may silently expand account permissions.

## Hooks

The project template includes an example `.githooks/pre-commit` for **local fast source checks only**. It is **not installed** by the scaffolder. An owner can explicitly opt in with `git config core.hooksPath .githooks` after inspecting it. The sample hook never makes network requests, publishes a game, changes account settings, installs packages or deletes files. Avoid lifecycle hooks that inject arbitrary remote instructions on every prompt or subagent start.

CI can run only offline checks without live Studio credentials. A green GitHub workflow does not prove Roblox Studio playability or published parity.

## Autonomous work permissions

The owner can approve the project implementation scope and routine Git commits/pushes. Material design changes, account permissions, paid tools, public publishing, monetization, destructive data operations and force push require specific approval. At time boundaries, finish only recoverable steps, then report and wait.
