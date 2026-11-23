#!/usr/bin/env python3
"""Staff and editor SOUL.md point at their skills for rules; they must not carry
a copy of the sheet's columns or status vocabulary.
Rules, per SOUL.md of every pack (packs/*/staff, packs/*/editor), line by line:
  1. No single line contains 3 or more distinct column headers (exact, case
     sensitive) of the scripts sheet or the `Đề xuất` file.
  2. No line lists all three statuses `Nháp`, `Đã duyệt`, `Hết hạn` together,
     that is as an adjacent run separated only by punctuation, quotes or
     "hoặc"/"và" (a vocabulary definition). A sentence that merely mentions
     all three inside a rule is fine.
  3. The SOUL names at least one skill of its own folder's skills/ directory.
Single mentions (a rule that says what to do with `Nháp`) are fine."""
import glob
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib"))
from cskh_common import template_columns  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_S = "(?:Nháp|Đã duyệt|Hết hạn)"
STATUS_RUN = re.compile(_S + r"(?:[\W_]{0,4}(?:hoặc|và|or)?[\W_]{0,4}" + _S + ")+")
for _s in (sys.stdout, sys.stderr):
    _s.reconfigure(encoding="utf-8")


def main():
    errors = []
    for tpl in sorted(glob.glob(os.path.join(ROOT, "packs", "*", "sheet-template.md"))):
        pack = os.path.dirname(tpl)
        kb, dx = template_columns(open(tpl, encoding="utf-8").read())
        headers = sorted(set(kb + dx), key=len, reverse=True)
        for soul in sorted(glob.glob(os.path.join(pack, "*", "SOUL.md"))):
            rel = os.path.relpath(soul, ROOT)
            text = open(soul, encoding="utf-8").read()
            for i, line in enumerate(text.splitlines(), 1):
                hit = [h for h in headers if re.search(r"(?<!\w)" + re.escape(h) + r"(?!\w)", line)]
                if len(hit) >= 3:
                    errors.append(f"{rel}:{i}: restates a column list ({', '.join(hit)}); point at the skill instead")
                if any(len(set(re.findall(_S, m.group(0)))) >= 3 for m in STATUS_RUN.finditer(line)):
                    errors.append(f"{rel}:{i}: defines the status vocabulary; point at the skill instead")
            names = [os.path.basename(d) for d in glob.glob(os.path.join(os.path.dirname(soul), "skills", "*"))]
            if not any(n in text for n in names):
                errors.append(f"{rel}: names none of its skills ({', '.join(sorted(names)) or 'no skills/ folder'})")
    for e in errors:
        print("FAIL", e)
    if not errors:
        print("SOUL files point at skills, no own column list or status vocabulary")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
