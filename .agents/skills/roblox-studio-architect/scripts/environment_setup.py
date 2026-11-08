#!/usr/bin/env python3
"""Local-first, opt-in Roblox Studio / Blender / MCP setup assistant.

No network requests or mutations in the default inspection mode. Never confuses
MCP configuration with an actual agent-side tool invocation.
Python 3.9+, Windows/macOS/Linux (Roblox Studio only macOS/Windows).
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import platform
import shutil
import subprocess
import sys
import webbrowser
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

STUDIO_DOCS = "https://create.roblox.com/docs/studio/setup"
STUDIO_MCP_DOCS = "https://create.roblox.com/docs/studio/mcp"
BLENDER_DOWNLOAD = "https://www.blender.org/download/"
BLENDER_MCP_SOURCE = "https://github.com/ahujasid/mcp-for-blender"
UV_DOCS = "https://docs.astral.sh/uv/getting-started/installation/"

SUPPORTED_AGENTS = ("codex", "claude", "cursor", "gemini", "vscode", "copilot", "other")
CLI_NAMES = {"codex": "codex", "claude": "claude", "cursor": "cursor-agent", "gemini": "gemini", "vscode": "code", "copilot": "code"}


def _mac_studio_candidates(home: Path) -> List[Path]:
    return [Path("/Applications/RobloxStudio.app/Contents/MacOS/StudioMCP"), home / "Applications/RobloxStudio.app/Contents/MacOS/StudioMCP"]


def _windows_studio_candidates(env: Dict[str, str]) -> List[Path]:
    base = Path(env.get("LOCALAPPDATA", str(Path.home() / "AppData/Local")))
    return [base / "Roblox/mcp.bat"]


def detect_studio(system: str, home: Path, env: Dict[str, str]) -> Dict[str, Any]:
    if system == "Darwin":
        paths = _mac_studio_candidates(home)
        apps = [Path("/Applications/RobloxStudio.app"), home / "Applications/RobloxStudio.app"]
        app_installed = any(p.is_dir() for p in apps)
    elif system == "Windows":
        paths = _windows_studio_candidates(env)
        local = Path(env.get("LOCALAPPDATA", str(home / "AppData/Local")))
        versions = local / "Roblox/Versions"
        app_installed = versions.is_dir() and any(versions.glob("*/RobloxStudioBeta.exe"))
    else:
        return {"supported": False, "installed": False, "launcher": None,
                "mcp_launcher_present": False,
                "note": "Roblox Studio is officially available for Windows and macOS, not Linux."}
    found = next((p for p in paths if p.is_file()), None)
    installed = app_installed or bool(found)
    return {"supported": True, "installed": installed,
            "launcher": str(found) if found else None,
            "mcp_launcher_present": bool(found),
            "note": "Application detected separately from Studio MCP launcher; unusual install paths may need manual selection."}


def detect_blender(system: str, home: Path, env: Dict[str, str], which=shutil.which) -> Dict[str, Any]:
    command = which("blender")
    paths: List[Path] = []
    if system == "Darwin":
        paths = [Path("/Applications/Blender.app/Contents/MacOS/Blender"),
                 home / "Applications/Blender.app/Contents/MacOS/Blender"]
    elif system == "Windows":
        base = Path(env.get("ProgramFiles", r"C:\Program Files")) / "Blender Foundation"
        if base.is_dir():
            for folder in sorted(base.glob("Blender *"), reverse=True):
                paths.append(folder / "blender.exe")
    found = command or next((str(p) for p in paths if p.is_file()), None)
    return {"installed": bool(found), "executable": found,
            "note": "CLI/app-path detection is heuristic; verify Blender opens before declaring ready."}


def detect_agents(which=shutil.which) -> Dict[str, bool]:
    return {name: bool(which(exe)) for name, exe in CLI_NAMES.items()}


def report_environment(system: Optional[str] = None, home: Optional[Path] = None,
                       env: Optional[Dict[str, str]] = None, which=shutil.which) -> Dict[str, Any]:
    system = system or platform.system()
    home = home or Path.home()
    env = env if env is not None else os.environ.copy()
    return {"platform": system, "python": platform.python_version(),
            "roblox_studio": detect_studio(system, home, env),
            "blender": detect_blender(system, home, env, which),
            "uvx": which("uvx"), "agents": detect_agents(which),
            "mcp_live_verified": False,
            "note": "Installed and configured do not mean MCP connected. Verify an actual read-only tool call from the chosen agent."}


def stdio_servers(report: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    servers: Dict[str, Dict[str, Any]] = {}
    launcher = report["roblox_studio"]["launcher"]
    if launcher:
        if report["platform"] == "Windows":
            servers["Roblox_Studio"] = {"command": "cmd.exe", "args": ["/c", launcher]}
        else:
            servers["Roblox_Studio"] = {"command": launcher, "args": []}
    if report["blender"]["installed"] and report["uvx"]:
        # Third-party server: opt-in only. Safe mode is defense-in-depth, not a sandbox.
        servers["blender"] = {"command": report["uvx"],
                              "args": ["--python", "3.11", "mcp-for-blender"],
                              "env": {"BLENDER_MCP_SAFE_MODE": "1"}}
    return servers


def config_target(agent: str, project: Path) -> Tuple[Optional[Path], str]:
    path_map = {
        "claude": (project / ".mcp.json", "mcpServers"),
        "cursor": (project / ".cursor/mcp.json", "mcpServers"),
        "gemini": (project / ".gemini/settings.json", "mcpServers"),
        "vscode": (project / ".vscode/mcp.json", "servers"),
        "copilot": (project / ".mcp.json", "mcpServers"),
    }
    return path_map.get(agent, (None, ""))


def _read_dict(path: Path) -> Dict[str, Any]:
    if path.is_symlink():
        raise ValueError("MCP config is a symbolic link; manual review required before writing")
    if not path.exists():
        return {}
    result = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(result, dict):
        raise ValueError("MCP configuration root must be an object; refusing to modify")
    return result


def prepare_config(agent: str, project: Path, servers: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
    """Return a proposed change; never writes. Fail closed on conflicting keys."""
    dest, key = config_target(agent, project)
    if dest is None:
        raise ValueError(f"{agent} requires a client-specific CLI/config workflow; no unsafe generic write attempted")
    cfg = _read_dict(dest)
    old = cfg.get(key, {})
    if not isinstance(old, dict):
        raise ValueError(f"Existing {key} is not an object; refusing to modify")
    merged = dict(old)
    added, same = [], []
    for name, fields in servers.items():
        candidate = dict(fields)
        if agent == "vscode":
            candidate = {"type": "stdio", **candidate}
        if name in merged:
            if merged[name] != candidate:
                raise ValueError(f"Existing MCP server {name!r} differs; manual review required (never overwrite)")
            same.append(name)
        else:
            merged[name] = candidate
            added.append(name)
    cfg[key] = merged
    return {"path": dest, "data": cfg, "added": added, "unchanged": same}


def save_config(prepared: Dict[str, Any]) -> Optional[Path]:
    """Called only after user approval. Atomic write, with a timestamped backup."""
    path = prepared["path"]
    if not prepared["added"]:
        return None
    path.parent.mkdir(parents=True, exist_ok=True)
    backup = None
    if path.exists():
        stamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S-%f")
        backup = path.with_name(path.name + f".{stamp}.bak")
        shutil.copy2(path, backup)
    temp = path.with_name(path.name + ".new")
    try:
        temp.write_text(json.dumps(prepared["data"], indent=2) + "\n", encoding="utf-8")
        os.replace(temp, path)
    finally:
        if temp.exists():
            temp.unlink()
    return backup


def codex_command(server_name: str, server: Dict[str, Any]) -> List[str]:
    args = ["codex", "mcp", "add", server_name]
    for k, v in server.get("env", {}).items():
        args.extend(["--env", f"{k}={v}"])
    return args + ["--", server["command"]] + server.get("args", [])


def cli_registration(agent: str, project: Path, server_name: str, server: Dict[str, Any]) -> List[str]:
    if agent == "codex":
        return codex_command(server_name, server)
    if agent == "gemini":
        return ["gemini", "mcp", "add", "--scope", "project", server_name, server["command"]] + server.get("args", [])
    raise ValueError("Use project-scoped JSON MCP files for this agent")


def _confirm(message: str) -> bool:
    return input(message + " [y/N]: ").strip().lower() in {"y", "yes"}


def _run_command(cmd: List[str], cwd: Path, timeout_seconds: int = 300) -> bool:
    try:
        result = subprocess.run(cmd, cwd=str(cwd), check=False, timeout=timeout_seconds, text=True)
        return result.returncode == 0
    except (OSError, subprocess.TimeoutExpired) as e:
        print(f"Command failed: {e}")
        return False


def _install_offers(report: Dict[str, Any], interactive: bool) -> None:
    missing = []
    if not report["roblox_studio"]["installed"]:
        missing.append(("Roblox Studio", STUDIO_DOCS))
    elif not report["roblox_studio"].get("mcp_launcher_present", False):
        print("Roblox Studio seems installed, but its documented built-in MCP launcher wasn't found.")
        print("Update Studio through the official app/installer and check Studio > Assistant > Manage MCP Servers.")
    if not report["blender"]["installed"]:
        missing.append(("Blender", BLENDER_DOWNLOAD))
    for name, url in missing:
        print(f"INSTALL OFFER — {name}: {url}")
        if interactive and name == "Blender":
            manager = shutil.which("brew") if report["platform"] == "Darwin" else shutil.which("winget") if report["platform"] == "Windows" else None
            command = ([manager, "install", "--cask", "blender"] if report["platform"] == "Darwin" else
                       [manager, "install", "-e", "--id", "BlenderFoundation.Blender"] if report["platform"] == "Windows" else None)
            if manager and command:
                print("Optional, package-manager installation: " + subprocess.list2cmdline(command))
                if _confirm("Install Blender using the detected package manager? This downloads and runs a system installer"):
                    if _run_command(command, Path.cwd(), timeout_seconds=1200):
                        print("Package manager reports success. Rerun diagnostics to verify actual app presence.")
                    else:
                        print("Package manager failed; no installation success claim.")
                    continue
        if interactive and _confirm(f"Open the official {name} installer/download instructions in your browser?"):
            webbrowser.open(url)
    if not report["uvx"]:
        print(f"OPTIONAL BLENDER MCP DEPENDENCY — uv/uvx installer: {UV_DOCS}")
    if not report["roblox_studio"]["supported"]:
        print("Roblox Studio is not officially supported by this OS; use a Windows/macOS computer for Studio/MCP.")


def _offer_addon(report: Dict[str, Any], project: Path, interactive: bool) -> None:
    if not report["blender"]["installed"]:
        return
    if not report["uvx"]:
        print("Blender MCP addon cannot be installed until uvx is installed and detected. Rerun setup.")
        return
    print(f"THIRD-PARTY BLENDER MCP: {BLENDER_MCP_SOURCE}")
    print("Warning: addon enables agent-driven Python code execution inside Blender. Safe mode is not a sandbox.")
    if interactive and _confirm("Run the community Blender MCP addon installer on this computer?"):
        if _run_command([report["uvx"], "--python", "3.11", "mcp-for-blender", "install-addon"], project):
            print("Addon files installed. Enable MCP for Blender in Blender preferences; verify in Blender UI.")
        else:
            print("Addon installer failed; no success claim. Consult upstream documentation.")


def _mcp_registered_cli(agent: str, project: Path) -> Optional[List[str]]:
    """Return registered names if CLI listing succeeds; None if unavailable/unknown.

    A name appearing here does NOT mean the MCP server is connected.
    """
    if agent not in ("codex", "claude", "gemini", "cursor"):
        return None
    cmd = {"codex": ["codex", "mcp", "list"],
           "claude": ["claude", "mcp", "list"],
           "gemini": ["gemini", "mcp", "list"],
           "cursor": ["cursor-agent", "mcp", "list"]}[agent]
    if not shutil.which(cmd[0]):
        return None
    try:
        done = subprocess.run(cmd, cwd=str(project), capture_output=True,
                              text=True, timeout=10, check=False)
        if done.returncode != 0:
            return None
        lines = done.stdout.splitlines()
        # Conservative: tokenize the first field of lines, not substring guesses.
        return [line.strip().split()[0].rstrip(":") for line in lines if line.strip()]
    except (OSError, subprocess.TimeoutExpired):
        return None


def _offer_config(agent: str, report: Dict[str, Any], project: Path, interactive: bool) -> None:
    servers = stdio_servers(report)
    if not servers:
        print("No MCP servers can be configured from detected launchers. Install missing applications first.")
        return
    if agent in ("claude", "cursor", "vscode", "copilot", "gemini"):
        # Gemini can also use project config; prefer JSON to avoid unexpected CLI user settings.
        try:
            ready = prepare_config(agent, project, servers)
        except (ValueError, json.JSONDecodeError) as e:
            print(f"Config blocked: {e}")
            return
        print(f"Project MCP file: {ready['path']}\n  New: {', '.join(ready['added']) or '(none)'}; existing: {', '.join(ready['unchanged']) or '(none)'}")
        if interactive and ready["added"] and _confirm(f"Safely merge these servers into {ready['path']}? (backup existing file)"):
            backup = save_config(ready)
            print(f"Saved {ready['path']}; backup: {backup or '(new file)'}")
    elif agent == "codex":
        if not report["agents"].get("codex", False):
            print("Codex CLI not detected; install/open the client and rerun, or use Studio Quick Connect.")
            return
        print("Codex MCP registration is normally user-level (shared by projects). Review EACH command before approval.")
        registered = _mcp_registered_cli("codex", project)
        for name, server in servers.items():
            if registered is not None and name in registered:
                print(f"{name} already registered in Codex. Skipping duplicate; agent-side live verification still required.")
                continue
            cmd = codex_command(name, server)
            print("Proposed Codex command: " + subprocess.list2cmdline(cmd))
            if interactive and _confirm(f"Register {name} with Codex? (changes Codex MCP configuration)"):
                success = _run_command(cmd, project)
                print("Registration command succeeded; LIVE TOOL CALL STILL REQUIRED." if success else "Registration failed; review logs.")
    else:
        print("Generic stdio MCP agent: read docs/MCP_SETUP.md and configure via the agent's approved config UI.")
    print("Restart/reload the chosen AI client. The configuration alone does not prove a live connection.")


def _verification_guidance(agent: str) -> None:
    print("\nLIVE MCP VERIFICATION (mandatory, performed from inside the selected AI agent):")
    print("  1. Open Roblox Studio, sign in, open a disposable/test place; Assistant > ... > Manage MCP Servers")
    print("     > Enable Studio as MCP server; prefer Studio Quick connect to your agent.")
    print("  2. Confirm Studio's green MCP connection indicator. Agent must call list_roblox_studios")
    print("     (or the current equivalent) and READ a harmless detail from that open test place.")
    print("  3. Enable Blender MCP for Blender addon, start its local server; agent must call a")
    print("     read-only scene-inspection tool and receive an actual scene result.")
    print("  4. Verify the returned Studio ID / Blender scene correspond to the actual open apps.")
    print("  5. Record exact tool names, results and timestamp in docs/TOOL_CONNECTION_EVIDENCE.md.")
    print("  Until BOTH tool calls pass, report SETUP_INCOMPLETE—not CONNECTED.")
    print("  Studio docs: " + STUDIO_MCP_DOCS)
    print("  Blender bridge: " + BLENDER_MCP_SOURCE)
    if agent == "codex":
        print("  Registration check: codex mcp list")
    elif agent == "claude":
        print("  Registration check: claude mcp list ; inside Claude Code: /mcp")
    elif agent == "gemini":
        print("  Registration check: gemini mcp list ; in Gemini CLI: /mcp")
    elif agent == "cursor":
        print("  Registration check: cursor-agent mcp list ; cursor-agent mcp list-tools Roblox_Studio")
    elif agent in ("vscode", "copilot"):
        print("  VS Code: Chat > Open Customizations > MCP Servers > inspect status and call read-only tool.")


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", type=Path, default=Path.cwd(), help="Local game project directory")
    parser.add_argument("--agent", choices=("auto",) + SUPPORTED_AGENTS, default="auto")
    parser.add_argument("--interactive", action="store_true", help="Offer approved installation links and opt-in MCP setup")
    parser.add_argument("--json", action="store_true", help="Machine-readable, read-only environment inspection")
    args = parser.parse_args(argv)
    project = args.project.expanduser().resolve()
    status = report_environment()
    if args.json:
        print(json.dumps(status, indent=2))
        return 0
    print("Roblox Studio Architect — local environment & MCP readiness")
    print(f"Platform: {status['platform']} | Python: {status['python']}")
    print(f"Studio MCP launcher: {status['roblox_studio']['launcher'] or 'not detected'}")
    print(f"Blender executable: {status['blender']['executable'] or 'not detected'}")
    print(f"uvx: {status['uvx'] or 'not detected'}")
    print("Detected agent CLIs: " + (", ".join(k for k,v in status['agents'].items() if v) or "none"))
    _install_offers(status, args.interactive)
    agent = args.agent
    if agent == "auto":
        agents = [a for a in ("codex", "claude", "cursor", "gemini", "vscode") if status['agents'].get(a)]
        if args.interactive:
            print("Select your current agent: " + ", ".join(SUPPORTED_AGENTS))
            response = input("Agent [" + (agents[0] if agents else "other") + "]: ").strip().lower()
            agent = response or (agents[0] if agents else "other")
            if agent not in SUPPORTED_AGENTS:
                parser.error("Invalid agent selection")
        else:
            agent = agents[0] if agents else "other"
    print("Selected agent: " + agent)
    if args.interactive:
        _offer_addon(status, project, True)
    _offer_config(agent, status, project, args.interactive)
    _verification_guidance(agent)
    if args.interactive:
        print("Rerun this wizard after installing/restarting applications to verify updated detection.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
