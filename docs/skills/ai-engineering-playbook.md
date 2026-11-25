# ai-engineering-playbook

## What it does

Gives the Coordinator bot a consistent way to answer questions about AI coding, agent and bot architecture, context management, skill vs subagent vs automation, and AI product strategy. Short questions get a 1-3 line answer; analytical ones follow one frame (conclusion, why, how, differentiation angle, doubts) and draw on public sources: the `mattpocock/skills` repo, aihero.dev posts and the Orca docs, kept in `references/`.

Source: [`skills/design/ai-engineering-playbook/SKILL.md`](../../skills/design/ai-engineering-playbook/SKILL.md)

## When to reach for it

The user asks how to build or run AI-assisted software, which mechanism fits a job, how to keep context healthy, or how to make an AI-built product stand apart.

## Common questions

**Does it hand work to other bots?** No. When the answer is "give this to a bot", or the user asks for advice and then says to do it, it loads `bot-roster` in the same turn.

**Can I trust the numbers in it?** Treat them as dated. Each claim that can go stale is marked, and the skill lists where sources disagree.

**Is anything from a paid course in it?** No. Only public sources are used.

## It's working if

- A short question gets a short answer; an analytical answer has a conclusion, a reason, concrete steps and a differentiation angle.
- Quoted numbers carry a date or an unverified mark.
- Inference is tagged "(suy luận)" rather than presented as Matt Pocock's view.
