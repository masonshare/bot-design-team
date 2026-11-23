# Scenarios

Behaviour scenarios for the pack's bots, written as plain Markdown so a person or an agent can replay them. They use FAKE data only (see `../fake-data/`). Files are named `<ticket>-<slug>.md`, for example `t8-approved-right-channel.md`.

## Format

```
---
id: t8-approved-right-channel
bot: staff
data: FAKE-kich-ban-cong-ty-mau.csv
channel: Shopee
---

## Message
The staff or owner message, in Vietnamese.

## Expect
- Observable expectation (reply content, which script code is used, sheet changes).

## Must not
- Behaviour that must not happen.
```

Rules:

- Front matter has exactly the keys `id`, `bot`, `data`, `channel`.
- `id` equals the file name without `.md`.
- `bot` is `staff` or `editor`.
- `data` names an existing file in `fake-data/` (a leading `fake-data/` is tolerated).
- `channel` is `Shopee`, `Zalo`, `hotline`, or `all` or `none` (editor scenarios).
- Sections `## Message`, `## Expect`, `## Must not` appear once each, in that order. `## Expect` and `## Must not` hold bullet lists.
- Expectations must be observable: what the reply says, which script code it came from, which sheet tabs change (or `no sheet change`).

## Replay

Load the named data file as the Sheet (pasted CSV or a copy of the template Sheet), start the bot, set the channel, send the `## Message`, and check each bullet.

`scripts/check-scenarios.sh` only checks that the files parse and point at real data.

## Automated run

`python scripts/run-scenarios.py --agent claude|codex` replays every scenario headlessly and writes `results/<agent>-<date>.md`. See `docs/scenario-testing.md`.
