"""Offline tests of opt-in, cross-agent app/MCP setup — zero installed software required."""
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

BASE = Path(__file__).resolve().parents[2]
MODULE = BASE / '.agents/skills/roblox-studio-architect/scripts/environment_setup.py'
SPEC = importlib.util.spec_from_file_location('environment_setup', MODULE)
setup = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(setup)


class BootstrapTests(unittest.TestCase):
    def test_offline_inspect_no_changes(self):
        with tempfile.TemporaryDirectory() as d:
            temp = Path(d)
            home = temp / 'home'; home.mkdir()
            # Isolate platform probes: the host may already have Studio/Blender installed.
            with patch.object(setup, 'detect_studio', return_value={
                'supported': True, 'installed': False, 'launcher': None, 'mcp_launcher_present': False,
            }), patch.object(setup, 'detect_blender', return_value={
                'installed': False, 'executable': None,
            }):
                result = setup.report_environment(system='Darwin', home=home, env={}, which=lambda _: None)
            self.assertFalse(result['roblox_studio']['installed'])
            self.assertFalse(result['blender']['installed'])
            self.assertFalse(result['mcp_live_verified'])
            self.assertEqual(list(temp.glob('**/*')), [home])

    def test_mac_detects_official_studio_launcher(self):
        with tempfile.TemporaryDirectory() as d:
            home = Path(d)
            executable = home / 'Applications/RobloxStudio.app/Contents/MacOS/StudioMCP'
            executable.parent.mkdir(parents=True)
            executable.write_text('test binary placeholder')
            # Use only the temporary launcher; never select the host's real /Applications copy.
            with patch.object(setup, '_mac_studio_candidates', return_value=[executable]):
                state = setup.detect_studio('Darwin', home, {})
            self.assertTrue(state['installed'])
            self.assertEqual(state['launcher'], str(executable))

    def test_windows_detects_studio_bat(self):
        with tempfile.TemporaryDirectory() as d:
            home = Path(d)
            launcher = home / 'Roblox/mcp.bat'; launcher.parent.mkdir()
            launcher.write_text('test bat')
            state = setup.detect_studio('Windows', home, {'LOCALAPPDATA': str(home)})
            self.assertTrue(state['installed'])
            self.assertEqual(state['launcher'], str(launcher))

    def test_linux_studio_unsupported(self):
        self.assertFalse(setup.detect_studio('Linux', Path('/tmp'), {})['supported'])

    def test_generates_proper_mcp_servers(self):
        report = {'platform': 'Darwin', 'roblox_studio': {'launcher':'/Applications/RobloxStudio.app/Contents/MacOS/StudioMCP'},
                  'blender': {'installed':True}, 'uvx':'/opt/homebrew/bin/uvx'}
        servers = setup.stdio_servers(report)
        self.assertEqual(servers['Roblox_Studio']['command'], report['roblox_studio']['launcher'])
        self.assertEqual(servers['blender']['env']['BLENDER_MCP_SAFE_MODE'], '1')
        self.assertIn('mcp-for-blender', servers['blender']['args'])

    def test_claude_merges_preserving_other_servers(self):
        with tempfile.TemporaryDirectory() as d:
            project = Path(d)
            file = project / '.mcp.json'
            file.write_text(json.dumps({'mcpServers':{'other':{'command':'existing'}}}))
            servers = {'Roblox_Studio':{'command':'/Applications/RobloxStudio.app/Contents/MacOS/StudioMCP','args':[]}}
            plan = setup.prepare_config('claude',project,servers)
            self.assertEqual(plan['added'], ['Roblox_Studio'])
            self.assertIn('other', plan['data']['mcpServers'])
            self.assertNotIn('Roblox_Studio', json.loads(file.read_text())['mcpServers'])
            backup = setup.save_config(plan)
            self.assertTrue(backup.exists())
            self.assertIn('other',json.loads(file.read_text())['mcpServers'])
            self.assertIn('Roblox_Studio',json.loads(file.read_text())['mcpServers'])

    def test_refuse_conflicting_mcp_key_without_write(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d); f=p/'.mcp.json'
            original = '{"mcpServers":{"blender":{"command":"custom"}}}'
            f.write_text(original)
            with self.assertRaises(ValueError):
                setup.prepare_config('copilot',p,{'blender':{'command':'uvx','args':['mcp-for-blender']}})
            self.assertEqual(f.read_text(),original)

    def test_vscode_local_harness_uses_servers_key(self):
        with tempfile.TemporaryDirectory() as d:
            data=setup.prepare_config('vscode',Path(d),{'Roblox_Studio':{'command':'stub','args':[]}})['data']
            self.assertEqual(data['servers']['Roblox_Studio']['type'], 'stdio')
            self.assertNotIn('mcpServers',data)

    def test_cursor_gemini_paths(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)
            self.assertEqual(setup.config_target('cursor',root)[0],root/'.cursor/mcp.json')
            self.assertEqual(setup.config_target('gemini',root)[0],root/'.gemini/settings.json')
            self.assertIsNone(setup.config_target('other',root)[0])

    def test_codex_command_uses_absolute_uvx(self):
        cmd = setup.codex_command('blender',{'command':'/opt/homebrew/bin/uvx','args':['mcp-for-blender'],'env':{'BLENDER_MCP_SAFE_MODE':'1'}})
        self.assertEqual(cmd[:4],['codex','mcp','add','blender'])
        self.assertIn('--env',cmd)
        self.assertEqual(cmd[-2:],['/opt/homebrew/bin/uvx','mcp-for-blender'])

    def test_json_mode_does_not_ask_install_or_configure(self):
        with patch.object(setup, 'report_environment', return_value={'platform':'Linux','mcp_live_verified':False}):
            with patch('builtins.input', side_effect=AssertionError('input must not run')):
                with patch.object(setup, '_install_offers', side_effect=AssertionError('install offer must not run')):
                    self.assertEqual(setup.main(['--json']),0)


