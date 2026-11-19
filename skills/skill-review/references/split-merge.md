# Split or merge a skill family

Read this when step 4 of skill-review decides whether to split one skill or merge several.

## Cost formula

Measure bytes of the files. Tokens are roughly bytes divided by 4 (a rough rule, not a tokenizer count).

- Always-loaded cost = sum of all descriptions (plus names), paid every turn.
- Per-run cost = the SKILL.md body of the skill that fires, paid on a match.

Example, from splitting a 15 KB skill into six: always-loaded rose from about 1,000 characters of description to about 3,500, which is roughly +600 tokens every turn. The body that loads on one task fell from 15 KB to 5-7 KB, saving roughly 2,000 tokens per run. The split pays back after about the first run that fires, then keeps saving when runs are one-stage jobs. If the user usually runs all stages in one session, the saving shrinks, since several bodies load.

Rule of thumb: split when expected runs per session touch one or two stages, merge when almost every run needs all of them.

## One job per skill

A skill is one thing a user types. Test each candidate with a sentence: "I want to ___". If two skills answer the same sentence, merge or narrow. If one skill answers sentences that start with different verbs and nouns (search, write, test, publish), split.

## Keeping the family together

- Keep one short router skill that names the siblings and the order. It carries the intake and the fallback for a missing sibling.
- Each sibling carries a route table of the same siblings. Renaming a sibling means editing every table.
- A platform that imports only SKILL.md still has to run each skill, so shared short lines are copied, not linked. Typical copies: the language rule, the gate definition, the 5-field handoff, the missing-sibling line.
- Keep a list of every copied line and the files it lives in. When one changes, change all.
- Long reference material moves into the references folder of the one skill that uses it; its SKILL.md keeps a short summary that works alone.
- A script lives only in the skill that runs it. Other skills name it and give the by-hand way.

## Merge candidates

- Two skills whose descriptions differ only in a noun.
- A skill under about 40 lines that is only ever used after another.
- Copies of the same table in three skills: keep the copy in each skill if each must run alone; otherwise keep one.
