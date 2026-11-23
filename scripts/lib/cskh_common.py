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