if __name__ == '__main__':
    unittest.main()

# Keep setup registration checks read-only; avoid creating duplicate servers.
class CliRegistrationTests(unittest.TestCase):
    def test_codex_registered_parse(self):
        with tempfile.TemporaryDirectory() as d:
            class Result:
                returncode = 0
                stdout = 'Name Command Args\nRoblox_Studio /Applications/RobloxStudio.app/Contents/MacOS/StudioMCP -\nblender uvx mcp-for-blender\n'
            with patch.object(setup.shutil, 'which', return_value='/fake/codex'):
                with patch.object(setup.subprocess, 'run', return_value=Result()) as run:
                    names = setup._mcp_registered_cli('codex', Path(d))
            self.assertIn('Roblox_Studio', names)
            self.assertIn('blender', names)
            run.assert_called_once()

class BootstrapSafetyTests(unittest.TestCase):
    def test_dry_run_makes_no_files_or_installs(self):
        with tempfile.TemporaryDirectory() as d:
            project=Path(d)
            fixture = {'platform':'Darwin','python':'3.11','roblox_studio':{'supported':True,'installed':False,'launcher':None,'mcp_launcher_present':False},
                       'blender':{'installed':False,'executable':None},'uvx':None,
                       'agents':{'codex':False,'claude':False,'cursor':False,'gemini':False,'vscode':False,'copilot':False},'mcp_live_verified':False}
            with patch.object(setup,'report_environment',return_value=fixture):
                with patch.object(setup.webbrowser,'open',side_effect=AssertionError('Do not open downloads in inspection')):
                    with patch.object(setup.subprocess,'run',side_effect=AssertionError('Do not install in inspection')):
                        self.assertEqual(setup.main(['--project',str(project),'--agent','other']),0)
            self.assertEqual(list(project.rglob('*')),[])

    def test_symlink_config_refused(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)
            target=root/'elsewhere.json';target.write_text('{"mcpServers":{}}')
            (root/'.mcp.json').symlink_to(target)
            with self.assertRaises(ValueError):
                setup.prepare_config('claude',root,{'Roblox_Studio':{'command':'x','args':[]}})
            self.assertEqual(target.read_text(),'{"mcpServers":{}}')
