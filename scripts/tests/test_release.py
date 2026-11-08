"""Verify public archive scope and reproduction without network access."""
from __future__ import annotations

import importlib.util
from pathlib import Path
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[2]

spec = importlib.util.spec_from_file_location("autoblox_build_release", ROOT / "scripts/build_release.py")
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)


class ReleaseTests(unittest.TestCase):
    def test_archives_have_required_entries_and_no_private_configs(self):
        with tempfile.TemporaryDirectory() as d:
            items = module.build_release(Path(d))
            self.assertEqual(2, len(items))
            for name in items:
                with zipfile.ZipFile(Path(d) / name) as z:
                    self.assertIsNone(z.testzip())
                    paths = z.namelist()
                    self.assertFalse(any("__pycache__" in p or "/dist/" in p for p in paths))
                    self.assertFalse(any(p.endswith(("/.mcp.json", "/.env", "/.cursor/mcp.json")) for p in paths))
                    if "full-toolkit" in name:
                        self.assertTrue(any(p.endswith("README.md") for p in paths))
                        self.assertTrue(any(p.endswith("scripts/publish_github.py") for p in paths))
                    else:
                        self.assertTrue(any(p.endswith("/SKILL.md") for p in paths))
            checksums = (Path(d) / "SHA256SUMS").read_text().splitlines()
            self.assertEqual(2, len(checksums))

    def test_archives_are_deterministic(self):
        with tempfile.TemporaryDirectory() as d1, tempfile.TemporaryDirectory() as d2:
            r1 = module.build_release(Path(d1))
            r2 = module.build_release(Path(d2))
            self.assertEqual({k: v["sha256"] for k, v in r1.items()},
                             {k: v["sha256"] for k, v in r2.items()})

    def test_skips_private_config_and_symlink(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)
            (p / "SKILL.md").write_text("hello")
            (p / ".mcp.json").write_text("sensitive")
            (p / ".env").write_text("sensitive")
            (p / ".cursor").mkdir()
            (p / ".cursor/mcp.json").write_text("sensitive")
            with tempfile.TemporaryDirectory() as out:
                archive = Path(out) / "safe.zip"
                self.assertEqual(1, module.zip_folder(p, archive, "test"))
                with zipfile.ZipFile(archive) as z:
                    self.assertEqual(["test/SKILL.md"], z.namelist())
            link = p / "reference"
            try:
                link.symlink_to(p / "SKILL.md")
            except (NotImplementedError, OSError):
                return
            with self.assertRaises(ValueError):
                module.zip_folder(p, p / "bad.zip", "test")


if __name__ == "__main__":
    unittest.main()
