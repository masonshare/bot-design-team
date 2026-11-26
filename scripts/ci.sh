#!/bin/sh
# Single CI entrypoint: runs every static check, exits nonzero if any fails.
# The checks are independent, so they run in parallel (process start-up dominates
# on Windows); output is printed in a fixed order and the exit code is unchanged.
cd "$(dirname "$0")/.." || exit 2
PYTHON=$(for p in python python3; do command -v "$p" >/dev/null 2>&1 && "$p" -c 1 2>/dev/null && { echo "$p"; break; }; done)
[ -n "$PYTHON" ] || { echo "python not found"; exit 2; }
export PYTHON
OUT=$(mktemp -d) || exit 2
trap 'rm -rf "$OUT"' EXIT
n=0
start() { n=$((n+1)); echo "$1" > "$OUT/$n.title"; shift; ( "$@" > "$OUT/$n.out" 2>&1; echo $? > "$OUT/$n.rc" ) & }
start "SKILL.md frontmatter (packs/)" "$PYTHON" scripts/check-frontmatter.py
start "layout and docs pages" sh scripts/check-layout.sh
start "legacy leftovers and AGENTS.md == CLAUDE.md" sh scripts/check-no-legacy.sh
start "scenario files parse" sh scripts/check-scenarios.sh
start "no real company data (leak scan)" "$PYTHON" scripts/check-no-real-data.py
start "column lists agree (template, FAKE CSVs, run-scenarios.py)" "$PYTHON" scripts/check-columns.py
start "glossary Avoid terms not used" "$PYTHON" scripts/check-glossary-avoid.py
start "no tracked __pycache__ or .pyc" sh scripts/check-no-build-artifacts.sh
start "SOUL files do not restate columns or statuses" "$PYTHON" scripts/check-soul-rules.py
start "repo map paths exist and are pointed at" sh scripts/check-repo-map.sh
start "no junk files in packs (backups, SPEC.md, working/...)" "$PYTHON" scripts/check-skill-junk.py
start "neutral skill wording (new packs)" "$PYTHON" scripts/check-skill-neutral.py
start "orchestrator skill list matches the pack folder" "$PYTHON" scripts/check-orchestrator-skills.py
wait
fail=0
i=1
while [ $i -le $n ]; do
  echo "== $(cat "$OUT/$i.title")"; cat "$OUT/$i.out"
  [ "$(cat "$OUT/$i.rc")" = 0 ] || fail=1
  i=$((i+1))
done
if [ $fail -eq 0 ]; then echo "CI OK"; else echo "CI FAILED"; fi
exit $fail
