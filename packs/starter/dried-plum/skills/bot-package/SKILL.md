---
name: bot-package
description: Packages a designed bot or bot team for rollout in Orca as numbered manual setup steps or an Orca bot share link, with the rollout order and a 10-line summary. Use when the user wants to export, share or publish a bot or team, set a bot up by hand, or learn what a share carries and what it drops. Not for deciding whether a bot is needed, designing the profile, routines, permissions or scoring. Vietnamese triggers - đóng gói team bot, chia sẻ đội bot, cài đặt bot thủ công, chia sẻ bot bằng link Orca.
license: MIT
metadata:
  author: Masonshare
  version: "2.1.0-draft"
  language: en (Vietnamese edition in references/vi.md)
---

# Bot package and rollout

Hand over something a person can install, in an order that stays safe. Stage 7 of the bot design flow.

Reply in the user's language. Vietnamese users get Vietnamese output; keep the English term in parentheses on first use.

Publishing, pushing to a repository, sharing a bot, installing and enabling a schedule are **gates**: the user approves each first. Writing the package is not publishing it.

## Steps

### 1. Choose the route

This repo targets Orca. Write manual setup steps, one numbered list per bot: create the bot, paste identity and soul, add skills, connect apps read-only, set the model, set permissions, add library files, create routines paused. To hand a bot to other people, the owner can share it with Orca's bot share link; the recipient still picks a model and connects apps on their own machine.

Done when: the route is chosen and the target (own machine, or share link) is named.

### 2. Tell the user what a share carries

Assume a share carries the soul and skill text only. Models, credentials, connections and memory stay on the owner's machine, and every skill must work from its SKILL.md alone, because `references/` and `scripts/` may not travel (unverified: check with one real share). After sharing: the recipient picks a model, switches skills on, connects apps themselves and enables routines by hand.

Assign skills by role: each enabled skill ties to one job in its bot's Job, and skills no job uses are disabled or removed, including inherited ones. A bot can own many skills.

Check before sharing: no secret, token or webhook URL in any soul or skill; no real company or customer data in the package.

### 3. Set the rollout order

Roll out in this order, with a gate between stages:
1. One bot, proven alone on the test cases.
2. Routines, starting paused; check each has its five parts, run each by hand twice, then enable.
3. The team, last; add a bot to a group only after it works alone.

Review after 1-2 weeks using usage and history; trim any soul that grew and move procedures into skills.

### 4. Summarise

Done when: the user has the setup steps, the rollout order, and a 10-line summary: what the bot does, does not do, which permissions, approximate cost.

## Reference files

- [references/vi.md](references/vi.md): Vietnamese edition. Read when the user writes Vietnamese.
