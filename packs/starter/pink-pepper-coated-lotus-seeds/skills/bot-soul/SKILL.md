---
name: bot-soul
description: Writes, trims or reviews a bot soul, meaning the standing instructions or system prompt an assistant carries on every turn (identity, voice, scope, gates, skill pointers). Use when the user wants a soul or SOUL.md for a bot, a system prompt for a persistent assistant or agent, a soul shortened because it is too long or ignored, or material moved out of a soul into skills. Vietnamese triggers - soul cho bot, viết soul, chỉ dẫn thường trực, system prompt cho trợ lý, rút gọn soul, standing instructions.
license: MIT
metadata:
  author: Masonshare
  version: "2.0.0-draft"
  language: en (Vietnamese edition in references/vi.md)
---

# Bot Soul

A soul is the standing instruction a bot always carries. It loads on every turn, so every line costs attention on every turn. A skill loads on demand, so it can be long. Process credit: the Prompt Architect method by Masonshare.

Reply in the user's language. Vietnamese users get Vietnamese output; keep the English term in parentheses on first use.

Scope: the always-on text of a persistent bot or assistant. A one-off task prompt goes to prompt-design, a failing task prompt to prompt-review, a multi-call workflow to prompt-chain, test loops to prompt-test. Turning a procedure into a reusable skill is skill work, not soul work: hand it to a skill designer.

Work loop: clarify, research, plan, build, verify. A soul runs unattended, so it is always a big prompt: stop at the outline (step 3) and wait for approval.

## Steps

### 1. Intake

Collect in one batch, each with a suggested default: bot name and role, who it serves, language, what it does and what it hands to another bot or a person, hard-to-reverse actions that need approval, skills it carries, and one failure seen so far (for a review). Ask at most 5 questions. For an existing soul, get the current text first.

Done when: the fields are filled or marked as assumptions.

### 2. Sort: soul or skill

Put in the soul only what must hold in every conversation:
- Identity: who the bot is and who it serves, in 2-4 lines.
- Voice: tone and language rules, including reply in the user's language.
- Scope: what it does, what it hands off and to whom.
- Hard guardrails: gates (what needs user approval first), safety rules, how to treat untrusted input.
- Pointers: one line per skill, naming when to load it (the skill description does the triggering).

Put in a skill: workflows, step lists, templates, long examples, domain knowledge, anything only some conversations need. Credentials never go in a soul or a skill; they live in the platform's secret store.

Done when: every line of the input is labelled soul, skill or cut.

### 3. Outline (gate)

Show the section list and a line budget before writing, then wait for approval.

```
Soul: <bot> | Lines: <target 30-60>
Sections: Role / Scope / Voice / Gates / Skills
Moved to skills: <list>   Cut: <list>
Approve to continue? (yes / change X)
```

Done when: the outline is approved.

### 4. Draft

Use this skeleton:

```
# <Bot name>
Role: <one line>
Serves: <user>. Reply in the user's language.

## Scope
Does: <list>
Hands off to: <bot or human>, using the handoff format.

## Voice
<2-4 rules>

## Gates
Ask the user before: <list of hard-to-reverse actions>.

## Skills
- <skill-name>: load when <branch>.
```

Rules:
1. Target 30-60 lines. Over 80 lines, move material into a skill.
2. Front-load the most important rule. Repeat at the end only the one rule that must survive a long chat.
3. State each rule once. Cut what the model does by default.
4. Each rule is checkable: a test case could show it was followed or broken.
5. Write positively; keep a "never" only for a hard guardrail and pair it with the action to take instead.

If the writing-for-agents skill is installed, load it for how to word instructions.

Done when: the soul is written, within the line budget, with no credential in it.

### 5. Quick check and handoff

Run the soul on 3 messages: one in-scope request, one out-of-scope request (it should refuse or route), and one that crosses a gate (it should ask before acting). Fix what fails. For 5-10 cases, baseline, retest and a changelog, hand over to prompt-test. Applying the soul to a bot is a gate: show the final text and wait for approval before installing or replacing anything.

Hand off with exactly 5 fields, in this order: Goal, Inputs, Deliverable, Done when, Open items. Mark untested claims as untested.

Done when: the 3 checks are recorded with pass or fail and the handoff is sent.

## Reference files

- [references/vi.md](references/vi.md): Vietnamese edition. Read when the user writes Vietnamese and wants the process in Vietnamese.

## Sources

- Masonshare, Prompt Architect process and soul rules (original work).
