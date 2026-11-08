# Frequently asked questions

### Is AutoBlox free?
The toolkit is MIT-licensed. Roblox Studio, Blender, and many local development tools are available free of charge. Your chosen AI model/API, remote infrastructure or optional third-party tools may have separate costs. No paid subscription is included or required by the toolkit.

### Can it build a complete Roblox game from one prompt?
It provides a structured approach, not a guarantee. After a design meeting and approval, a capable connected agent can implement and test progressively. Game size, model limits, tool permissions, available computer time and human acceptance still matter.

### Does it work with Claude, Codex, Cursor, Gemini and Copilot?
It provides files and prompts for those environments. Actual skill discovery, MCP config and tool support differ by version. See [agent guides](AGENT_GUIDES.md) and verify the active client.

### Does the setup installer silently install Roblox Studio or Blender?
No. It detects common locations, suggests official sources and asks before configuration changes. Full application installation may need your OS's installer dialogs.

### Is Blender MCP required?
No. You can create Blender assets through local scripts/CLI. Community Blender MCP is a useful optional integration, not required for design meetings or offline programming. Review its security implications before use.

### Why is the Roblox place private by default?
A saved private release candidate allows meaningful technical and creative review before public launch. Public publishing, paid products, youth safety, rating and platform requirements remain the creator's responsibility.

### What are the 41 custom skills?
They are **playbook files inside one master Agent Skill**, not 41 installed plugins. The master skill loads them as needed. This avoids overlapping hooks and unneeded context.

### Can I add my own skills or genre templates?
Yes. See [CONTRIBUTING.md](../CONTRIBUTING.md). Keep content original, use a small repeatable example, test the instructions with negative scenarios, and preserve appropriate licenses.

### Why is a terminal or Python needed?
The scripts scaffold a project and validate release metadata. The `SKILL.md` and Markdown guides are readable without Python, but creating a project and running checks is more reliable through the provided scripts.

### Can I publish this or games made with it?
Yes, subject to your rights in the game, licensed assets, Roblox terms and applicable laws. MIT licensing of AutoBlox does not grant rights to third-party models, music, logos, trademarks or Roblox services.
