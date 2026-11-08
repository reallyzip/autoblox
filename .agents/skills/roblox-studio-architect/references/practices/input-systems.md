# Input Systems — Roblox Studio Architect

Origin reviewed: awesome-gamedev/input-systems
Activate when: Keyboard, mouse, touch, controller, keybinding or action-state tasks
Outcome: Maintain a single accessible action contract across inputs.

## Original Roblox production method

1. List game verbs before keys: move, interact, jump, sprint, open menu, use ability; separate press, hold, toggle and analog intent.
2. Prefer Roblox-native character controls and ContextActionService. Preserve platform-reserved controls and existing text-chat focus.
3. Route intents into validated server actions only when gameplay authority is needed; leave visual-only actions local.
4. Handle device switching, input cancellation, death, tool ownership, menus, focus loss and respawn as explicit state transitions.
5. Map mobile controls around thumb regions and test controller focus; avoid duplicate bindings that fire on one press.

## Evidence required

- Action table plus real input test evidence for keyboard/mouse, gamepad and touch simulation.
- Verify input while chat is focused, after a repair is canceled, and after a device switch.

## Guardrail

Never equate a synthetic remote call with a real button-press or assume keyboard-only controls suffice.

Other skills are optional sources of inspiration; this playbook is original project guidance, not a vendored copy.
