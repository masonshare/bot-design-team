#!/bin/sh
# Checks packs/*/scenarios/*.md parse (front matter, sections) and reference existing fake-data files.
cd "$(dirname "$0")/.." || exit 2
exec python scripts/check_scenarios.py
