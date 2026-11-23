#!/bin/sh
# Checks the skills layout: buckets exist, every skill is under skills/design|in-progress|deprecated,
# each promoted (design) and pack skill has a docs page with the four sections, and the scripts run.
# Rules follow the pack layout contract: docs/adr/0005-pack-layout-contract.md.
cd "$(dirname "$0")/.." || exit 2
fail=0
for b in design in-progress deprecated; do
  [ -d "skills/$b" ] || { echo "missing bucket: skills/$b"; fail=1; }
done
for d in skills/*/; do
  d=${d%/}; b=${d##*/}
  case "$b" in design|in-progress|deprecated) ;; *) echo "skill outside a bucket: $d"; fail=1;; esac
done
for f in $(find skills -name SKILL.md); do
  case "$f" in skills/design/*/SKILL.md|skills/in-progress/*/SKILL.md|skills/deprecated/*/SKILL.md) ;; *) echo "bad depth: $f"; fail=1;; esac
done
check_page() {
  [ -f "$1" ] || { echo "missing docs page: $1"; fail=1; return; }
  # fast path: one grep when all four headings are present
  [ "$(grep -cxF -e "## What it does" -e "## When to reach for it" -e "## Common questions" -e "## It's working if" "$1")" -ge 4 ] && return
  for h in "## What it does" "## When to reach for it" "## Common questions" "## It's working if"; do
    grep -qxF "$h" "$1" || { echo "$1 lacks: $h"; fail=1; }
  done
}
for d in skills/design/*/; do
  d=${d%/}; check_page "docs/skills/${d##*/}.md"
done
# pack skills get the same four-section docs pages
for f in $(find packs -name SKILL.md 2>/dev/null); do
  p=${f%/*}; check_page "docs/skills/${p##*/}.md"
done
"${PYTHON:-python}" skills/design/skill-package/scripts/validate_skill.py skills/design/skill-design >/dev/null || { echo "validate_skill.py failed"; fail=1; }
"${PYTHON:-python}" skills/design/bot-score/scripts/score_bot.py skills/design/bot-score/references/sample-profile.md >/dev/null || { echo "score_bot.py failed"; fail=1; }
[ $fail -eq 0 ] && echo "ok"
exit $fail
