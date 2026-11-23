#!/usr/bin/env python3
"""The column lists of the scripts sheet (`Kịch bản`, 9 columns) and the `Đề xuất`
file (8 columns) must be identical in sheet-template.md, the FAKE CSV headers
and the KB_COLUMNS / DX_COLUMNS constants of scripts/run-scenarios.py."""
import ast
import csv
import glob
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib"))
from cskh_common import template_columns  # noqa: E402

for _s in (sys.stdout, sys.stderr):
    _s.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def constants(path):
    tree = ast.parse(open(path, encoding="utf-8").read())
    found = {}
    for node in tree.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            if node.targets[0].id in ("KB_COLUMNS", "DX_COLUMNS"):
                found[node.targets[0].id] = list(ast.literal_eval(node.value))
    return found


def main():
    errors = []
    packs = sorted(glob.glob(os.path.join(ROOT, "packs", "*", "sheet-template.md")))
    consts = constants(os.path.join(ROOT, "scripts", "run-scenarios.py"))
    for name in ("KB_COLUMNS", "DX_COLUMNS"):
        if name not in consts:
            errors.append(f"scripts/run-scenarios.py: constant {name} missing")
    for tpl in packs:
        pack = os.path.dirname(tpl)
        rel = os.path.relpath(pack, ROOT)
        try:
            kb, dx = template_columns(open(tpl, encoding="utf-8").read())
        except ValueError as e:
            errors.append(f"{rel}/sheet-template.md: {e}")
            continue
        if len(kb) != 9 or len(dx) != 8:
            errors.append(f"{rel}/sheet-template.md: expected 9 and 8 columns, found {len(kb)} and {len(dx)}")
        sources = [("scripts/run-scenarios.py KB_COLUMNS", consts.get("KB_COLUMNS"), kb),
                   ("scripts/run-scenarios.py DX_COLUMNS", consts.get("DX_COLUMNS"), dx)]
        for kind, want in (("kich-ban", kb), ("de-xuat", dx)):
            for f in sorted(glob.glob(os.path.join(pack, "fake-data", f"FAKE-{kind}-*.csv"))):
                with open(f, encoding="utf-8-sig", newline="") as fh:
                    sources.append((os.path.relpath(f, ROOT), next(csv.reader(fh), []), want))
        for label, got, want in sources:
            if got is not None and got != want:
                errors.append(f"{label}: {got} != sheet-template.md {want}")
    if not packs:
        errors.append("no packs/*/sheet-template.md found")
    for e in errors:
        print("FAIL", e)
    if not errors:
        print("columns agree")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
