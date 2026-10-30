#!/usr/bin/env python3
"""Check Lucky Kit package integrity using only the Python standard library."""
# Copyright (C) 2026 Ihza Luckyan Passya
# SPDX-License-Identifier: GPL-3.0-only

from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "skills" / "lucky-kit"
EXCLUDED = {".git", ".venv", "__pycache__"}


def heading_ids(text):
    identifiers = set()
    occurrences = {}
    for heading in re.findall(r"^#{1,6}\s+(.+?)\s*#*\s*$", text, re.MULTILINE):
        base = re.sub(r"[^\w\- ]", "", heading.lower()).replace(" ", "-")
        count = occurrences.get(base, 0)
        identifiers.add(f"{base}-{count}" if count else base)
        occurrences[base] = count + 1
    return identifiers


def prose(text):
    return re.sub(r"^(```|~~~)[^\n]*\n.*?^\1[^\n]*$", "", text,
                  flags=re.MULTILINE | re.DOTALL)


def validate_openai_metadata(path):
    errors = []
    interface = path.read_text(encoding="utf-8-sig")
    for field, value in [("display_name", "Lucky Kit"), ("default_prompt", "$lucky-kit")]:
        match = re.search(rf'^\s*{field}:\s*"([^"\n]+)"\s*$', interface, re.MULTILINE)
        if not match or (match.group(1) != value if field == "display_name" else value not in match.group(1)):
            errors.append(f"UI {field} does not match the skill identity.")
    summary = re.search(r'^\s*short_description:\s*"([^"\n]+)"\s*$', interface, re.MULTILINE)
    if not summary or not 25 <= len(summary.group(1)) <= 64:
        errors.append("UI short_description must contain 25–64 characters.")
    return errors


def validate(root=ROOT):
    skill = root / "skills" / "lucky-kit"
    errors = []
    required = [root / "LICENSE", skill / "SKILL.md", skill / "LICENSE.txt",
                skill / "NOTICE.md", skill / "OUTPUT-LICENSE.md"]
    for path in required:
        if not path.is_file():
            errors.append(f"Missing file: {path.relative_to(root)}")
    if errors:
        return errors, 0

    entry = (skill / "SKILL.md").read_text(encoding="utf-8-sig")
    frontmatter = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", entry, re.DOTALL)
    if not frontmatter:
        errors.append("SKILL.md must start with YAML frontmatter.")
    else:
        fields = frontmatter.group(1)
        if not re.search(r"^name:\s*lucky-kit\s*$", fields, re.MULTILINE):
            errors.append("Skill name must match its lucky-kit directory.")
        if not re.search(r"^description:\s*\S.+$", fields, re.MULTILINE):
            errors.append("Skill description is missing.")
        if not re.search(r"^license:\s*GPL-3\.0-only[^\n]*OUTPUT-LICENSE\.md", fields, re.MULTILINE):
            errors.append("Declare GPLv3-only and the generated-output permission.")

    interface_path = skill / "agents" / "openai.yaml"
    if interface_path.exists():
        errors.extend(validate_openai_metadata(interface_path))

    license_bytes = (root / "LICENSE").read_bytes()
    if license_bytes != (skill / "LICENSE.txt").read_bytes():
        errors.append("Packaged LICENSE.txt must match the root LICENSE byte for byte.")
    if b"GNU GENERAL PUBLIC LICENSE" not in license_bytes or b"Version 3, 29 June 2007" not in license_bytes:
        errors.append("Expected the GPLv3 license text.")

    checked = 0
    for path in sorted(root.rglob("*.md")):
        relative = path.relative_to(root)
        if any(part in EXCLUDED for part in relative.parts):
            continue
        # Templates describe paths in future generated projects, not this package.
        if path.is_relative_to(skill / "assets" / "templates"):
            continue
        content = prose(path.read_text(encoding="utf-8-sig"))
        for target in re.findall(r"\[[^\]\n]*\]\(([^)\n]+)\)", content):
            target = target.strip().strip("<>")
            if re.match(r"^[A-Za-z]:[\\/]", target):
                errors.append(f"Machine-specific path in {relative}: {target}")
                continue
            url = urlsplit(target)
            if url.scheme or url.netloc:
                continue
            destination = (path.parent / unquote(url.path)).resolve() if url.path else path
            if not destination.is_relative_to(root):
                errors.append(f"Link escapes repository in {relative}: {target}")
                continue
            if path.is_relative_to(skill) and not destination.is_relative_to(skill):
                errors.append(f"Installed skill depends on repository file in {relative}: {target}")
                continue
            checked += 1
            if not destination.exists():
                errors.append(f"Broken link in {relative}: {target}")
            elif url.fragment and destination.suffix.lower() == ".md":
                headings = heading_ids(prose(destination.read_text(encoding="utf-8-sig")))
                if unquote(url.fragment) not in headings:
                    errors.append(f"Missing heading in {relative}: {target}")
    return errors, checked


if __name__ == "__main__":
    problems, links = validate()
    if problems:
        for problem in problems:
            print(f"FAIL: {problem}", file=sys.stderr)
        sys.exit(1)
    print(f"PASS: skill identity, licensing, and {links} local Markdown links.")
    print("Not checked: full YAML schema, remote links, agent behavior, or output quality.")
