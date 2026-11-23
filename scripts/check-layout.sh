#!/bin/sh
# Checks the skills layout: buckets exist, every skill is under skills/design|in-progress|deprecated,
# each promoted (design) skill has a docs page with the four sections, and the scripts run.
cd "$(dirname "$0")/.." || exit 2
fail=0
for b in design in-progress deprecated; do
  [ -d "skills/$b" ] || { echo "missing bucket: skills/$b"; fail=1; }
done
for d in skills/*/; do
  b=$(basename "$d")
  case "$b" in design|in-progress|deprecated) ;; *) echo "skill outside a bucket: $d"; fail=1;; esac
done
for f in $(find skills -name SKILL.md); do
  case "$f" in skills/design/*/SKILL.md|skills/in-progress/*/SKILL.md|skills/deprecated/*/SKILL.md) ;; *) echo "bad depth: $f"; fail=1;; esac
done
for d in skills/design/*/; do
  n=$(basename "$d")
  page="docs/skills/$n.md"
  [ -f "$page" ] || { echo "missing docs page: $page"; fail=1; continue; }
  for h in "## What it does" "## When to reach for it" "## Common questions" "## It's working if"; do
    grep -qxF "$h" "$page" || { echo "$page lacks: $h"; fail=1; }
  done
done
python skills/design/skill-package/scripts/validate_skill.py skills/design/skill-design >/dev/null || { echo "validate_skill.py failed"; fail=1; }
python skills/design/bot-score/scripts/score_bot.py skills/design/bot-score/references/sample-profile.md >/dev/null || { echo "score_bot.py failed"; fail=1; }
[ $fail -eq 0 ] && echo "ok"
exit $fail
