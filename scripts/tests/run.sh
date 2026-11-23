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
PH0=$(printf '%s%s' 09 08123456)

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
c_pack_bad_name() { mk_skill "$PK/cskh-intake/SKILL.md" wrong d; }
c_pack_no_desc() { mkdir -p "$PK/cskh-intake"; printf -- '---\nname: cskh-intake\n---\n' > "$PK/cskh-intake/SKILL.md"; }
c_pack_bad_depth() { mk_skill "$PK/x/y/SKILL.md" y d; }

c_leak_phone() { printf 'Lien he: %s
' "$PH0" >> "$TMP/r/README.md"; }
c_leak_phone84() { printf 'Zalo +84 90 812 34 56
' >> "$TMP/r/README.md"; }
c_leak_chat() { printf 'Khách: Nguyễn Văn An
Shop: Dạ chào anh
' >> "$TMP/r/docs/chat.md"; }
c_leak_name_field() { printf 'Customer name: Tran Thi Bich
' >> "$TMP/r/docs/chat.md"; }
c_leak_prices() { printf 'Áo thun trắng 150k
Quần jean xanh 350.000đ
Giày da nâu 1.200.000 VND
' >> "$TMP/r/docs/gia.md"; }
c_fake_ok() { printf 'Khách: Nguyễn Văn An (FAKE)
LH %s FAKE
' "$PH0" >> "$TMP/r/docs/chat.md"; }
c_fake_dir_ok() { printf 'Áo A 150k
Áo B 250k
Áo C 350k
SĐT %s
' "$PH0" > "$TMP/r/packs/ecommerce-cskh/fake-data/FAKE-extra.txt"; }
c_nonfake_in_fakedir() { printf 'SĐT %s
' "$PH0" > "$TMP/r/packs/ecommerce-cskh/fake-data/real.txt"; }
c_scenario_fake_ok() { mkdir -p "$TMP/r/packs/ecommerce-cskh/scenarios"; printf '# FAKE scenario
Khách: Nguyễn Văn An
SĐT %s
' "$PH0" > "$TMP/r/packs/ecommerce-cskh/scenarios/s1.md"; }
c_scenario_nofake() { mkdir -p "$TMP/r/packs/ecommerce-cskh/scenarios"; printf 'SĐT %s
' "$PH0" > "$TMP/r/packs/ecommerce-cskh/scenarios/s1.md"; }

t "baseline passes (no packs/ present)" c_baseline 0
t "pack skill valid is accepted" c_pack_ok 0
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
t "planted phone rejected" c_leak_phone 1
t "planted +84 phone rejected" c_leak_phone84 1
t "planted named chat transcript rejected" c_leak_chat 1
t "planted customer name field rejected" c_leak_name_field 1
t "planted price list rejected" c_leak_prices 1
t "FAKE-marked lines accepted" c_fake_ok 0
t "FAKE- file in fake-data accepted" c_fake_dir_ok 0
t "non-FAKE file in fake-data rejected" c_nonfake_in_fakedir 1
t "scenario file with FAKE token accepted" c_scenario_fake_ok 0
t "scenario file without FAKE rejected" c_scenario_nofake 1

echo "$pass passed, $failn failed"
[ $failn -eq 0 ]
