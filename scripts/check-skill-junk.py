#!/usr/bin/env python3
"""Fail if a file or folder that must not be public sits anywhere under packs/ (version
folders, working notes, backups, progress logs, SPEC.md, transcripts, .git ...).
The list lives in scripts/lib/skill_rules.py. Stdlib only. Usage: check-skill-junk.py [root]"""
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "lib"))
from skill_rules import is_junk_name  # noqa: E402

root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent
bad = 0
for d, dirs, files in os.walk(root / "packs"):
    for name in list(dirs):
        if is_junk_name(name, True):
            print(f"{(Path(d) / name).relative_to(root).as_posix()}/: junk folder, delete it")
            bad += 1
            dirs.remove(name)
    for name in files:
        if is_junk_name(name, False):
            print(f"{(Path(d) / name).relative_to(root).as_posix()}: junk file, delete it (SPEC.md content goes to docs/skills/<name>.md)")
            bad += 1
print("ok" if not bad else f"{bad} junk path(s)")
sys.exit(1 if bad else 0)
