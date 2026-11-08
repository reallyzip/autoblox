# Audio Design — Roblox Studio Architect

Origin reviewed: awesome-gamedev/audio-design
Activate when: Audio, voice, music, ambience, feedback or loudness tasks
Outcome: Make events recognizable, intelligible and comfortable at varied volume settings.

## Original Roblox production method

1. Inventory audio emitters, sound ownership, and existing volume preferences before making new assets. Separate music, ambience, UI cues and spatial gameplay effects by intent.
2. Create an audio event matrix: source, trigger, priority, audience, variants, max simultaneity and cleanup owner. Use native Sound/SoundGroup behavior and approved assets.
3. Duck or deprioritize nonessential audio when safety-critical cues or teammate messages are active. Provide mute and reduced-effects preferences where relevant.
4. Prefer a few original layered cues over dozens of repeated generic stock sounds; vary sample or pitch mildly without changing the meaning of an alert.
5. Keep playback client-presentational when possible; only server-confirmed game state may trigger rewarding or consequential sounds.

## Evidence required

- Solo and two-client audible event ordering, mute/reset and repeated-shift cleanup.
- Document source/license of every imported sound and measure actual playback behavior rather than asserting quality from file presence.

## Guardrail

Do not let music drown spoken/gameplay information or make an audio cue grant rewards.

Other skills are optional sources of inspiration; this playbook is original project guidance, not a vendored copy.
