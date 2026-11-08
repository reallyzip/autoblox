# Changelog

## v0.3.0-preview — Public-ready AutoBlox packaging

- Rebrand public repository as **AutoBlox**, retaining the `roblox-studio-architect` canonical skill identifier for backwards compatibility.
- Add public README banner, installation and MCP guides, agent-specific copy-paste prompts, FAQ, architecture, roadmap, and sample first-session dialog.
- Add deterministic release archives and SHA-256 sums, local GitHub CLI publisher, optional manual GitHub Actions release workflow, issue and PR templates.
- Retain 41 original Roblox-focused playbooks and existing local-first safety defaults.
- Preview only: live cross-agent MCP connections and actual autonomous game shipping remain unverified.

# Changelog

## 0.2.0-preview — Cross-agent, consent-based Studio/Blender MCP onboarding

- Support Codex, Claude Code, Cursor, Gemini CLI and GitHub Copilot/VS Code via canonical skill and native entry-point adapters, with generic stdio fallback.
- First-run diagnostics and interactive opt-in install offers for Roblox Studio and Blender on supported OSes.
- Official Roblox Studio built-in MCP integration and live-verification procedure.
- Optional, explicitly consented third-party Blender MCP addon with security disclosure and safe-mode configuration.
- Agent-specific JSON merge or Codex CLI setup, safe config backup/conflict handling, no silent changes.
- New setup documentation/evidence files, expanded safety notices, and tests.
- No apps, MCP servers or credentials installed in the package builder environment.

# Changelog

## 0.1.0-preview — 2026-11-07

- Introduced one master Roblox production skill with 41 original practice playbooks covering the verified Upkeep skill inventory and independently authored visual-review guidance.
- Added project-neutral Rojo/Luau starter, design meeting and directive templates, source/evidence/release records, Blender asset inventory and local-first permissions.
- Added overwrite-safe project scaffolder, offline structural validator and a release-candidate gate that fails for a new untested project.
- Added optional local Git hook and offline CI; neither automatically installs connectors or publishes games.
- Passed four offline unit tests and one generated project smoke test. Real Codex agent scenario trials and Roblox Studio end-to-end tests have not been run.
