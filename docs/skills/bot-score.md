# bot-score

## What it does

Scores and tests a bot profile before it ships, reporting design, applied, read-back and behaviour-tested as four separate states. Includes a 14-item scorecard and the optional completeness check (the Python scorer `score_bot.py`).

Source: [`skills/design/bot-score/SKILL.md`](../../skills/design/bot-score/SKILL.md)

## When to reach for it

You want a bot checked for readiness, test cases run for a bot, or a coordinator bot tested.

## Common questions

**What does score_bot.py measure?** Only completeness of the 13 headings, not quality or behaviour.

**How do I run it?** `python scripts/score_bot.py profile.md` from this skill's folder.

**Why four states?** So a design that looks good is not reported as a bot that behaves well.

## It's working if

- Each conclusion cites evidence and its source tier.
- The four states are reported separately.
- The Python scorer runs on references/sample-profile.md and prints a completeness line.
