# Game Feel — Roblox Studio Architect

Origin reviewed: awesome-gamedev/game-feel
Activate when: Actions mechanically work but feel unresponsive or unsatisfying
Outcome: Give important actions timely feedback without changing server decisions.

## Original Roblox production method

1. Identify meaningful player actions and rank their importance: input acknowledgment, task progress, success, failure and danger.
2. For each action choose at most a few matching feedback channels: sound, animation, light, UI, haptics, particles or a very small camera response.
3. Attach feedback to a known authoritative result for rewards, combat outcomes and work completion; speculative client previews must remain cosmetic.
4. Tune response timing and intensity on the lowest intended device tier. Add reduced-motion and low-effects options.
5. Compare adjacent actions and remove feedback that masks danger, reduces readability or becomes tiring after a full session.

## Evidence required

- Record input-to-feedback behavior, repeated-action spam behavior and independent reduced-effects verification.
- Test actual controller, touch and multiplayer observer views when available.

## Guardrail

Do not freeze a shared simulation to sell a local impact or stack uncontrolled camera shake.

Other skills are optional sources of inspiration; this playbook is original project guidance, not a vendored copy.
