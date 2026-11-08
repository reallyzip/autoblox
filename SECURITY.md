# Security policy

The toolkit contains instructions, local Python scaffolding and an optional Git hook. It includes no API tokens, automatic network calls, Roblox account actions, global configuration changes or auto-installed marketplace extensions.

Never commit Roblox credentials, local session cookies, personal files or protected player data. Review any optional tool, hook or Studio connector permissions before enabling. For private vulnerability reports, avoid exposing exploitable details in a public issue until they can be safely handled.

The `--release-candidate` structural validator reads local evidence files but cannot attest their authenticity. Human review and real Roblox Studio testing remain required before public visibility changes.


## AI-agent MCP setup (v0.2 preview)

MCP tools may read or modify the user's local Roblox Studio place or execute code in Blender. Require user approval before configuring tools, installing addon code or enabling permissions. Roblox Studio's own built-in MCP is the preferred source. The optional community Blender MCP can execute Python and network requests; even `BLENDER_MCP_SAFE_MODE=1` is not a complete sandbox. Avoid arbitrary one-line remote shell installers, preserve existing config, and do not store secrets in repository MCP JSON. Verify a harmless read-only tool call against the intended local test scene before any edit.
