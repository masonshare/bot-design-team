#!/bin/bash
# Failing-case tests for scripts/ci.sh. Copies the repo into a temp dir,
# breaks one rule at a time and asserts ci.sh exits nonzero. Plain bash.
set -u
SRC=$(cd "$(dirname "$0")/../.." && pwd)
TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT
pass=0; failn=0

fresh() {
  rm -rf "$TMP/r"; mkdir "$TMP/r"
  (cd "$SRC" && git ls-files -z --cached --others --exclude-standard | xargs -0 -I{} cp --parents {} "$TMP/r/" 2>/dev/null)
  (cd "$TMP/r" && git init -q && git add -A >/dev/null 2>&1)
}
# expect <name> <0|1>: run ci.sh in the current temp copy
expect() {
  local out rc
  out=$(cd "$TMP/r" && git add -A >/dev/null 2>&1; sh scripts/ci.sh 2>&1); rc=$?
  if { [ "$2" = 0 ] && [ $rc -eq 0 ]; } || { [ "$2" = 1 ] && [ $rc -ne 0 ]; }; then
    echo "PASS $1"; pass=$((pass+1))
  else
    echo "FAIL $1 (exit $rc)"; echo "$out" | tail -15; failn=$((failn+1))
  fi
}
t() { fresh; "$2"; expect "$1" "$3"; }

mk_skill() { mkdir -p "$(dirname "$1")"; printf -- '---\nname: %s\ndescription: %s\n---\nbody\n' "$2" "$3" > "$1"; }
PK="$TMP/r/packs/ecommerce-cskh/skills"

c_baseline() { :; }
c_no_name() { sed -i '/^name:/d' "$TMP/r/skills/design/skill-test/SKILL.md"; }
c_wrong_name() { sed -i 's/^name:.*/name: other/' "$TMP/r/skills/design/skill-test/SKILL.md"; }
c_no_desc() { sed -i '/^description:/d' "$TMP/r/skills/design/skill-test/SKILL.md"; }
c_no_frontmatter() { echo "just text" > "$TMP/r/skills/design/skill-test/SKILL.md"; }
c_outside_bucket() { mk_skill "$TMP/r/skills/stray/SKILL.md" stray d; }
c_bad_depth() { mk_skill "$TMP/r/skills/in-progress/a/b/SKILL.md" b d; }
c_no_docs_page() { rm "$TMP/r/docs/skills/bot-soul.md"; }
c_docs_section() { sed -i '/^## Common questions/d' "$TMP/r/docs/skills/bot-soul.md"; }
c_agents_differ() { echo "extra" >> "$TMP/r/AGENTS.md"; }
c_legacy_ref() { echo "see $(printf 'bot%s' mrr) and $(printf 'Gr%s' ok)" >> "$TMP/r/README.md"; }
c_legacy_path() { mkdir -p "$TMP/r/guides"; echo x > "$TMP/r/guides/a.md"; }
c_pack_ok() { mk_skill "$PK/cskh-intake/SKILL.md" cskh-intake d; }
c_bot_pack_ok() { mk_skill "$TMP/r/packs/ecommerce-cskh/staff/skills/cskh-lookup/SKILL.md" cskh-lookup d; }
c_pack_bad_name() { mk_skill "$PK/cskh-intake/SKILL.md" wrong d; }
c_pack_no_desc() { mkdir -p "$PK/cskh-intake"; printf -- '---\nname: cskh-intake\n---\n' > "$PK/cskh-intake/SKILL.md"; }
c_pack_bad_depth() { mk_skill "$PK/x/y/SKILL.md" y d; }

t "baseline passes (no packs/ present)" c_baseline 0
t "pack skill valid is accepted" c_pack_ok 0
t "bot-folder pack skill is accepted" c_bot_pack_ok 0
t "missing name rejected" c_no_name 1
t "name != directory rejected" c_wrong_name 1
t "missing description rejected" c_no_desc 1
t "no frontmatter rejected" c_no_frontmatter 1
t "skill outside bucket rejected" c_outside_bucket 1
t "skill too deep rejected" c_bad_depth 1
t "promoted skill without docs page rejected" c_no_docs_page 1
t "docs page missing section rejected" c_docs_section 1
t "AGENTS.md != CLAUDE.md rejected" c_agents_differ 1
t "legacy leftover text rejected" c_legacy_ref 1
t "legacy path rejected" c_legacy_path 1
t "pack skill name mismatch rejected" c_pack_bad_name 1
t "pack skill missing description rejected" c_pack_no_desc 1
t "pack skill wrong depth rejected" c_pack_bad_depth 1

PY=$(command -v python || command -v python3)
if "$PY" -W ignore "$SRC/scripts/tests/test_run_scenarios.py" >"$TMP/unit.log" 2>&1; then
  echo "PASS run-scenarios unit tests (stub agent)"; pass=$((pass+1))
else
  echo "FAIL run-scenarios unit tests"; tail -20 "$TMP/unit.log"; failn=$((failn+1))
fi

echo "$pass passed, $failn failed"
[ $failn -eq 0 ]
