#!/usr/bin/env python3
"""Exercise installer outcomes in temporary directories, not live installs."""
# Copyright (C) 2026 Ihza Luckyan Passya
# SPDX-License-Identifier: GPL-3.0-only

import importlib.util
from pathlib import Path
import tempfile
import unittest
import sys

sys.dont_write_bytecode = True

spec = importlib.util.spec_from_file_location(
    "installer", Path(__file__).with_name("install-skill.py"))
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


def inventory(root):
    return {p.relative_to(root).as_posix(): p.read_bytes()
            for p in root.rglob("*") if p.is_file()}


class InstallTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="lucky-kit-install-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def test_install_repeat_and_legal_files(self):
        target, count = installer.install(self.root / "spaces and unicode é")
        self.assertGreater(count, 0)
        self.assertEqual(inventory(installer.SOURCE), inventory(target))
        self.assertTrue((target / "LICENSE.txt").is_file())
        self.assertTrue((target / "OUTPUT-LICENSE.md").is_file())
        self.assertEqual(installer.install(target.parent)[1], 0)

    def test_conflict_preflight_update_and_extras(self):
        target, _ = installer.install(self.root)
        (target / "SKILL.md").write_text("Local customization")
        (target / "NOTICE.md").unlink()
        (target / "local-note.txt").write_text("Keep")
        before = inventory(target)
        with self.assertRaisesRegex(ValueError, "Installed files differ"):
            installer.install(self.root)
        self.assertEqual(before, inventory(target))
        installer.install(self.root, update=True)
        for path, data in inventory(installer.SOURCE).items():
            self.assertEqual((target / path).read_bytes(), data)
        self.assertEqual((target / "local-note.txt").read_text(), "Keep")

    def test_overlap(self):
        with self.assertRaisesRegex(ValueError, "overlap"):
            installer.install(installer.SOURCE.parent, update=True)
        with self.assertRaisesRegex(ValueError, "overlap"):
            installer.install(installer.SOURCE / "nested", update=True)
        self.assertFalse((installer.SOURCE / "nested").exists())
        source = self.root / "lucky-kit" / "nested"
        source.mkdir(parents=True)
        (source / "SKILL.md").write_text("source")
        with self.assertRaisesRegex(ValueError, "overlap"):
            installer.install(self.root, source=source)

    def test_file_directory_collisions(self):
        for name, blocking_file in (("parent", True), ("leaf", False)):
            root = self.root / name
            target = root / "lucky-kit"
            target.mkdir(parents=True)
            if blocking_file:
                (target / "assets").write_text("not a directory")
            else:
                (target / "SKILL.md").mkdir()
            before = inventory(target)
            with self.assertRaises(ValueError):
                installer.install(root, update=True)
            self.assertEqual(before, inventory(target))

    def test_link_rejected(self):
        actual = self.root / "actual"
        actual.mkdir()
        link = self.root / "linked"
        try:
            link.symlink_to(actual, target_is_directory=True)
        except OSError:
            self.skipTest("Symlink creation unavailable on this host")
        with self.assertRaisesRegex(ValueError, "Linked paths"):
            installer.install(link)
        self.assertEqual(list(actual.iterdir()), [])


if __name__ == "__main__":
    unittest.main()
