# bot-shape

## What it does

Decides whether work belongs in one bot or a team (one coordinator plus 2 to 3 specialists) and writes a one-line job and a seven-answer spec per bot.

Source: [`skills/design/bot-shape/SKILL.md`](../../skills/design/bot-shape/SKILL.md)

## When to reach for it

You ask how many bots you need, want to split or merge bots, or a bot does too many jobs.

## Common questions

**Is more bots better?** No. One bot is the default; split only when jobs differ in access, voice or risk.

**Who approves the shape?** You do, at the gate the skill ends with.

**Does it fill the profile?** No. That is bot-profile.

## It's working if

- Every bot has exactly one job line.
- Each bot's access and voice differences justify any split.
- You approved the shape before profiles were written.
