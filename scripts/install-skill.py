#!/usr/bin/env python3
"""Install the complete skill into an explicit host directory; no dependencies."""
# Copyright (C) 2026 Ihza Luckyan Passya
# SPDX-License-Identifier: GPL-3.0-only

import argparse
from pathlib import Path
import shutil
import sys

SOURCE = Path(__file__).resolve().parent.parent / "skills" / "lucky-kit"


def reject_links(path):
    for part in (path, *path.parents):
        if part.is_symlink() or getattr(part, "is_junction", lambda: False)():
            raise ValueError(f"Linked paths are not supported: {part}")


def install(skills_root, update=False, source=SOURCE):
    source = source.absolute()
    destination = Path(skills_root).expanduser().absolute() / "lucky-kit"
    reject_links(source)
    reject_links(destination)
    source, destination = source.resolve(), destination.resolve()
    if (source == destination or source in destination.parents
            or destination in source.parents):
        raise ValueError("Source and destination must not overlap.")
    if not (source / "SKILL.md").is_file():
        raise ValueError(f"Skill source not found: {source}")

    pending, conflicts = [], []
    for item in sorted(source.rglob("*")):
        reject_links(item)
        if not item.is_file():
            continue
        target = destination / item.relative_to(source)
        reject_links(target)
        for parent in target.parents:
            if parent.exists() and not parent.is_dir():
                raise ValueError(f"Destination parent is not a directory: {parent}")
        if target.exists():
            if not target.is_file():
                raise ValueError(f"Destination is not a file: {target}")
            if item.read_bytes() == target.read_bytes():
                continue
            conflicts.append(str(item.relative_to(source)))
        pending.append((item, target))
    if conflicts and not update:
        raise ValueError("Installed files differ; review and use --update: "
                         + ", ".join(conflicts))
    # All predictable collisions are checked before any write.
    for item, target in pending:
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(item, target)
    return destination, len(pending)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skills-root", required=True,
                        help="Host skills directory; lucky-kit is appended.")
    parser.add_argument("--update", action="store_true",
                        help="Overwrite differing package files; retain extras.")
    args = parser.parse_args()
    try:
        destination, count = install(args.skills_root, args.update)
    except (ValueError, OSError) as error:
        parser.exit(1, f"Install failed: {error}\n")
    print(f"Installed Lucky Kit ({count} files): {destination}" if count
          else f"Already up to date: Lucky Kit at {destination}")
    print("Extra files are retained. Use your host's skill invocation or plain chat.")


if __name__ == "__main__":
    main()
