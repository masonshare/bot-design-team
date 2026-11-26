#!/usr/bin/env python3
"""Cross-check the marketing-ecommerce orchestrator against the pack folder.

Every skill name the orchestrator lists (SKILL.md section "Skills in this pack" and the first
column of the tables in references/ecosystem-map.md) must be a folder in
packs/marketing-ecommerce/skills/, and every folder must be listed.

scripts/orchestrator-pending.txt holds names that are listed but not merged yet (one per line,
`name  # reason`). A pending name is allowed to have no folder; a pending name that does have a
folder is stale and fails, so the file shrinks as skills land. Names of other packs may appear
elsewhere in the orchestrator as soft suggestions; only the two lists above are checked.
Stdlib only. Usage: check-orchestrator-skills.py [root]"""
import re
import sys
from pathlib import Path

root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent
pack = root / "packs" / "marketing-ecommerce" / "skills"
orch = pack / "orchestrator"
NAME = r"[a-z][a-z0-9]*(?:-[a-z0-9]+)*"
bad = 0


def fail(msg):
    global bad
    bad += 1
    print(msg)


if not (orch / "SKILL.md").is_file():
    print("no orchestrator in packs/marketing-ecommerce: nothing to check")
    sys.exit(0)

dirs = {d.name for d in pack.iterdir() if d.is_dir() and (d / "SKILL.md").is_file()}

pending = {}
pf = root / "scripts" / "orchestrator-pending.txt"
if pf.is_file():
    for line in pf.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            pending[line.split("#")[0].strip()] = line

# SKILL.md: names in backticks inside the "Skills in this pack" section
text = (orch / "SKILL.md").read_text(encoding="utf-8")
m = re.search(r"^## Skills in this pack\s*$(.*?)(?=^## )", text, re.S | re.M)
if not m:
    fail("orchestrator/SKILL.md has no '## Skills in this pack' section")
    listed_md = set()
else:
    listed_md = set(re.findall(r"`(%s)`" % NAME, m.group(1)))

# ecosystem-map.md: first column of table rows
listed_map = set()
mp = orch / "references" / "ecosystem-map.md"
if mp.is_file():
    for line in mp.read_text(encoding="utf-8").splitlines():
        mm = re.match(r"^\|\s*`(%s)`\s*\|" % NAME, line)
        if mm:
            listed_map.add(mm.group(1))
else:
    fail("orchestrator/references/ecosystem-map.md is missing")

expected = dirs | set(pending)
for name in sorted(listed_md - expected):
    fail(f"orchestrator/SKILL.md lists `{name}` but packs/marketing-ecommerce/skills/{name}/ does not exist and it is not in scripts/orchestrator-pending.txt")
for name in sorted(expected - listed_md):
    fail(f"packs/marketing-ecommerce/skills/{name}/ exists but orchestrator/SKILL.md does not list it")
want_map = expected - {"orchestrator"}
for name in sorted(listed_map - want_map):
    fail(f"orchestrator/references/ecosystem-map.md lists `{name}` which is neither a skill folder nor pending")
for name in sorted(want_map - listed_map):
    fail(f"orchestrator/references/ecosystem-map.md does not list `{name}`")
for name in sorted(set(pending) & dirs):
    fail(f"scripts/orchestrator-pending.txt still lists `{name}` but its folder exists now: delete the line")
print("ok" if not bad else f"{bad} orchestrator cross-check problem(s)")
sys.exit(1 if bad else 0)
