#!/usr/bin/env python3
"""Check SKILL.md frontmatter (name + description present, name == directory name)
for skills/**/SKILL.md and packs/*/skills/**/SKILL.md, and that pack skills sit at
packs/<pack>/skills/<name>/SKILL.md. Missing packs/ is fine. Stdlib only."""
import re
import sys
from pathlib import Path

root = Path(__file__).resolve().parent.parent
files = sorted(root.glob("skills/**/SKILL.md")) + sorted(root.glob("packs/**/skills/**/SKILL.md"))
bad = 0


def fail(f, msg):
    global bad
    bad += 1
    print(f"{f.relative_to(root).as_posix()}: {msg}")


for f in files:
    rel = f.relative_to(root).parts
    if rel[0] == "packs" and not (len(rel) == 5 and rel[2] == "skills"):
        fail(f, "pack skill must be packs/<pack>/skills/<name>/SKILL.md")
    if rel[0] == "skills" and len(rel) != 4:
        fail(f, "skill must be skills/<bucket>/<name>/SKILL.md")
    lines = f.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        fail(f, "no frontmatter")
        continue
    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration:
        fail(f, "unterminated frontmatter")
        continue
    fm = {}
    for line in lines[1:end]:
        m = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if m:
            fm[m.group(1)] = m.group(2).strip().strip("\"'")
    if not fm.get("name"):
        fail(f, "missing name")
    elif fm["name"] != f.parent.name:
        fail(f, f"name '{fm['name']}' != directory '{f.parent.name}'")
    if not fm.get("description"):
        fail(f, "missing description")
print("ok" if not bad else f"{bad} frontmatter problem(s)")
sys.exit(1 if bad else 0)
