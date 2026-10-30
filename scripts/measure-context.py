#!/usr/bin/env python3
"""Measure normalized text; characters/4 is a heuristic, not actual token usage."""
# Copyright (C) 2026 Ihza Luckyan Passya
# SPDX-License-Identifier: GPL-3.0-only

import argparse
import json
from pathlib import Path
import math


def measure(root):
    skill = Path(root) / "skills" / "lucky-kit"
    groups = {
        "core": [skill / "SKILL.md"],
        "references": sorted((skill / "references").glob("*.md")),
        "templates": sorted((skill / "assets" / "templates").glob("*.md")),
    }
    result = {}
    for name, paths in groups.items():
        texts = [p.read_text(encoding="utf-8-sig") for p in paths]
        chars = sum(map(len, texts))
        result[name] = dict(files=len(paths), characters=chars,
                            words=sum(len(t.split()) for t in texts),
                            estimated_tokens_chars_div_4=math.ceil(chars / 4))
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path,
                        default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--before", type=Path)
    args = parser.parse_args()
    output = {"after": measure(args.root)}
    if args.before:
        output["before"] = measure(args.before)
    print(json.dumps(output, indent=2))
