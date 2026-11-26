#!/usr/bin/env python3
"""Validate an Agent Skills skill folder.

Usage: python validate_skill.py <skill-folder>
Prints PASS/FAIL per check. Exits 0 when all pass, 1 on any failure, 2 on usage error.
Standard library only.
"""
import re
import sys
from pathlib import Path

NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
LINK_RE = re.compile(r"(?<!\!)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
ABS_PATH_RES = [
    re.compile(r"(?<![A-Za-z0-9])[A-Za-z]:\\"),
    re.compile(r"(?<![A-Za-z0-9])[A-Za-z]:/(?!/)"),
    re.compile(r"/Users/"),
    re.compile(r"/home/"),
]


def parse_frontmatter(text):
    """Return (fields, raw_lines) or None. Top-level `key: value` pairs only."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        return None
    fields = {}
    body = lines[1:end]
    for idx, line in enumerate(body):
        m = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if not m:
            continue
        key, val = m.group(1), m.group(2).rstrip()
        nxt = body[idx + 1] if idx + 1 < len(body) else ""
        continued = bool(nxt) and nxt[0] in " \t" and key != "metadata"
        if len(val) >= 2 and val[0] == val[-1] and val[0] in "\"'":
            val = val[1:-1]
        fields[key] = (val, continued)
    return fields


def main(argv):
    if len(argv) != 2 or argv[1] in ("-h", "--help"):
        print(__doc__)
        return 2
    folder = Path(argv[1]).resolve()
    results = []

    def check(label, ok, detail=""):
        results.append(ok)
        print(("PASS" if ok else "FAIL") + "  " + label + (" - " + detail if detail and not ok else ""))

    skill_md = folder / "SKILL.md"
    if not skill_md.is_file():
        check("SKILL.md exists", False, "not found in " + folder.name)
        return 1
    check("SKILL.md exists", True)
    text = skill_md.read_text(encoding="utf-8")
    fields = parse_frontmatter(text)
    check("frontmatter present", fields is not None, "file must start with --- and close with ---")
    fields = fields or {}

    name = fields.get("name", ("", False))[0]
    ok_name = 1 <= len(name) <= 64 and bool(NAME_RE.match(name))
    check("name valid (1-64, a-z0-9, single hyphens, no edge hyphen)", ok_name,
          "got %r" % name)
    check("name equals folder name", name == folder.name, "name %r, folder %r" % (name, folder.name))

    desc, desc_continued = fields.get("description", ("", False))
    check("description non-empty", bool(desc.strip()) and desc.strip() not in (">", "|", ">-", "|-"),
          "missing or block scalar")
    check("description <= 1024 chars", len(desc) <= 1024, "%d chars" % len(desc))
    check("description on one line", not desc_continued and desc.strip() not in (">", "|", ">-", "|-"),
          "description spans several lines")

    if "compatibility" in fields:
        n = len(fields["compatibility"][0])
        check("compatibility <= 500 chars", n <= 500, "%d chars" % n)
    else:
        check("compatibility absent or <= 500 chars", True)

    nlines = len(text.splitlines())
    check("SKILL.md under 500 lines", nlines < 500, "%d lines" % nlines)

    broken = []
    for target in LINK_RE.findall(text):
        t = target.strip("<>")
        if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", t) or t.startswith("#"):
            continue
        path = t.split("#", 1)[0].split("?", 1)[0]
        if path and not (folder / path).exists():
            broken.append(t)
    check("relative links resolve", not broken, "missing: " + ", ".join(broken))

    hits = []
    for lineno, line in enumerate(text.splitlines(), 1):
        if any(r.search(line) for r in ABS_PATH_RES):
            hits.append(str(lineno))
    check("no absolute local paths", not hits, "line(s) " + ", ".join(hits))

    failed = results.count(False)
    print("\n%d passed, %d failed" % (len(results) - failed, failed))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
