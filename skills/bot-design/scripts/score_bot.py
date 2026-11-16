#!/usr/bin/env python3
"""Score a bot profile written in Markdown with the 13 section headings.

Usage: python score_bot.py profile.md

Each section is reported as one of:
  filled      real content under the heading
  empty       heading present (or missing) with no real content
  not needed  the section says "not needed" (or "không cần"), ideally with a reason

Score = filled / (filled + empty), over applicable sections only.
The script prints a table and exits 0. Standard library only.
"""
import re
import sys

SECTIONS = [
    ("overview", "Overview"),
    ("identity", "Identity"),
    ("soul", "Soul"),
    ("skills", "Skills"),
    ("memory", "Memory"),
    ("library", "Library"),
    ("routines", "Routines"),
    ("access", "Access"),
    ("model", "Model"),
    ("permissions", "Permissions"),
    ("voice", "Voice/alerts"),
    ("history", "History"),
    ("usage", "Usage"),
]
THRESHOLD = 0.8
NOT_NEEDED = re.compile(r"\bnot needed\b|\bkhông cần\b", re.IGNORECASE)
PLACEHOLDER = re.compile(r"^(todo|tbd|\.\.\.|…|n/a|-|\*)?$", re.IGNORECASE)


def clean(lines):
    """Drop HTML comments, hint blockquotes, blank lines and bare placeholders."""
    text = re.sub(r"<!--.*?-->", "", "\n".join(lines), flags=re.DOTALL)
    out = []
    for line in text.splitlines():
        s = line.strip()
        if not s or s.startswith(">"):
            continue
        if PLACEHOLDER.match(s) or re.fullmatch(r"<[^>]*>", s):
            continue
        out.append(s)
    return out


def split_sections(markdown):
    """Map section key -> body lines, matching headings by their keyword."""
    bodies = {}
    current = None
    for line in markdown.splitlines():
        m = re.match(r"^#{1,6}\s+(.*)$", line)
        if m:
            title = m.group(1).lower()
            current = None
            for key, _ in SECTIONS:
                if re.search(r"\b" + key, title):
                    current = key
                    bodies.setdefault(key, [])
                    break
            continue
        if current:
            bodies[current].append(line)
    return bodies


def classify(lines):
    body = clean(lines)
    if not body:
        return "empty"
    if NOT_NEEDED.search(" ".join(body)) and len(" ".join(body)) < 200:
        return "not needed"
    return "filled"


def main(argv):
    if len(argv) != 2:
        print("Usage: python score_bot.py profile.md")
        return 0
    try:
        with open(argv[1], encoding="utf-8") as f:
            markdown = f.read()
    except OSError as exc:
        print(f"Cannot read {argv[1]}: {exc}")
        return 0

    bodies = split_sections(markdown)
    rows = []
    for key, label in SECTIONS:
        status = classify(bodies[key]) if key in bodies else "empty"
        rows.append((label, status))

    print(f"{'Section':<16}{'Status':<12}")
    print("-" * 28)
    for label, status in rows:
        print(f"{label:<16}{status:<12}")
    print("-" * 28)

    filled = sum(1 for _, s in rows if s == "filled")
    skipped = sum(1 for _, s in rows if s == "not needed")
    applicable = len(rows) - skipped
    score = filled / applicable if applicable else 0.0
    verdict = "PASS" if score >= THRESHOLD else "BELOW 80%"
    print(f"filled {filled}, empty {applicable - filled}, not needed {skipped}")
    print(f"score {filled}/{applicable} = {score:.0%} ({verdict}, target {THRESHOLD:.0%})")
    for label, status in rows:
        if status == "empty":
            print(f"fix: fill {label}, or mark it 'not needed' with a reason")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
