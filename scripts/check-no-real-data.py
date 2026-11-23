#!/usr/bin/env python3
"""Leak scan (ADR 0003): block real company data in this public repo.

Flags, outside the FAKE allowlist:
  1. Vietnamese phone-number-like strings (0xxxxxxxxx, +84..., spaces/dots/dashes).
  2. Chat-transcript lines carrying a personal name ("Khach: Nguyen Van A",
     "Customer name: ...").
  3. Price lists: 3+ lines with text and a VND/d/k price within a 10-line window.

Allowlist:
  - files under packs/*/fake-data/ whose filename starts with FAKE-
  - any line containing the token FAKE
  - files under packs/*/scenarios/ that contain FAKE anywhere
  - scripts/tests/ (test fixtures) and this script
Stdlib only. Usage: check-no-real-data.py [root]   (default: repo root)
"""
import os
import re
import subprocess
import sys

ROOT = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PHONE = re.compile(r"(?<![\w.+,/-])(?:\+84|0084|0)(?:[ .\-]?\d){9}(?!\d)")
CHAT = re.compile(
    r"^\s*(?:[-*>]\s*|\*\*)?(?:Khách hàng|Khách|KH|Customer|Client|Buyer)\s*\**\s*[:：]\s*\**\s*(?P<v>.+)$",
    re.IGNORECASE)
NAMEFIELD = re.compile(
    r"^\s*(?:[-*>|]\s*)?(?:Customer name|Tên khách hàng|Tên khách|Tên KH|Họ tên khách)\s*[:：]\s*(?P<v>.*)$",
    re.IGNORECASE)
PRICE = re.compile(r"\d[\d.,]*\s*(?:k|K|đ|₫|VND|VNĐ|vnd|vnđ)(?![\w])")
FAKE = "FAKE"


def is_name(value):
    """True for 2-4 capitalised words (a personal name), not placeholders."""
    value = value.strip().strip("*_`\"'")
    if not value or value[0] in "<[{(":
        return False
    words = re.split(r"\s+", value.rstrip(".,!?"))
    if not 2 <= len(words) <= 4:
        return False
    return all(w[0].isalpha() and w[0].isupper() and w.isalpha() for w in words)


def has_name_field(value):
    value = value.strip()
    return bool(value) and value[0] not in "<[{("


def files():
    try:
        out = subprocess.run(["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard"],
                             cwd=ROOT, capture_output=True, check=True).stdout.decode("utf-8", "replace")
        return [p for p in out.split("\0") if p]
    except Exception:
        res = []
        for d, ds, fs in os.walk(ROOT):
            ds[:] = [x for x in ds if x != ".git"]
            res += [os.path.relpath(os.path.join(d, f), ROOT).replace(os.sep, "/") for f in fs]
        return res


def skip_path(p):
    if p.startswith("scripts/tests/") or p == "scripts/check-no-real-data.py":
        return True
    return bool(re.match(r"packs/[^/]+/fake-data/FAKE-[^/]*$", p))


def main():
    problems = []
    for p in files():
        if skip_path(p):
            continue
        try:
            with open(os.path.join(ROOT, p), "rb") as f:
                raw = f.read()
        except OSError:
            continue
        if b"\0" in raw:
            continue
        text = raw.decode("utf-8", "replace")
        if re.match(r"packs/[^/]+/scenarios/", p) and FAKE in text:
            continue
        price_lines = []
        for n, line in enumerate(text.splitlines(), 1):
            if FAKE in line:
                continue
            if PHONE.search(line):
                problems.append(f"{p}:{n}: phone-number-like string")
            chat = CHAT.match(line)
            field = NAMEFIELD.match(line)
            if (chat and is_name(chat.group("v"))) or (field and has_name_field(field.group("v"))):
                problems.append(f"{p}:{n}: chat transcript line with a personal name")
            if PRICE.search(line) and re.search(r"[^\W\d_]{2,}", line):
                price_lines.append(n)
        for i in range(len(price_lines) - 2):
            if price_lines[i + 2] - price_lines[i] <= 10:
                problems.append(f"{p}:{price_lines[i]}: price list (3+ priced lines); mark FAKE or remove")
                break
    for pr in problems:
        print(pr)
    if problems:
        print("real-data scan FAILED: use FAKE-marked sample data only (see CONTRIBUTING.md)")
        return 1
    print("ok")
    return 0


sys.exit(main())
