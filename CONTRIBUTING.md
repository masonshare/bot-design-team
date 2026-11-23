# Contributing

## No real data in this public repo

Never commit real company data: scripts, product names with prices, customer chats, customer or staff names, phone numbers, or secrets (see `docs/adr/0003-no-real-data-in-public-repo.md`). Write fake examples and mark them `FAKE`.

CI (`sh scripts/ci.sh`) runs `scripts/check-no-real-data.py`, which fails on:

- phone-number-like strings (`0xxxxxxxxx`, `+84 ...`, with spaces, dots or dashes)
- chat-transcript lines with a personal name (`Khách: Nguyễn Văn A`, `Customer name: ...`)
- price lists: 3 or more lines with a product and a VND/đ/k price close together

Allowlist (nothing else is exempt):

- files under `packs/*/fake-data/` whose name starts with `FAKE-`
- any line containing the token `FAKE`
- files under `packs/*/scenarios/` that contain `FAKE` anywhere
- test fixtures under `scripts/tests/`

Tests: `bash scripts/tests/run.sh`. Keep `AGENTS.md` and `CLAUDE.md` byte-identical.
