#!/usr/bin/env python3
"""Check SKILL.md frontmatter (name + description present, name == directory name)
for skills/**/SKILL.md and every SKILL.md anywhere under packs/, and that pack skills sit at
packs/<pack>/skills/<name>/SKILL.md or packs/<pack>/<bot>/skills/<name>/SKILL.md. Missing packs/ is fine. Stdlib only.

The placement rules implement the pack layout contract in docs/adr/0005-pack-layout-contract.md;
change that ADR first, then this file, scripts/check-layout.sh and scripts/tests/run.sh together."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "lib"))
from cskh_common import split_frontmatter  # noqa: E402

root = Path(__file__).resolve().parent.parent
files = sorted(root.glob("skills/**/SKILL.md")) + sorted(root.glob("packs/**/SKILL.md"))
bad = 0


def fail(f, msg):
    global bad
    bad += 1
    print(f"{f.relative_to(root).as_posix()}: {msg}")


for f in files:
    rel = f.relative_to(root).parts
    if rel[0] == "packs" and not ((len(rel) == 5 and rel[2] == "skills") or (len(rel) == 6 and rel[3] == "skills")):
        fail(f, "pack skill must be packs/<pack>/skills/<name>/SKILL.md or packs/<pack>/<bot>/skills/<name>/SKILL.md")
    if rel[0] == "skills" and len(rel) != 4:
        fail(f, "skill must be skills/<bucket>/<name>/SKILL.md")
    try:
        fm, _ = split_frontmatter(f.read_text(encoding="utf-8"))
    except ValueError as e:
        fail(f, str(e))
        continue
    if not fm.get("name"):
        fail(f, "missing name")
    elif fm["name"] != f.parent.name:
        fail(f, f"name '{fm['name']}' != directory '{f.parent.name}'")
    if not fm.get("description"):
        fail(f, "missing description")
print("ok" if not bad else f"{bad} frontmatter problem(s)")
sys.exit(1 if bad else 0)
