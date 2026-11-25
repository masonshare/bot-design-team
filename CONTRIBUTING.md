# Contributing

## No real data in this public repo

Never commit real company data: scripts, product names with prices, customer chats, customer or staff names, phone numbers, or secrets (see `docs/adr/0003-no-real-data-in-public-repo.md`). Write fake examples and mark them `FAKE`.

The leak scan `scripts/check-no-real-data.py` fails on:

- phone-number-like strings (`0xxxxxxxxx`, `+84 ...`, with spaces, dots or dashes)
- chat-transcript lines with a personal name (`Khách: Nguyễn Văn A`, `Customer name: ...`)
- price lists: 3 or more lines with a product and a VND/đ/k price close together

Allowlist (nothing else is exempt):

- files under `packs/*/fake-data/` whose name starts with `FAKE-`
- any line containing the token `FAKE`
- files under `packs/*/scenarios/` that contain `FAKE` anywhere
- test fixtures under `scripts/tests/`

## What `sh scripts/ci.sh` runs

1. `scripts/check-frontmatter.py`: SKILL.md frontmatter (name equals directory, description present) and skill placement under `skills/` and `packs/`.
2. `scripts/check-layout.sh`: skill buckets, the four-section docs page (`docs/skills/<name>.md`) for every design skill and every pack skill, and the bundled skill scripts run.
3. `scripts/check-no-legacy.sh`: no legacy leftovers, and `AGENTS.md` equals `CLAUDE.md`.
4. `scripts/check-scenarios.sh`: scenario files in `packs/*/scenarios/` parse and point at existing fake data.
5. `scripts/check-no-real-data.py`: the leak scan above.
6. `scripts/check-columns.py`: the 9 `Kịch bản` columns and the 8 `Đề xuất` columns are identical in `packs/*/sheet-template.md`, the headers of the `FAKE-kich-ban-*.csv` / `FAKE-de-xuat-*.csv` files, and the `KB_COLUMNS` / `DX_COLUMNS` constants in `scripts/run-scenarios.py`. Change a column in all three places together.
7. `scripts/check-glossary-avoid.py`: terms listed under `## Avoid` in `GLOSSARY.md` (for example `chủ dự án`, use `Chủ shop`) must not appear, in any letter case, in `.md` files under `skills/`, `packs/`, `docs/` or the repo root. Only `.md` files are scanned (so `scripts/`, including `scripts/tests/`, is not). Exempt: `GLOSSARY.md` itself, `docs/adr/` (ADRs may quote a term as an example), and any line containing the token `avoid-ok`. Add a term as a bullet under `## Avoid` whose first backticked text is the term.
8. `scripts/check-no-build-artifacts.sh`: no tracked `__pycache__/` content or `*.pyc` among tracked files (`git ls-files`). It does not look at `.gitignore` or untracked files; the ignore rules in `.gitignore` are what keep new ones out of `git add`.
9. `scripts/check-soul-rules.py`: each `packs/*/staff/SOUL.md` and `packs/*/editor/SOUL.md` points at its skills for rules. A line must not list 3 or more sheet column headers (exact match of the template headers), must not list all three statuses `Nháp`, `Đã duyệt`, `Hết hạn` as one adjacent run, and the SOUL must name at least one skill from its own `skills/` folder. Single mentions inside a rule are fine.
10. `scripts/check-repo-map.sh`: `docs/repo-map.md` exists, every repo path it names in backticks exists (a `<placeholder>` or `*` is checked up to that part), and `AGENTS.md` points at it. Update the map when you move or add a top-level folder.

Shared parsing (front matter, phone regex) lives in `scripts/lib/cskh_common.py`. GitHub Actions runs the tests below, then `sh scripts/ci.sh`, on every push and on pull requests to `main`.

Tests: `bash scripts/tests/run.sh` (failing-case tests for the checks, plus unit tests of `scripts/run-scenarios.py` with a stub agent; CI never calls a real agent). It builds one pristine temp copy and resets it between cases, so it runs in under about 75 s on Windows (Git Bash, measured 40-72 s); it was about 150 s with a full copy per case. It aborts with exit 2 if the pristine commit or a reset/clean fails. Keep `AGENTS.md` and `CLAUDE.md` byte-identical. Dispatching pipeline skills to a worker: `docs/agents/dispatch-pipeline-skills.md`.

## Pack layout contract

Where pack skills, docs pages, fake data, scenarios and results live is defined once, in `docs/adr/0005-pack-layout-contract.md`. CI rules and pack tickets both follow it; change the ADR first if a ticket needs a different layout.

## Merge gate

After every merge into an integration branch, run `sh scripts/ci.sh` (about 1 s) and fix any failure before dispatching more work. Parallel tickets can each pass alone and still break each other once merged, so do not wait for GitHub CI to find it. Before opening a PR also run `bash scripts/tests/run.sh` (under about 75 s; run it in the background if your tool has a 120 s timeout).
