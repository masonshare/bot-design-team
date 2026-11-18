# Writing an OpenMausBot team file (team.md)

The format is BotMRR Markdown v1, defined by the openmausbot-teams project (FORMAT.md): https://github.com/milind-soni/openmausbot-teams. This page summarises it for bot designers. When it disagrees with FORMAT.md or the app, FORMAT.md and the app win; check them before publishing.

## Where it lives

- The repo is public and its root holds `botmrr.md` or `team.md` on the `main` or `master` branch.
- The user imports it in OpenMausBot through Teams, Import, by pasting the repo link (a blob or raw URL of the file also works).
- Import is additive: it creates new bots and changes nothing existing, and rolls back if a step fails.

## Frontmatter keys

Checked against the OpenMausBot package parser (`shared/package-format.ts`, v1 schema). Unknown keys are rejected, so copy the shape exactly.

```yaml
---
botmrr: 1
id: my-team                  # lowercase slug: a-z, 0-9, hyphens
release: 1.0.0               # semantic version
name: My Team                # at most 100 characters
tagline: One line for the listing        # at most 160
summary: Two or three sentences on what the team does.   # at most 2000
category: Operations
author:
  name: Your Name
  url: https://github.com/you            # optional
license: MIT
tags: [email, support]                   # optional
outcomes:                                # 1-12 items
  - Inbox cleared before 9am
setupMinutes: 15                         # 1-240
requirements:
  apps:                                  # may be []
    - slug: gmail
      label: Gmail
      reason: Read the inbox the user approves.
      optional: true
  capabilities: [agents, schedules]      # may be []
agents:
  - key: lead
    name: Lead
    title: Coordinator
    description: Routes requests to the specialist and merges answers.
    soul: |
      You coordinate. You do no specialist work. Reply in the user's language.
    appearance:
      color: teal
      mascotExpression: focused          # free text, at most 80 characters
    skills: [triage-inbox]
  - key: writer
    name: Writer
    title: Reply drafter
    description: Drafts replies in the owner's voice.
    soul: |
      You draft short replies. The user sends them.
    appearance:
      color: coral
chiefOfStaff: lead
rooms:                                   # optional
  - key: inbox-desk
    name: Inbox desk
    members: [lead, writer]
    bulletin: Lead owns triage; Writer owns drafts.
    defaultResponder:
      kind: agent                        # agent | everyone | mentions
      agent: lead
routines:                                # optional
  - key: morning-triage
    name: Morning triage
    agent: lead
    prompt: Run triage-inbox and post the summary.
    runOn: maus                          # maus | cloud
    schedule:
      type: daily
      time: 08:00
      weekdays: [1, 2, 3, 4, 5]
    durationMinutes: 30
    enabledAfterInstall: false           # always false
playbooks:                               # optional
  - key: triage
    name: Triage
    summary: Sort unread mail.
    triggers: [inbox review]
    instructions: Read only the approved label...
skills:
  version: 1
  entries:
    - name: triage-inbox
      description: Sorts unread mail into act, wait, ignore. Use each morning.
      license: MIT
      instructions: |
        ---
        name: triage-inbox
        description: Sorts unread mail into act, wait, ignore. Use each morning.
        license: MIT
        ---
        # Triage inbox
        1. ...
---
```

Key notes:
- Every routine carries `enabledAfterInstall: false`; routines always arrive paused.
- `agents[].skills` lists skill names that exist in `skills.entries` (at most 20 per agent).
- `chiefOfStaff` names the `key` of the coordinator agent.
- A working example file: https://github.com/milind-soni/openmausbot-teams/blob/main/packages/inbox-follow-up.md

## Colors

`appearance.color` is one of: green, blue, red, orange, purple, cyan, pink, yellow, teal, coral, silver, chrome.

## The skills block

`skills.entries[].instructions` holds the full SKILL.md text, including its frontmatter, so it must start with `---`. Its `name`, `description` and `license` must match the SKILL.md frontmatter exactly (compare them character by character). Only the SKILL.md text travels: a skill that needs `references/` or `scripts/` must work without them, so put every step a run needs in SKILL.md. Imported skills arrive switched off.

## Body headings (all 7 required, in this order)

1. Activation
2. Mission
3. Outcomes
4. Connections
5. Team
6. Chief of Staff
7. Completion rule

The body is read by people and by a Chief of Staff bot, and must stand on its own when pasted into a conversation. Open with a line such as "Give this file to your Chief of Staff", then state what each heading covers: how to start, the mission, measurable outcomes, apps to connect and why, who is on the team, how the coordinator routes work, and when the job counts as done.

## Limits

- `soul`: at most 24000 bytes per agent.
- `description`: at most 4000 characters.
- At most 20 skills per v1 package.
- A file up to 1,000,000 bytes.

## What does not travel

Models, credentials, connection values, memory and chat history, a skill's `references/` and `scripts/`, and the enabled state of skills and routines. State these in the Connections section so the installer knows what to do by hand: pick a model per bot, switch skills on, connect apps, enable routines.

## Checks before publishing

- Seven body headings present, in order.
- Every agent has a key, name, title, description, soul, color from the list.
- `chiefOfStaff` matches an agent key.
- Every skill listed under an agent exists in `skills.entries`; each `instructions` starts with `---` and matches its SKILL.md name, description and license.
- All routines have `enabledAfterInstall: false`.
- No secret, token or webhook URL anywhere in the file.
- Soul, description and skill counts are inside the limits.
