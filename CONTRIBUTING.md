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

Shared parsing (front matter, phone regex) lives in `scripts/lib/cskh_common.py`. GitHub Actions runs the tests below, then `sh scripts/ci.sh`, on every push and on pull requests to `main`.

Tests: `bash scripts/tests/run.sh` (failing-case tests for the checks, plus unit tests of `scripts/run-scenarios.py` with a stub agent; CI never calls a real agent). Keep `AGENTS.md` and `CLAUDE.md` byte-identical.
