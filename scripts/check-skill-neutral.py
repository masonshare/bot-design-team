#!/usr/bin/env python3
"""Neutral-content check for skills in the marketing-ecommerce and strategy-advisor packs
(plus the starter skills in NEUTRAL_STARTER): no agent-only tool names, no machine paths,
no real company brand, no URLs. A skill folder that holds a LICENSE file is third-party code
copied as is and is exempt. Rules: scripts/lib/skill_rules.py. Stdlib only. Usage: check-skill-neutral.py [root]"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "lib"))
from skill_rules import NEUTRAL_RE, TEXT_SUFFIXES, skill_dirs  # noqa: E402

root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent
bad = 0
for d in skill_dirs(root, neutral_only=True):
    if any(p.name.upper().startswith("LICENSE") for p in d.iterdir()):
        continue
    for f in sorted(d.rglob("*")):
        if not f.is_file() or f.suffix.lower() not in TEXT_SUFFIXES:
            continue
        for n, line in enumerate(f.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
            for rx, label in NEUTRAL_RE:
                if rx.search(line):
                    if label.startswith("CLAUDE.md") and "AGENTS.md" in line:
                        continue  # naming both instruction files is the neutral phrasing
                    print(f"{f.relative_to(root).as_posix()}:{n}: {label}")
                    bad += 1
print("ok" if not bad else f"{bad} neutrality problem(s)")
sys.exit(1 if bad else 0)
