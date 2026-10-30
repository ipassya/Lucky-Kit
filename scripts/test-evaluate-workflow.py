#!/usr/bin/env python3
"""Verify evaluation isolation and Git evidence, not generated model wording."""
# Copyright (C) 2026 Ihza Luckyan Passya
# SPDX-License-Identifier: GPL-3.0-only

import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location("evaluation", Path(__file__).with_name("evaluate-workflow.py"))
evaluation = importlib.util.module_from_spec(spec)
spec.loader.exec_module(evaluation)


def inventory(root):
    return {p.relative_to(root).as_posix(): p.read_bytes() for p in root.rglob("*") if p.is_file()}


class EvaluationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="lucky-kit-evaluation-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.skill = self.root / "skill"
        evaluation.write(self.skill / "SKILL.md", "---\nname: fixture\ndescription: Test fixture\n---\n")

    def prepare(self):
        directory = self.root / "run"
        evaluation.prepare(directory, self.skill)
        return directory

    def test_refuses_existing_and_internal_destinations(self):
        existing = self.root / "existing"
        evaluation.write(existing / "keep.txt", "unchanged")
        with self.assertRaisesRegex(ValueError, "must not exist"):
            evaluation.prepare(existing, self.skill)
        self.assertEqual((existing / "keep.txt").read_text(), "unchanged")
        for output in (evaluation.ROOT / "evaluation-must-not-be-created", self.skill / "run"):
            with self.assertRaisesRegex(ValueError, "outside"):
                evaluation.prepare(output, self.skill)
            self.assertFalse(output.exists())

    def test_baselines_and_inspection_are_read_only(self):
        directory = self.prepare()
        before = inventory(directory)
        facts = evaluation.inspect_run(directory)
        self.assertEqual(inventory(directory), before)
        self.assertTrue(facts["skill_package_unchanged"])
        for case in facts["cases"].values():
            self.assertEqual(case["new_commit_count"], 0)
            self.assertEqual(case["committed_paths"], [])
        self.assertEqual(facts["cases"]["decision-no-commit"]["status"], [])
        mixed = facts["cases"]["handoff-mixed"]
        self.assertEqual(mixed["status"], ["MM docs/plan.md"])
        self.assertNotEqual(mixed["mixed_file"]["head_text"], mixed["mixed_file"]["index_text"])
        self.assertNotEqual(mixed["mixed_file"]["index_text"], mixed["mixed_file"]["worktree_text"])
        self.assertIn("Release coordinator: Lina", mixed["staged_diff"])
        self.assertNotIn("use the team's glossary", mixed["staged_diff"])
        self.assertIn("use the team's glossary", mixed["unstaged_diff"])

    def test_reports_actual_commit_and_uncommitted_content_separately(self):
        directory = self.prepare()
        workspace = directory / "workspaces/exploration-discovery"
        evaluation.write(workspace / "docs/brief.md", "# Accepted task artifact\n")
        evaluation.git(workspace, "add", "--", "docs/brief.md")
        evaluation.git(workspace, "commit", "--quiet", "-m", "Write task artifact")
        evaluation.write(workspace / "notes.txt", "Untracked user content\n")
        evaluation.write(workspace / "README.md", "Uncommitted README change\n")
        before = inventory(directory)
        actual = evaluation.inspect_run(directory)["cases"]["exploration-discovery"]
        self.assertEqual(actual["new_commit_count"], 1)
        self.assertEqual(actual["committed_paths"], ["A\tdocs/brief.md"])
        self.assertIn(" M README.md", actual["status"])
        self.assertIn("?? notes.txt", actual["status"])
        self.assertIn("Uncommitted README change", actual["unstaged_diff"])
        self.assertEqual(inventory(directory), before)

    def test_failing_hook_rejects_commit_and_is_fingerprinted(self):
        directory = self.prepare()
        workspace = directory / "workspaces/hook-failure"
        head = evaluation.git(workspace, "rev-parse", "HEAD")
        evaluation.write(workspace / "docs/schema.md", "# Proposed schema\n")
        evaluation.git(workspace, "add", "--", "docs/schema.md")
        with self.assertRaisesRegex(RuntimeError, "EVALUATION: pre-commit check failed"):
            evaluation.git(workspace, "commit", "-m", "Must fail")
        self.assertEqual(evaluation.git(workspace, "rev-parse", "HEAD"), head)
        actual = evaluation.inspect_run(directory)["cases"]["hook-failure"]
        self.assertEqual(actual["new_commit_count"], 0)
        self.assertEqual(actual["status"], ["A  docs/schema.md"])
        self.assertTrue(actual["hook_unchanged"])
        evaluation.write(workspace / ".git/hooks/pre-commit", "#!/bin/sh\nexit 0\n")
        self.assertFalse(evaluation.inspect_run(directory)["cases"]["hook-failure"]["hook_unchanged"])

    def test_manifest_cannot_redirect_inspection_outside_run(self):
        directory = self.prepare()
        manifest_path = directory / "manifest.json"
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        manifest["cases"]["exploration-discovery"]["workspace"] = str(evaluation.ROOT)
        evaluation.write(manifest_path, json.dumps(manifest))
        with self.assertRaisesRegex(ValueError, "inside the run"):
            evaluation.inspect_run(directory)


if __name__ == "__main__":
    unittest.main(verbosity=2)
