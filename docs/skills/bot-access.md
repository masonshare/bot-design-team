# bot-access

## What it does

Sets what a bot may do, which apps it connects to and where credentials live, using least privilege, risk tiers, read-before-write and a gate before every outward or irreversible action.

Source: [`skills/design/bot-access/SKILL.md`](../../skills/design/bot-access/SKILL.md)

## When to reach for it

You ask what a bot should be allowed to do, which tools to give it, whether it may send, delete or pay, or want access trimmed.

## Common questions

**Where do keys go?** Never in the soul or a skill. The skill says where they live.

**What starts read-only?** Everything. Write access is added per need.

**Does it connect the apps?** It decides the access; you apply it in Orca.

## It's working if

- Every permission has a stated reason and a risk tier.
- Outward and irreversible actions sit behind a gate.
- No secret appears in any file.
