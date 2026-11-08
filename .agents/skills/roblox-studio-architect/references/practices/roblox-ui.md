# Roblox Ui — Roblox Studio Architect

Origin reviewed: awesome-gamedev/roblox-ui
Activate when: Creating ScreenGuis, menus, HUD, settings, tooltips, shops or chat-related UI
Outcome: Make all user-facing interface states editable, usable and resilient.

## Original Roblox production method

1. Inspect existing StarterGui/PlayerGui templates and UI ownership; avoid rebuilding every screen with monolithic scripts.
2. Use scalable UDim2 layouts, constraints, safe-area-aware insets and design tokens; account for longer labels and localization.
3. Keep UI state a presentation of server-confirmed facts where needed, and use Activated plus explicit gamepad focus handling.
4. Keep screen transitions reversible, distinguish loading/failed/confirmed operations and release event connections on teardown.
5. Treat TextChatService and Roblox core UI restrictions as platform responsibilities; style without bypassing filtering or privacy.

## Evidence required

- Keyboard, phone, gamepad focus, screen resize, respawn and multiple-open cycles.
- Check clipping, contrast, readable text, touch target sizes and emergency message priority.

## Guardrail

Never bind purchase success to a local button click or assume UI success means a server operation persisted.

Other skills are optional sources of inspiration; this playbook is original project guidance, not a vendored copy.
