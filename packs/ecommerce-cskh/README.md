# Pack: ecommerce-cskh (customer service for e-commerce shops)

A two-bot pack for a Vietnamese e-commerce shop (Shopee, Zalo, hotline). The shop owner keeps approved reply scripts in a Google Sheet. An Editor bot helps the owner write and clean up scripts. A Staff bot helps customer-service staff answer customers using only approved scripts.

Needs the Starter pack first (`packs/starter/`): install it before this one.

Everything in this folder uses FAKE data. No real company, product, price or customer data belongs here. The skills (`cskh-lookup`, `cskh-no-script`, `cskh-draft`) live under each bot's `skills/` folder; each has a docs page in `docs/skills/`.

## What is in the pack

```
packs/ecommerce-cskh/
  README.md            this file
  sheet-template.md    Google Sheet tabs, exact columns, status vocabulary, access model
  voice-guide.md       placeholder brand-voice guide (Vietnamese)
  editor/              Editor bot home: SOUL.md, skills/
  staff/               Staff bot home: SOUL.md, skills/
  fake-data/           FAKE sample scripts, for testing only
```

The folder layout is a contract enforced by CI: see `docs/adr/0005-pack-layout-contract.md`.

Each bot folder is in bot-home form (see `docs/orca-skill-loading.md` and `docs/adr/0001-*.md`): `SOUL.md` plus `skills/<name>/SKILL.md`. Orca writes the `bot.json` manifest itself when a bot is shared, so none is kept here. Do not place skills in `.claude/skills` or `.agents/skills` inside a bot home; Orca links them.

Editor and Staff are two separate bots with two separate share links. The Staff bot must never get the Editor's write access.

## Where the bots run

Bots run on the customer's own machine and under the customer's own AI subscriptions. Nothing in this pack is hosted by the pack author. A share link carries only the bot's files (soul, ticked skills, connector kinds; no sign-ins or secrets). Each person signs in to Google themselves.

## Setup

1. Create the Google Sheet from `sheet-template.md` in the owner's Google account. Put real scripts only there, never in this repo.
2. Fill `voice-guide.md` with the shop's real tone. Keep the real copy out of any shared package unless it holds nothing sensitive.
3. In Orca, create the Editor bot from `editor/` and the Staff bot from `staff/` (copy each folder's contents into a new bot home). Add the Sheet link in the bot's own memory after creation, not in the files here.
4. Connect Google (connector kind `google`) for each bot, signed in as the right person (see permissions below).
5. Share the Staff bot link with staff. Each staff member opens it on their own machine and picks their own agent. The package only hints at the agent, so each person confirms it runs on their machine.
6. Do not rely on schedules; they arrive disabled.

## Google permissions needed

| Who | Sheet access | Why |
|---|---|---|
| Owner | Owner / editor | Approves scripts, manages tabs |
| Editor bot (signed in as the owner or an editor) | Edit on tab `Kịch bản` (scripts file); read `Đề xuất CSKH` | Writes `Nháp` rows only |
| Staff members | View-only on the scripts file; editor on the separate `Đề xuất CSKH` file | Read approved scripts; log unknown questions |
| Staff bot (signed in as the staff member) | Read the scripts file; append rows to the `Đề xuất CSKH` file only | Logs unknown questions |

The `Đề xuất` tab is its own Google Sheet file (`Đề xuất CSKH`) because Google shares per file, not per tab. See `sheet-template.md`.

Google Sheets read and write scope is enough. No Drive-wide or Gmail access is needed.

## Rollout: owner, then pilot, then team

Step-by-step checklist with exit criteria: [`docs/pilot-rollout-checklist.md`](../../docs/pilot-rollout-checklist.md).

1. Owner: builds the Sheet, runs the Editor bot, approves a first batch of scripts (status `Đã duyệt`, with approver and date).
2. Pilot: one staff member uses the Staff bot for about a week. Review the `Đề xuất CSKH` file daily, fix wrong answers, add missing scripts.
3. Team: share the Staff bot link with the rest of the staff once the pilot's answers are acceptable.

## Editor skill: cskh-draft

`editor/skills/cskh-draft/` drafts scripts from pasted chats, questions or the public Q&A page. Drafts are always `Nháp`; only the owner approves. Scenarios for it are in `scenarios/t10-*.md`.

Data rule: the real Q&A content and real chats are loaded into the owner's own Google Sheet at runtime only. This repo holds FAKE data only; tests use `fake-data/FAKE-qa-khong-nhat-quan.txt` and `fake-data/FAKE-chat-khach.txt`.

## Testing with fake data

`fake-data/` holds files for the fictional "Công ty Mẫu". Every file name and every row is marked FAKE. Import the CSVs into a test Sheet to try the bots. Prices, days and policies in them are invented. `FAKE-qa-khong-nhat-quan.txt` is a deliberately inconsistent Q&A page, to check that the bots flag contradictions instead of picking one.
