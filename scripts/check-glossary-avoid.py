#!/usr/bin/env python3
"""Terms listed under '## Avoid' in GLOSSARY.md must not appear (case-insensitive)
in skills/, packs/, docs/ or the root *.md files.
Only .md files are scanned. Exempt: GLOSSARY.md itself, docs/adr/ (ADRs may
quote an avoided term as an example), and any line containing the token
`avoid-ok`. scripts/ is not scanned at all."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib"))
from cskh_common import avoid_terms  # noqa: E402

for _s in (sys.stdout, sys.stderr):
    _s.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXTS = (".md",)


def files():
    for name in sorted(os.listdir(ROOT)):
        if name.endswith(".md") and name != "GLOSSARY.md":
            yield os.path.join(ROOT, name)
    for top in ("skills", "packs", "docs"):
        for d, dirs, names in os.walk(os.path.join(ROOT, top)):
            rel = os.path.relpath(d, ROOT).replace(os.sep, "/")
            if rel == "docs/adr" or rel.startswith("docs/adr/"):
                dirs[:] = []
                continue
            for n in sorted(names):
                if n.endswith(EXTS):
                    yield os.path.join(d, n)


def main():
    gpath = os.path.join(ROOT, "GLOSSARY.md")
    terms = avoid_terms(open(gpath, encoding="utf-8").read()) if os.path.exists(gpath) else []
    if not terms:
        print("FAIL GLOSSARY.md has no '## Avoid' section with '- `term`' bullets")
        return 1
    bad = 0
    for f in files():
        for i, line in enumerate(open(f, encoding="utf-8", errors="replace"), 1):
            low = line.lower()
            if "avoid-ok" in low:
                continue
            for t in terms:
                if t.lower() in low:
                    print(f"FAIL {os.path.relpath(f, ROOT)}:{i}: avoided term `{t}` (see GLOSSARY.md Avoid)")
                    bad += 1
    if not bad:
        print(f"no avoided terms ({len(terms)} listed)")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
