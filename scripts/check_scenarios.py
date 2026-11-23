"""Validate scenario files: packs/*/scenarios/*.md (stdlib only)."""
import glob
import os
import re
import sys

fail = 0
files = [f for f in glob.glob("packs/*/scenarios/*.md") if os.path.basename(f) != "README.md"]
if not files:
    print("no scenario files")
    sys.exit(1)
for f in sorted(files):
    errs = []
    text = open(f, encoding="utf-8").read()
    m = re.match(r"---\r?\n(.*?)\r?\n---\r?\n(.*)", text, re.S)
    if not m:
        print(f"{f}: missing front matter")
        fail = 1
        continue
    meta = {}
    for line in m.group(1).splitlines():
        k, _, v = line.partition(":")
        meta[k.strip()] = v.strip()
    if set(meta) != {"id", "bot", "data", "channel"}:
        errs.append(f"front matter keys {sorted(meta)}")
    if meta.get("id") != os.path.basename(f)[:-3]:
        errs.append("id does not match file name")
    if meta.get("bot") not in ("staff", "editor"):
        errs.append("bot must be staff|editor")
    if meta.get("channel") not in ("Shopee", "Zalo", "hotline", "none"):
        errs.append("bad channel")
    d = os.path.join(os.path.dirname(os.path.dirname(f)), "fake-data", meta.get("data", ""))
    if not os.path.isfile(d):
        errs.append(f"data file not found: {meta.get('data')}")
    body = m.group(2)
    heads = re.findall(r"^## .*$", body, re.M)
    if heads != ["## Message", "## Expect", "## Must not"]:
        errs.append(f"sections {heads}")
    else:
        parts = re.split(r"^## .*$", body, flags=re.M)[1:]
        for h, part in zip(heads, parts):
            if not part.strip():
                errs.append(f"{h} empty")
            if h != "## Message" and not re.search(r"^- ", part, re.M):
                errs.append(f"{h} has no bullets")
    for e in errs:
        print(f"{f}: {e}")
        fail = 1
if not fail:
    print(f"ok ({len(files)} scenarios)")
sys.exit(fail)
