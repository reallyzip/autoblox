#!/usr/bin/env python3
"""Opt-in public GitHub repository + preview release publisher using the user's gh login.

Requires an authenticated GitHub CLI, Git and explicit --yes-public consent.
No implicit tokens, force pushes, account setting changes or unapproved overwrites.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def checked(*args: str, cwd: Path = ROOT, capture: bool = False):
    return subprocess.run(list(args), cwd=str(cwd), text=True, check=True,
                          stdout=subprocess.PIPE if capture else None,
                          stderr=subprocess.PIPE if capture else None)


def git_origin() -> str:
    out = subprocess.run(["git", "remote", "get-url", "origin"], cwd=str(ROOT),
                         text=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    return out.stdout.strip() if out.returncode == 0 else ""


def origin_matches(origin: str, owner: str, repo: str) -> bool:
    target = owner + "/" + repo
    return origin.rstrip("/") in {
        "https://github.com/" + target,
        "https://github.com/" + target + ".git",
        "git@github.com:" + target,
        "git@github.com:" + target + ".git",
    }


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--owner", default="reallyzip")
    p.add_argument("--repo", default="autoblox")
    p.add_argument("--tag", default="v" + (ROOT / "VERSION").read_text(encoding="utf-8").strip())
    p.add_argument("--yes-public", action="store_true", help="Explicit authorization to publish source and release assets publicly")
    p.add_argument("--resume", action="store_true", help="Resume an interrupted publication to the identical verified repository")
    args = p.parse_args()
    target = args.owner + "/" + args.repo
    print("Target PUBLIC GitHub repository:", target)
    print("Tag:", args.tag)
    print("Source:", ROOT)
    if not args.yes_public:
        print("DRY RUN: no publication. Re-run with --yes-public after reviewing the source and terms.")
        return 0
    if not shutil.which("gh"):
        p.error("GitHub CLI not installed: https://cli.github.com/ (then run: gh auth login)")
    if not shutil.which("git"):
        p.error("Git is required; install Git and retry")
    try:
        checked("gh", "auth", "status")
        checked(sys.executable, "-m", "unittest", "discover", "-s", "scripts/tests", "-v")
        checked(sys.executable, "scripts/verify_package.py")
        checked(sys.executable, "scripts/build_release.py")
        if not (ROOT / ".git").exists():
            checked("git", "init", "-b", "main")
        origin = git_origin()
        if origin and not origin_matches(origin, args.owner, args.repo):
            raise RuntimeError("Existing Git origin points elsewhere: " + origin)
        existing = subprocess.run(["gh", "repo", "view", target, "--json", "nameWithOwner"],
                                  cwd=str(ROOT), stdout=subprocess.DEVNULL,
                                  stderr=subprocess.DEVNULL)
        if existing.returncode == 0 and not args.resume:
            raise RuntimeError("Repository already exists. Review it and rerun with --resume to prevent accidental replacement.")
        checked("git", "add", "-A")
        unstaged = checked("git", "diff", "--cached", "--name-only", capture=True).stdout.strip()
        if unstaged:
            checked("git", "commit", "-m", "release: AutoBlox public preview " + args.tag)
        if existing.returncode != 0:
            if origin:
                raise RuntimeError("Remote already exists but repository lookup failed; refusing risky creation")
            checked("gh", "repo", "create", target, "--public", "--source", ".", "--remote", "origin", "--push",
                    "--description", "AutoBlox — a cross-agent Roblox AI game-development skill and starter toolkit")
        else:
            if not origin:
                # User created an empty repository in GitHub's UI. Only attach the
                # exact, authenticated owner/repo after --resume, never guess.
                checked("git", "remote", "add", "origin", "https://github.com/" + target + ".git")
            if not origin_matches(git_origin(), args.owner, args.repo):
                raise RuntimeError("Cannot resume: local Git origin does not match selected repository")
            # Only push the current HEAD on the configured branch: never force.
            checked("git", "push", "-u", "origin", "HEAD")
        version = args.tag.lstrip("v")
        local_tag = subprocess.run(["git", "rev-parse", "-q", "--verify", "refs/tags/" + args.tag],
                                   cwd=str(ROOT), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if local_tag.returncode != 0:
            checked("git", "tag", args.tag)
        tag_sha = checked("git", "rev-list", "-n", "1", args.tag, capture=True).stdout.strip()
        head_sha = checked("git", "rev-parse", "HEAD", capture=True).stdout.strip()
        if tag_sha != head_sha:
            raise RuntimeError("Existing local release tag differs from current HEAD; aborting")
        checked("git", "push", "origin", args.tag)
        release = subprocess.run(["gh", "release", "view", args.tag, "--repo", target, "--json", "url"],
                                 cwd=str(ROOT), text=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        if release.returncode != 0:
            assets = [
                "dist/autoblox-full-toolkit-v" + version + ".zip",
                "dist/autoblox-master-skill-v" + version + ".zip",
                "dist/SHA256SUMS",
            ]
            for path in assets:
                if not (ROOT / path).is_file():
                    raise RuntimeError("Missing required built release asset " + path)
            cmd = ["gh", "release", "create", args.tag, *assets, "--repo", target,
                   "--verify-tag", "--title", "AutoBlox " + args.tag,
                   "--notes-file", "docs/RELEASE_NOTES.md"]
            if "-" in args.tag:
                cmd.append("--prerelease")
            checked(*cmd)
        checked("gh", "repo", "view", target, "--json", "url,visibility")
        checked("gh", "release", "view", args.tag, "--repo", target, "--json", "url,isPrerelease,assets")
    except (subprocess.CalledProcessError, RuntimeError) as exc:
        print("PUBLICATION INCOMPLETE:", exc, file=sys.stderr)
        print("No force push or destructive recovery attempted. Review remote/release state before retrying --resume.", file=sys.stderr)
        return 1
    print("PUBLICATION COMPLETE: https://github.com/" + target)
    print("Release: https://github.com/" + target + "/releases/tag/" + args.tag)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
