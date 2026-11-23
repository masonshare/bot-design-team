# prompt-chain

## What it does

Turns a multi-step task into a prompt chain: numbered prompts where each output feeds the next, with placeholders, a handoff map and approval points.

Source: [`skills/design/prompt-chain/SKILL.md`](../../skills/design/prompt-chain/SKILL.md)

## When to reach for it

One prompt is too much because the task mixes research, planning, drafting and checking.

## Common questions

**How long is a chain?** As short as the task allows, with an approval point between big stages.

**Where are example prompts?** references/stage-prompts.md.

**Can I run it in any chat model?** Yes. It is plain prompts.

## It's working if

- Each step names its input and its output.
- The handoff map shows what passes between steps.
- Running the chain end to end produced the deliverable.
