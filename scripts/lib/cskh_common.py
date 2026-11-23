"""Shared helpers for the scripts in scripts/ (stdlib only): one front-matter
parser and one phone-number regex, so every check agrees on both."""
import re

# Vietnamese phone-number-like strings: 0xxxxxxxxx, +84..., 0084..., with spaces, dots or dashes.
PHONE = re.compile(r"(?<![\w.+,/-])(?:\+84|0084|0)(?:[ .\-]?\d){9}(?!\d)")

_KEY = re.compile(r"^([A-Za-z0-9_-]+):\s*(.*)$")


def split_frontmatter(text):
    """Split '---\\n<key: value lines>\\n---\\n<body>' into (meta dict, body).
    Values are stripped of surrounding quotes. Raises ValueError('no frontmatter')
    or ValueError('unterminated frontmatter')."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("no frontmatter")
    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration:
        raise ValueError("unterminated frontmatter") from None
    meta = {}
    for line in lines[1:end]:
        m = _KEY.match(line)
        if m:
            meta[m.group(1)] = m.group(2).strip().strip("\"'")
    return meta, "\n".join(lines[end + 1:])


def template_columns(text):
    """Column headers of the two tables in sheet-template.md whose header row is
    '| Column | Header | Content |': (scripts sheet `Kịch bản`, `Đề xuất` file).
    Returns a pair of lists, in table order."""
    tables, cur = [], None
    for line in text.splitlines():
        if not line.lstrip().startswith("|"):
            cur = None
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if cells[:3] == ["Column", "Header", "Content"]:
            cur = []
            tables.append(cur)
        elif cur is not None and len(cells) >= 2 and not set(cells[0]) <= set("-: "):
            cur.append(cells[1])
    if len(tables) != 2:
        raise ValueError(f"expected 2 column tables in sheet template, found {len(tables)}")
    return tables[0], tables[1]


def avoid_terms(glossary_text):
    """Terms listed under the '## Avoid' section of GLOSSARY.md: the first
    backticked term of each '- ' bullet. Empty list if there is no section."""
    terms, inside = [], False
    for line in glossary_text.splitlines():
        if line.startswith("## "):
            inside = line.strip() == "## Avoid"
        elif inside and line.startswith("- "):
            m = re.search(r"`([^`]+)`", line)
            if m:
                terms.append(m.group(1))
    return terms
