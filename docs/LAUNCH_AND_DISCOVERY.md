# AutoBlox — public discovery and creator growth playbook

**Project:** [reallyzip/autoblox](https://github.com/reallyzip/autoblox)  
**Stage:** v0.3.0-preview; cross-agent live integration and autonomous full-game completion are not certified.  
**Principle:** Demonstrate real usefulness, not artificial "viral algorithm" tricks.

## 0. The two launch prerequisites

**Download experience — live and checked 2026-11-07:** [full toolkit ZIP](https://github.com/reallyzip/autoblox/releases/download/autoblox-v0.3.0/autoblox-full-toolkit-v0.3.0-preview.zip), [master skill ZIP](https://github.com/reallyzip/autoblox/releases/download/autoblox-v0.3.0/autoblox-master-skill-v0.3.0-preview.zip), and [release notes + checksums](https://github.com/reallyzip/autoblox/releases/tag/autoblox-v0.3.0). These links point to uploaded assets on the published `autoblox-v0.3.0` release. The toolkit remains a preview in capability, even though GitHub lists this release as non-prerelease.

**GitHub topics — repository owner action required:** GitHub repository About panel → gear icon → Topics → add the list below → Save changes. Alternatively, with a locally authenticated GitHub CLI, run `gh api -X PUT repos/reallyzip/autoblox/topics --input topics.json`, using the committed UTF-8 [`docs/github-topics.json`](github-topics.json) file from this repository. From the repo root, run: `gh api -X PUT repos/reallyzip/autoblox/topics --input docs/github-topics.json`. Alternatively, `gh repo edit reallyzip/autoblox --add-topic "roblox,roblox-studio,roblox-development,luau,game-development,game-dev,ai-coding,ai-agents,agent-skills,model-context-protocol,mcp,blender,codex,claude-code,cursor,github-copilot,open-source,game-development-tools"`. GitHub allows a maximum of 20 lowercase/hyphenated topics.

Recommended 18 topics (relevant, not misleading): `roblox`, `roblox-studio`, `roblox-development`, `luau`, `game-development`, `game-dev`, `ai-coding`, `ai-agents`, `agent-skills`, `model-context-protocol`, `mcp`, `blender`, `codex`, `claude-code`, `cursor`, `github-copilot`, `open-source`, `game-development-tools`.

Topic relevance matters more than exhausting all 20 slots. Do not claim an untested capability is supported.

Also configure the **repository social preview** in Settings → General → Social preview. Upload `assets/autoblox-social-preview.png` (1200×630, approximately 56 KB), already present in the repo. Repository About website can point to the GitHub release until an independent website exists.

## 1. Positioning

**One sentence:** *AutoBlox turns a Roblox game idea into an agent-guided production plan, reusable source project, and verifiable private release-candidate workflow.*

**Accessible promise:** Open-source, local-first tooling for solo Roblox creators, small teams, and curious AI developers who want to get past a scattered stack of prompts.

**Truthful differentiation:** One master skill + 41 original playbooks; guided design council; specialist workflow routing; safe Roblox Studio/Blender MCP onboarding; multi-agent instructions; private-first release gates; repeatable tests and Git checkpoints.

**Never claim:** "one click makes a hit game", "fully autonomous game guaranteed", "all platforms validated", "works on every PC", "official Roblox/Anthropic/OpenAI tool", "top-rated" or "trending" before independently confirmed.

## 2. Target audiences in order

1. Roblox Studio beginners with a game idea but no clear architecture or development process.
2. Roblox Luau developers who need reliable testing, networking, asset and scope discipline.
3. AI coding-agent users building Roblox games with Codex, Claude Code, Cursor, Gemini, or Copilot.
4. Blender modelers, animators, UI designers and game-development collaborators.
5. Creator educators and YouTubers/TikTokers covering helpful free GitHub developer tools.
6. Broader open-source AI automation and indie game-development audiences after real demonstrations exist.

**Avoid broadening to unrelated audiences before the core Roblox users find it valuable.**

## 3. A proof-first launch kit for influencers

Before pitching creators, produce these honest, easy-to-reuse assets:
- 15-second vertical clip: design question → scaffold command → new project tree → private preview (only if an actual preview was achieved).
- 45–60-second screen capture: installation, prompting Codex/Claude, safe MCP onboarding, and one **real** tested Studio change.
- 3–6 minute walkthrough: create a game scaffold, review the design council, integrate a small game mechanic, demonstrate verification and caveats.
- PNG social card: `assets/autoblox-social-preview.png`; keep a mobile-readable 9:16 variant in the future.
- Simple B-roll: terminal, project files, Roblox Studio, Blender (owned footage, no invented game footage).
- Creator media notes: what AutoBlox is; what is tested; credit ReallyZip; license and install URLs; no required paid sponsorship.

Creators should be encouraged to **test and criticize the tool independently**, not repeat a supplied review as fact.

## 4. Four organic content pillars

**A. The 30-second problem/solution:** “I had a Roblox idea, but five tools and no workflow. Here's the missing setup.” Show the actual setup, not an imagined final game.

**B. Build in public:** One reproducible module per video—inventory, jump system, multiplayer validation, Blender prop, save/load. Show bugs fixed and real evidence.

**C. Free toolbox:** Compare what beginners already have (Studio, Luau, Blender) and how an agent skill organizes the workflow. Avoid paying for unnecessary tools.

**D. Reality checks:** “Can an AI agent finish a Roblox game?” Show what worked, what's still difficult, manual approvals and real test results. Authenticity converts better than overpromising.

## 5. Messaging and discovery keywords

GitHub search/readme: `Roblox Studio`, `Roblox game development`, `Luau`, `AI coding agent`, `Agent Skills`, `MCP server`, `Blender`, `Roblox game template`, `multiplayer testing`, `server-authoritative`, `game dev workflow`, `Codex`, `Claude Code`, `Cursor`.

Search-driven video phrases to test (not guaranteed “algorithm triggers”):
- how to make a Roblox game with AI
- Roblox Studio AI coding workflow
- free AI tools for Roblox developers
- Codex Roblox game development
- Claude Code Roblox Studio MCP
- Blender and Roblox Studio with AI
- Roblox game starter template GitHub
- build a Roblox game from scratch
- best GitHub repos for game developers
- AI agent game development toolkit

Use 2–4 relevant hashtags per video, varying by audience: `#RobloxDev`, `#RobloxStudio`, `#GameDev`, `#OpenSource`, `#AICoding`, `#Blender3D`, `#BuildInPublic`. No hashtag pileups or irrelevant trending tags.

## 6. Creator outreach

Prioritize micro-creators whose audiences actually build games. Look for Roblox scripting tutorials, Roblox UI/building tips, Blender-for-Roblox workflows, coding agent reviews, free GitHub tool showcases, or AI build-in-public series. Do not scrape private personal contact data, buy fake engagement, mass-message communities or imply endorsement.

**Short email/DM:**

> Subject: Free open-source Roblox + AI agent toolkit to test
>
> Hey — I built AutoBlox, a free toolkit that gives Codex, Claude Code and other AI coding agents a guided Roblox game-development workflow: design review, Luau/Blender routing, Studio MCP setup, tests and private release gates.
>
> It's a public preview, not a one-click finished-game generator. If you cover useful Roblox or GitHub tools, feel free to test it, break it, or compare it honestly with your existing workflow.
>
> Repo: https://github.com/reallyzip/autoblox
> Downloads: https://github.com/reallyzip/autoblox/releases/tag/autoblox-v0.3.0
>
> No sponsorship or positive review expected. Feedback is welcome.

Contact small numbers of highly relevant creators individually. Share disclosure terms if compensation or gifts are ever introduced.

## 7. Copy-ready launch posts

### Roblox developer post

> I made AutoBlox — a free, open-source toolkit for building Roblox games with AI coding agents.
>
> Instead of asking an agent to “make me a game” and hoping for the best, AutoBlox starts with a game-design meeting, scopes a playable build, routes specialized skills, and requires real Studio testing before the final handoff.
>
> Supports Codex, Claude Code and other agents through project adapters. Includes Blender/Roblox Studio MCP setup guidance.
>
> This is a preview: feedback and bug reports are welcome.
>
> https://github.com/reallyzip/autoblox
>
> #RobloxDev #GameDev #OpenSource

### AI coding audience

> AI agents can write a lot of Luau. The harder part is knowing what to build, what to test, and when a Roblox game is actually ready.
>
> AutoBlox is my open-source attempt at solving that workflow: design council → final spec → small milestones → specialist playbooks → Studio QA → private release candidate.
>
> Codex, Claude, and other agents can use the same project template.
>
> Try the preview: https://github.com/reallyzip/autoblox
>
> #AICoding #AgentSkills #RobloxStudio

### GitHub repository round-up pitch

> One free GitHub repo worth testing if you make Roblox games: ReallyZip/AutoBlox. It bundles an Agent Skill, 41 task-specific playbooks, starter templates, Blender/Studio onboarding, and evidence-based release checks. The tool is still a preview, which makes it an interesting real-world candidate to test instead of a “magic prompt” showcase.
>
> https://github.com/reallyzip/autoblox

### 15-second short-video script

> “Want to make a Roblox game with AI? Don’t start with a giant prompt. Start with a game plan.”
>
> Show: AutoBlox repo → download → project scaffold → specialist skill → real Studio result.
>
> “AutoBlox is free and open source. Link in the description.”

Only show an actual game result if produced and verified.

## 8. Thirty-day rollout

| Window | Work | Measure |
|---|---|---|
| Days 1–3 | Confirm release assets, topics, social preview, README clarity, docs; recruit 3–5 independent testers | Working download, install completion, reproducible issues |
| Days 4–7 | Publish one walkthrough and three honest short clips; post in appropriate Roblox developer communities where allowed | Qualified repo visits, full ZIP downloads, install feedback |
| Week 2 | Produce two small proof-of-build demos, compare Codex/Claude setup; invite 5–10 niche creators to test | Reproduced projects, stars, saves, creator replies |
| Week 3 | Address top blockers, publish changelog and bug-fix clip; request GitHub Issues from users | Issue response time, repeat usage, genuine contributors |
| Week 4 | “What we learned” post, independent comparisons, community examples, next preview release | Returning users, downloads per release, stars/forks, validated testimonials |

No need for an aggressive daily posting quota. Publish when there is useful evidence, a strong clip, or a meaningful improvement.

## 9. Tracking

Review weekly: unique GitHub visitors (where available), referrers, release downloads, stars/forks, meaningful issues/PRs, tester setup success, successful project scaffolds, verified MCP connections, first-playable demos, and repeat users willing to recommend it.

Use URLs with UTM parameters for creator posts when appropriate, but GitHub's in-repo analytics won't automatically show all attribution.

Define good early traction as **real users successfully using the toolkit**, not raw star count. Never purchase stars, views, comments, downloads or positive reviews.

## 10. Next milestone: trustworthy proof

Before an aggressive “best AI game development repo” campaign, publish one reproducible end-to-end small Roblox game created with AutoBlox, including the scope, agent, setup, exact checkpoint, gameplay video, test evidence, and honest limitations. This is the strongest credibility asset for programmers and creators.

## Reference sources

- GitHub topic rules: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics
- GitHub social previews: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/customizing-your-repositorys-social-media-preview
- YouTube Shorts discovery: https://support.google.com/youtube/answer/11914225?co=YOUTUBE._YTVideoType%3Dshorts&hl=en
- TikTok Creator Search Insights: https://newsroom.tiktok.com/creator-search-insights?lang=en
- Roblox Developer Forum: https://devforum.roblox.com/rules

No sponsored promotion or creator contact has been performed by this document.
