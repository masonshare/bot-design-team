---
name: bot-access
description: Sets what an AI bot may do, which apps it connects to and where its credentials live, using least privilege, risk tiers, read-before-write and a gate before every outward or irreversible action. Use when the user asks what a bot should be allowed to do, which connections or tools to give it, whether it may send, delete, pay or control the computer, where to put an API key or webhook, or wants a bot's existing access reviewed and trimmed. Not for deciding whether a bot is needed, profile sections other than access, routine specs, scoring or packaging. Vietnamese triggers - quyền của bot, cấp quyền cho bot, kết nối ứng dụng cho bot, bot có được gửi mail không, bí mật và API key, thu hẹp quyền.
license: MIT
metadata:
  author: Masonshare
  version: "2.0.0-draft"
  language: en (Vietnamese edition in references/vi.md)
---

# Bot access

Give the bot the least it needs, and put a gate before anything that cannot be undone. Stage 5 of the bot design flow.

Reply in the user's language. Vietnamese users get Vietnamese output; keep the English term in parentheses on first use.

Giving write access, and every send, publish, delete, spend, install, commit or push, is a **gate**: the user approves first. This skill proposes the access; the user applies it.

## Steps

### 1. Tie every tool to a job

List every tool, connection and skill the bot has or would get, and the job in its Job that needs each one. If it ties to none, remove it: trimming leftovers keeps the context small and the attack surface short. For an existing bot, read the saved state directly; what you could not read is `unverified`, and a teammate's report is not a readback.

Done when: each item has a job, or is listed for removal.

### 2. Set the tier and the control

Grant read and search freely, drafts and writes inside a working folder within scope, and a gate before every outward or irreversible action.

| Risk tier | Examples | Control |
|---|---|---|
| Low | Read, search, summarise | Autonomous, logged |
| Medium | Drafts, files in a working folder | Reviewed before leaving the workspace |
| High | Logins, payments, bulk changes | Gate every time; the human enters passwords, codes and CAPTCHAs |
| Critical | Delete data, sign, change policy | Do not automate |

Done when: every action the bot can take has a tier.

### 3. Apply the rules

- Read before write: start every connection read-only; add write access per tool when a test case needs it.
- Gate before sending, publishing, deleting, spending, installing, committing or pushing code, enabling a schedule.
- Money limits live in the platform's settings, not in prompt text.
- Credentials go only in the platform's secret or connection store. Keep secrets, webhook URLs and auth notes out of prompts, skills, memory, chat and files; ask the user to add them through the secret store.
- Several labelled accounts for one app beat duplicate bots.
- Local computer control: the Grok Bot docs default it to "Ask every time", not "blocked". Choose "Never allow" for any bot whose Job does not need the local machine.
- A routine that waits for approval must not depend on a late answer: cards expire (30 minutes in the Grok Bot docs) and the safe result of an expired card is that nothing happens.
- Bots on one account share one cloud computer. It is not a security boundary between bots: never rely on it to keep one bot's files or secrets from another.

### 4. Show the worst case

Write the permission table (action, tier, control, worst case if the bot is wrong).

Done when: the table shows the worst case if the bot is wrong, every irreversible action has a gate, and no secret appears anywhere in the output.

## Next stage

bot-score. Hand off with exactly 5 fields, in this order: Goal, Inputs, Deliverable, Done when, Open items. If bot-score is not installed, tell the user the next stage is a scorecard plus 5-10 test cases (baseline, then retest) and offer to run it.

## Reference files

- [references/vi.md](references/vi.md): Vietnamese edition. Read when the user writes Vietnamese.

## Sources

- Masonshare, risk tiers and least-privilege rules (original).
- Grok Bot docs, computer and apps (local computer default, shared cloud computer, approval card expiry), https://docs.x.ai/grok-bot/computer-and-apps.
- Lauren Tan, dr-eggbot-v2 marketplace page (no leftover tools), https://x.ai/bot/marketplace/bots/dr-eggbot-v2.
