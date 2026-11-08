"""Offline tests of the scaffolder and truthful release gates."""
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

BASE = Path(__file__).resolve().parents[2]


def get_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


class ScaffoldTests(unittest.TestCase):
    def setUp(self):
        self.new = get_module(BASE/'scripts/new_game.py','new_game')

    def test_new_game_structural_pass_but_not_release(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'Test Game'
            self.new.make_game('Test Game',p,'Obby')
            v=get_module(p/'scripts/verify_game.py','verify_game')
            self.assertEqual(v.inspect(p),[])
            self.assertTrue(v.inspect(p,release_candidate=True))
            self.assertEqual(json.loads((p/'docs/VERIFICATION.json').read_text())['status'],'NOT_READY')

    def test_refuse_overwrite(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'Existing'
            p.mkdir()
            (p/'safety.txt').write_text('keep')
            with self.assertRaises(FileExistsError):
                self.new.make_game('Another',p)
            self.assertEqual((p/'safety.txt').read_text(),'keep')

    def test_reject_bad_name(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(ValueError):
                self.new.make_game('{{BUSTED}}',Path(d)/'Game')

    def test_readable_skill_metadata_and_modules(self):
        skill=BASE/'.agents/skills/roblox-studio-architect'
        data=json.loads((skill/'references/coverage.json').read_text())
        self.assertEqual(len(data),41)
        self.assertEqual(len({x['slug'] for x in data}),41)
        for item in data:
            self.assertTrue((skill/'references/practices'/f"{item['slug']}.md").is_file())


if __name__=='__main__':
    unittest.main()
