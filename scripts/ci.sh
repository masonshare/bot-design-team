#!/bin/sh
# Single CI entrypoint: runs every static check, exits nonzero if any fails.
cd "$(dirname "$0")/.." || exit 2
PYTHON=$(for p in python python3; do command -v "$p" >/dev/null 2>&1 && "$p" -c 1 2>/dev/null && { echo "$p"; break; }; done)
[ -n "$PYTHON" ] || { echo "python not found"; exit 2; }
export PYTHON
fail=0
run() { echo "== $1"; shift; "$@" || fail=1; }
run "SKILL.md frontmatter (skills/ and packs/)" "$PYTHON" scripts/check-frontmatter.py
run "layout and docs pages" sh scripts/check-layout.sh
run "legacy leftovers and AGENTS.md == CLAUDE.md" sh scripts/check-no-legacy.sh
run "scenario files parse" sh scripts/check-scenarios.sh
run "no real company data (leak scan)" "$PYTHON" scripts/check-no-real-data.py
if [ $fail -eq 0 ]; then echo "CI OK"; else echo "CI FAILED"; fi
exit $fail
