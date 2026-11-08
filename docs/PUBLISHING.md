# Publishing AutoBlox to your GitHub account

This repository is designed to be public, but **publishing modifies a real GitHub account**. Never run the publisher until you have inspected the source and intend to make it public.

## One-command publication (from the toolkit directory)

Install [Git](https://git-scm.com/downloads) and [GitHub CLI](https://cli.github.com/), sign in via `gh auth login`, and confirm `gh auth status` uses the intended account.

```bash
python3 scripts/publish_github.py --owner reallyzip --repo autoblox --yes-public
```

Windows PowerShell: `py scripts/publish_github.py --owner reallyzip --repo autoblox --yes-public`.

The script:

1. Runs offline tests and the package verifier.
2. Builds two ZIPs and SHA256SUMS in ignored `dist/`.
3. Initializes local Git if needed, commits the public toolkit, and creates **public** `reallyzip/autoblox` using your authenticated `gh` account.
4. Pushes the repository and version tag without force.
5. Creates the tagged prerelease and uploads ZIPs and checksums.
6. Reads GitHub's repository and release metadata to confirm publication.

If creation succeeds but a later step fails, inspect GitHub and retry with `--resume` only when the same repository and origin are confirmed. The script never force-pushes or overwrites an unrelated repository.

## Manual alternative

1. Create a public empty repository named `autoblox` under your personal GitHub account. **Do not initialize with a README, .gitignore or license** if you intend to push the provided complete directory.
2. From the extracted AutoBlox project root, run tests and `python3 scripts/build_release.py`.
3. `git init -b main`, `git add -A`, `git commit -m "release: AutoBlox v0.3.0-preview"`, `git remote add origin https://github.com/reallyzip/autoblox.git`, `git push -u origin main`.
4. `git tag v0.3.0-preview` and `git push origin v0.3.0-preview`.
5. Use GitHub's Releases UI to create a prerelease from that tag and attach both ZIP files and `dist/SHA256SUMS`; alternatively use `gh release create` with the same files.
6. Open the README and both release downloads in a signed-out browser to confirm they're public.
7. In GitHub repository Settings, optionally use `assets/autoblox-social-preview.png` as the social preview artwork, and add topics such as `roblox`, `roblox-studio`, `luau`, `ai-agent`, `claude-code`, `codex`, `blender`, `mcp`, `game-development`.

For future releases, bump `VERSION`, update `CHANGELOG.md`, run tests and the release builder, then tag the verified commit. The optional manually triggered `.github/workflows/release.yml` can build/upload release assets after the repository is created and Actions are authorized.

## Public-release safety checklist

- Confirm all included files are yours to publish and follow [LICENSE](../LICENSE) / [THIRD_PARTY_NOTICES.md](../THIRD_PARTY_NOTICES.md).
- Exclude access tokens, project-private config, unpublished Roblox place IDs, user data and personal paths.
- Avoid implying that private Upkeep game assets or third-party MCP code are bundled.
- Review README claims: offline tests do not mean Studio/Blender MCP has passed live end-to-end tests.
- Confirm preview badge, download links, issue templates and release artifacts.
