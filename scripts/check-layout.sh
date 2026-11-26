#!/bin/sh
# Checks the layout: every SKILL.md is under packs/ at a legal depth (check-frontmatter.py), every pack skill
# has a docs page with the four sections, no top-level skills/ or bots/ folder, and the helper scripts run.
# Rules follow the pack layout contract: docs/adr/0005-pack-layout-contract.md and 0006.
cd "$(dirname "$0")/.." || exit 2
fail=0
for d in skills bots; do
  [ -e "$d" ] && { echo "top-level $d/ must not exist: bots and skills live under packs/ (ADR 0006)"; fail=1; }
done
check_page() {
  [ -f "$1" ] || { echo "missing docs page: $1"; fail=1; return; }
  # fast path: one grep when all four headings are present
  [ "$(grep -cxF -e "## What it does" -e "## When to reach for it" -e "## Common questions" -e "## It's working if" "$1")" -ge 4 ] && return
  for h in "## What it does" "## When to reach for it" "## Common questions" "## It's working if"; do
    grep -qxF "$h" "$1" || { echo "$1 lacks: $h"; fail=1; }
  done
}
# every pack skill gets a docs page with the four sections
for f in $(find packs -name SKILL.md 2>/dev/null); do
  p=${f%/*}; check_page "docs/skills/${p##*/}.md"
done
S=packs/starter
"${PYTHON:-python}" $S/mango-spring-roll/skills/skill-package/scripts/validate_skill.py $S/mango-spring-roll/skills/skill-design >/dev/null || { echo "validate_skill.py failed"; fail=1; }
"${PYTHON:-python}" $S/dried-plum/skills/bot-score/scripts/score_bot.py $S/dried-plum/skills/bot-score/references/sample-profile.md >/dev/null || { echo "score_bot.py failed"; fail=1; }
[ $fail -eq 0 ] && echo "ok"
exit $fail
