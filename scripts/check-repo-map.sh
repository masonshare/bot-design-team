#!/bin/sh
# docs/repo-map.md must exist, every repo path it names in backticks must exist,
# and AGENTS.md must point at it. A path with <placeholder> or * is checked up to that part.
cd "$(dirname "$0")/.." || exit 2
MAP=docs/repo-map.md
[ -f "$MAP" ] || { echo "FAIL missing $MAP"; exit 1; }
fail=0
grep -q 'docs/repo-map.md' AGENTS.md || { echo "FAIL AGENTS.md does not point at $MAP"; fail=1; }
for tok in $(grep -o '`[^` ]*`' "$MAP" | tr -d '`' | grep -E '/|\.(md|sh|py)$' | grep -v -E '^(~|https?:)'); do
  p=$(printf '%s' "$tok" | sed -E 's/[<*].*$//; s#/+$##')
  case "$p" in "") continue;; esac
  [ -e "$p" ] || { echo "FAIL $MAP names a path that does not exist: $tok"; fail=1; }
done
[ $fail -eq 0 ] && echo "repo map ok"
exit $fail
