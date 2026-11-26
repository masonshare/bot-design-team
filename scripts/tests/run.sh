#!/bin/bash
# Failing-case tests for scripts/ci.sh. Copies the repo into a temp dir,
# breaks one rule at a time and asserts ci.sh exits nonzero. Plain bash.
set -u
SRC=$(cd "$(dirname "$0")/../.." && pwd)
TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT
pass=0; failn=0

# One pristine copy is built once (committed in its own throwaway repo); fresh()
# only resets it: reset --hard restores mutated/deleted files, clean drops files
# a case added. No per-case full-repo copy (that took >120 s on Windows).
PRISTINE=0
fresh() {
  if [ $PRISTINE -eq 0 ]; then
    mkdir -p "$TMP/r"
    (cd "$SRC" && git ls-files -z --cached --others --exclude-standard | tar --null -T - -cf - 2>/dev/null) | tar -xf - -C "$TMP/r"
    (cd "$TMP/r" && git init -q && git config core.autocrlf false && git add -A >/dev/null 2>&1       && git -c user.name=t -c user.email=t@t -c commit.gpgsign=false commit -qm pristine >/dev/null 2>&1)       || { echo "ABORT: could not create the pristine commit; test state would leak" >&2; exit 2; }
    PRISTINE=1
  else
    (cd "$TMP/r" && git reset -q --hard && git clean -fdxq)       || { echo "ABORT: reset/clean of the pristine copy failed; test state would leak" >&2; exit 2; }
  fi
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
c_no_name() { sed -i '/^name:/d' "$TMP/r/packs/starter/mango-spring-roll/skills/skill-test/SKILL.md"; }
c_wrong_name() { sed -i 's/^name:.*/name: other/' "$TMP/r/packs/starter/mango-spring-roll/skills/skill-test/SKILL.md"; }
c_no_desc() { sed -i '/^description:/d' "$TMP/r/packs/starter/mango-spring-roll/skills/skill-test/SKILL.md"; }
c_no_frontmatter() { echo "just text" > "$TMP/r/packs/starter/mango-spring-roll/skills/skill-test/SKILL.md"; }
c_bad_depth() { mk_skill "$TMP/r/packs/starter/mango-spring-roll/skills/a/b/SKILL.md" b d; }
c_no_docs_page() { rm "$TMP/r/docs/skills/bot-soul.md"; }
c_docs_section() { sed -i '/^## Common questions/d' "$TMP/r/docs/skills/bot-soul.md"; }
c_pack_docs_section() { sed -i '/^## Common questions/d' "$TMP/r/docs/skills/cskh-lookup.md"; }
c_pack_no_docs() { rm "$TMP/r/docs/skills/cskh-draft.md"; }
c_scenario_bad() { sed -i 's/^## Must not/## Nope/' "$TMP/r/packs/ecommerce-cskh/scenarios/t9-sensitive-price.md"; }
c_agents_differ() { echo "extra" >> "$TMP/r/AGENTS.md"; }
c_legacy_ref() { echo "see $(printf 'bot%s' mrr) and $(printf 'Gr%s' ok)" >> "$TMP/r/README.md"; }
c_legacy_path() { mkdir -p "$TMP/r/guides"; echo x > "$TMP/r/guides/a.md"; }
c_pack_ok() { mk_skill "$PK/cskh-intake/SKILL.md" cskh-intake d; cp "$TMP/r/docs/skills/cskh-lookup.md" "$TMP/r/docs/skills/cskh-intake.md"; }
c_bot_pack_ok() { mk_skill "$TMP/r/packs/ecommerce-cskh/staff/skills/cskh-lookup/SKILL.md" cskh-lookup d; }
c_pack_bad_name() { mk_skill "$PK/cskh-intake/SKILL.md" wrong d; }
c_pack_no_desc() { mkdir -p "$PK/cskh-intake"; printf -- '---\nname: cskh-intake\n---\n' > "$PK/cskh-intake/SKILL.md"; }
c_pack_misplaced() { mk_skill "$TMP/r/packs/ecommerce-cskh/staff/cskh-x/SKILL.md" cskh-x d; }
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
' "$PH0" > "$TMP/r/packs/ecommerce-cskh/scenarios/s1.txt"; }
c_scenario_nofake() { mkdir -p "$TMP/r/packs/ecommerce-cskh/scenarios"; printf 'SĐT %s
' "$PH0" > "$TMP/r/packs/ecommerce-cskh/scenarios/s1.txt"; }

t "baseline passes (no packs/ present)" c_baseline 0
t "pack skill valid is accepted" c_pack_ok 0
t "bot-folder pack skill is accepted" c_bot_pack_ok 0
t "missing name rejected" c_no_name 1
t "name != directory rejected" c_wrong_name 1
t "missing description rejected" c_no_desc 1
t "no frontmatter rejected" c_no_frontmatter 1
t "skill too deep rejected" c_bad_depth 1
t "promoted skill without docs page rejected" c_no_docs_page 1
t "docs page missing section rejected" c_docs_section 1
t "pack skill docs page missing section rejected" c_pack_docs_section 1
t "pack skill without docs page rejected" c_pack_no_docs 1
t "malformed scenario file rejected" c_scenario_bad 1
t "AGENTS.md != CLAUDE.md rejected" c_agents_differ 1
t "legacy leftover text rejected" c_legacy_ref 1
t "legacy path rejected" c_legacy_path 1
t "pack skill name mismatch rejected" c_pack_bad_name 1
t "pack skill missing description rejected" c_pack_no_desc 1
t "pack skill wrong depth rejected" c_pack_bad_depth 1
t "pack skill outside a skills/ folder rejected" c_pack_misplaced 1
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

SH="$TMP/r/packs/ecommerce-cskh"
c_col_template() { sed -i 's/| G | Lưu ý nội bộ |/| G | Ghi chú |/' "$SH/sheet-template.md"; }
c_col_template_dx() { sed -i 's/| H | Số lần hỏi |/| H | Lần hỏi |/' "$SH/sheet-template.md"; }
c_col_csv() { sed -i '1s/Trạng thái,/Status,/' "$SH/fake-data/FAKE-kich-ban-cong-ty-mau.csv"; }
c_col_csv_dx() { sed -i '1s/,Số lần hỏi/,Số lần hỏi,Thừa/' "$SH/fake-data/FAKE-de-xuat-cong-ty-mau.csv"; }
c_col_const() { sed -i '/^KB_COLUMNS/s/Lưu ý nội bộ/Ghi chú/' "$TMP/r/scripts/run-scenarios.py"; }
c_col_const_dx() { sed -i '/^DX_COLUMNS/s/Mã gần nhất/Mã/' "$TMP/r/scripts/run-scenarios.py"; }
c_term_skill() { printf 'Hỏi %s duyệt.
' "$(printf 'chủ dự %s' án)" >> "$TMP/r/packs/starter/mango-spring-roll/skills/skill-test/SKILL.md"; }
c_term_soul() { printf 'Gửi %s.
' "$(printf 'Chủ Dự %s' Án)" >> "$SH/staff/SOUL.md"; }
c_term_docs() { printf 'Gửi %s.
' "$(printf 'chủ dự %s' án)" >> "$TMP/r/docs/skills/bot-soul.md"; }
c_term_adr_ok() { mkdir -p "$TMP/r/docs/adr"; printf 'Ví dụ tránh: %s.
' "$(printf 'chủ dự %s' án)" >> "$TMP/r/docs/adr/0099-x.md"; }
c_term_marker_ok() { printf 'Không dùng %s (avoid-ok).
' "$(printf 'chủ dự %s' án)" >> "$TMP/r/docs/skills/bot-soul.md"; }
c_avoid_missing() { sed -i '/^## Avoid/,$d' "$TMP/r/GLOSSARY.md"; }
c_pyc_tracked() { mkdir -p "$TMP/r/scripts/lib/__pycache__"; echo x > "$TMP/r/scripts/lib/__pycache__/a.cpython-3.pyc"; (cd "$TMP/r" && git add -f scripts/lib/__pycache__/a.cpython-3.pyc); }
c_pyc_loose() { echo x > "$TMP/r/scripts/stray.pyc"; (cd "$TMP/r" && git add -f scripts/stray.pyc); }
c_pyc_untracked_ok() { mkdir -p "$TMP/r/scripts/lib/__pycache__"; echo x > "$TMP/r/scripts/lib/__pycache__/a.cpython-3.pyc"; }
c_soul_cols() { printf 'Các cột: Mã, Nhóm, Tình huống.
' >> "$SH/staff/SOUL.md"; }
c_soul_cols_dx() { printf 'Đề xuất có Ngày, Kênh, Người hỏi.
' >> "$SH/editor/SOUL.md"; }
c_soul_status() { printf 'Trạng thái: Nháp, Đã duyệt, Hết hạn.
' >> "$SH/editor/SOUL.md"; }
c_soul_nopointer() { sed -i 's/cskh-draft/x/g' "$SH/editor/SOUL.md"; }
c_soul_two_ok() { printf 'Nháp hoặc Hết hạn thì không dùng; Mã và Nhóm xem skill cskh-lookup.
' >> "$SH/staff/SOUL.md"; }

t "template header drift rejected" c_col_template 1
t "template Đề xuất header drift rejected" c_col_template_dx 1
t "scripts CSV header drift rejected" c_col_csv 1
t "Đề xuất CSV extra column rejected" c_col_csv_dx 1
t "run-scenarios KB_COLUMNS drift rejected" c_col_const 1
t "run-scenarios DX_COLUMNS drift rejected" c_col_const_dx 1
t "avoided term in a skill rejected" c_term_skill 1
t "avoided term in a SOUL (any case) rejected" c_term_soul 1
t "avoided term in docs rejected" c_term_docs 1
t "avoided term in docs/adr accepted" c_term_adr_ok 0
t "avoided term on avoid-ok line accepted" c_term_marker_ok 0
t "GLOSSARY.md without Avoid section rejected" c_avoid_missing 1
t "tracked __pycache__ file rejected" c_pyc_tracked 1
t "tracked stray .pyc rejected" c_pyc_loose 1
t "untracked ignored __pycache__ accepted" c_pyc_untracked_ok 0
t "SOUL restating sheet columns rejected" c_soul_cols 1
t "SOUL restating Đề xuất columns rejected" c_soul_cols_dx 1
t "SOUL defining status vocabulary rejected" c_soul_status 1
t "SOUL without a skill pointer rejected" c_soul_nopointer 1
t "SOUL naming two statuses or two columns accepted" c_soul_two_ok 0

c_map_bad_path() { printf 'Extra: `packs/nope/staff/`.
' >> "$TMP/r/docs/repo-map.md"; }
c_map_missing() { rm "$TMP/r/docs/repo-map.md"; }
c_map_placeholder_ok() { printf 'Extra: `packs/<pack>/scenarios/`.
' >> "$TMP/r/docs/repo-map.md"; }
c_nav_missing() { sed -i '/repo-map/d' "$TMP/r/AGENTS.md" "$TMP/r/CLAUDE.md"; }
t "repo map naming a missing path rejected" c_map_bad_path 1
t "missing repo map rejected" c_map_missing 1
t "repo map placeholder path accepted" c_map_placeholder_ok 0
t "steering file without repo-map pointer rejected" c_nav_missing 1

MK="$TMP/r/packs/marketing-ecommerce/skills"
c_junk_bak() { echo x > "$MK/ecommerce-kpi-analytics/SKILL.md.bak.1"; }
c_junk_spec() { echo x > "$MK/ecommerce-kpi-analytics/SPEC.md"; }
c_junk_working() { mkdir -p "$MK/ecommerce-kpi-analytics/working"; echo x > "$MK/ecommerce-kpi-analytics/working/a.md"; }
c_junk_transcript() { echo x > "$MK/ecommerce-kpi-analytics/transcript-lecture.txt"; }
c_neutral_ask() { printf 'Dung AskUserQuestion de hoi.
' >> "$MK/ecommerce-kpi-analytics/SKILL.md"; }
c_neutral_brand() { printf 'Vi du: Nam Xanh ban tra.
' >> "$MK/ecommerce-kpi-analytics/SKILL.md"; }
c_neutral_url() { printf 'Xem https://example.com/x
' >> "$MK/ecommerce-kpi-analytics/SKILL.md"; }
c_neutral_slash() { printf 'Go /express de chay nhanh.
' >> "$MK/ecommerce-kpi-analytics/SKILL.md"; }
c_neutral_claude_path() { printf 'Luu o ~/.claude/skills.
' >> "$MK/ecommerce-kpi-analytics/SKILL.md"; }
c_neutral_license_ok() { mk_skill "$MK/vendored/SKILL.md" vendored d; printf 'See https://example.com and AskUserQuestion
' >> "$MK/vendored/SKILL.md"; printf 'MIT License
' > "$MK/vendored/LICENSE"; cp "$TMP/r/docs/skills/ecommerce-kpi-analytics.md" "$TMP/r/docs/skills/vendored.md"; }
c_neutral_starter_old_ok() { printf 'Dung AskUserQuestion.
' >> "$TMP/r/packs/starter/mango-spring-roll/skills/skill-test/SKILL.md"; }
c_neutral_framework_ok() { printf 'Khung AIDA, JTBD va BATNA van duoc dung.
' >> "$MK/ecommerce-kpi-analytics/SKILL.md"; }
t "backup file in a pack rejected" c_junk_bak 1
t "SPEC.md in a pack rejected" c_junk_spec 1
t "working/ folder in a pack rejected" c_junk_working 1
t "transcript file in a pack rejected" c_junk_transcript 1
t "AskUserQuestion in a marketing skill rejected" c_neutral_ask 1
t "real company brand in a marketing skill rejected" c_neutral_brand 1
t "URL in a marketing skill rejected" c_neutral_url 1
t "slash command in a marketing skill rejected" c_neutral_slash 1
t ".claude path in a marketing skill rejected" c_neutral_claude_path 1
t "third-party skill folder with LICENSE exempt from neutral check" c_neutral_license_ok 0
t "older starter skill naming a Claude tool accepted" c_neutral_starter_old_ok 0
t "framework names (AIDA, JTBD, BATNA) accepted" c_neutral_framework_ok 0

PY=$(command -v python || command -v python3)
if "$PY" -W ignore "$SRC/scripts/tests/test_run_scenarios.py" >"$TMP/unit.log" 2>&1; then
  echo "PASS run-scenarios unit tests (stub agent)"; pass=$((pass+1))
else
  echo "FAIL run-scenarios unit tests"; tail -20 "$TMP/unit.log"; failn=$((failn+1))
fi

echo "$pass passed, $failn failed"
[ $failn -eq 0 ]
