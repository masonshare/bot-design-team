#!/usr/bin/env python3
"""Small draft-copy checker. Standard library only (Python 3), Windows and Linux.

Usage:
    python copy_check.py --file draft.txt
    python copy_check.py "Some copy text"
    python copy_check.py --stdin < draft.txt

It flags things for a human to review. It does not judge quality.
"""
import argparse
import re
import sys

STOCK = [
    "unlock", "seamless", "seamlessly", "game-changer", "game changer", "leverage",
    "cutting-edge", "revolutionary", "synergy", "best-in-class", "world-class",
    "in today's world", "have you ever wondered", "it's no secret", "at the end of the day",
    "in order to", "due to the fact that", "delve",
]
PROOFY = re.compile(r"\b\d[\d,.]*\s?(%|x\b|percent\b|times\b)|\b(guarantee[d]?|proven|clinically|#1|number one|best selling)\b", re.I)
PLACEHOLDER = re.compile(r"\[[A-Z][A-Z ]{2,}[:\]][^\]]*\]?")


def sentences(text):
    parts = re.split(r"(?<=[.!?])\s+|\n+", text)
    return [p.strip() for p in parts if p.strip()]


def syllables(word):
    word = re.sub(r"[^a-z]", "", word.lower())
    if not word:
        return 0
    groups = re.findall(r"[aeiouy]+", word)
    count = len(groups)
    if word.endswith("e") and count > 1:
        count -= 1
    return max(count, 1)


def main():
    ap = argparse.ArgumentParser(description="Flag issues in draft copy.")
    ap.add_argument("text", nargs="?")
    ap.add_argument("--file", "-f")
    ap.add_argument("--stdin", action="store_true")
    a = ap.parse_args()
    if a.stdin:
        text = sys.stdin.read()
    elif a.file:
        with open(a.file, encoding="utf-8") as fh:
            text = fh.read()
    elif a.text:
        text = a.text
    else:
        ap.print_help()
        return 1

    sents = sentences(text)
    words = re.findall(r"[A-Za-z']+", text)
    if not words or not sents:
        print("No text found.")
        return 1
    syl = sum(syllables(w) for w in words)
    wps = len(words) / len(sents)
    spw = syl / len(words)
    grade = 0.39 * wps + 11.8 * spw - 15.59  # English-oriented estimate
    lengths = [len(re.findall(r"[A-Za-z']+", s)) for s in sents]
    low = text.lower()

    print(f"Words: {len(words)}  Sentences: {len(sents)}  Avg words/sentence: {wps:.1f}")
    print(f"Longest sentence: {max(lengths)} words  Shortest: {min(lengths)} words")
    print(f"Reading level estimate (English only): grade {grade:.1f}")
    if grade > 9:
        print("  -> Above grade 9: consider shorter sentences and simpler words.")
    hits = sorted({s for s in STOCK if s in low})
    print("Stock phrases: " + (", ".join(hits) if hits else "none"))
    claims = sorted({m.group(0) for m in PROOFY.finditer(text)})
    print("Claims to source or support: " + (", ".join(claims) if claims else "none"))
    ph = PLACEHOLDER.findall(text)
    print(f"Open placeholders: {len(ph)}")
    for p in ph[:10]:
        print("  " + p)
    you = len(re.findall(r"\byou(r|rs)?\b", low))
    we = len(re.findall(r"\b(we|our|us|i|my)\b", low))
    print(f"Reader words (you) vs sender words (we/I): {you} vs {we}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
