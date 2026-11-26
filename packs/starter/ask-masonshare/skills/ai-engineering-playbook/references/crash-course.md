# AI coding fundamentals: our summary

A short summary, in our own words, of the ideas taught in Matt Pocock's AI Coding Crash Course (aihero.dev). It is a study aid, not a copy; the course is the source of truth. Credit is in `CREDITS.md`. Where a line is our own inference it says "(inference)". Numbers can go stale: check the course before quoting them.

## 1. The core flow

Five steps stay the same whatever tool you use: grill, spec, tickets, implement, review.

1. **Grill**: an agent interviews you until the plan is clear. It asks a round of questions, each with a recommended answer, and stops when no open question is left.
2. **Spec**: write the destination down (problem, solution, user stories, decisions, testing, out of scope). Keep it on the issue tracker, not in the repo.
3. **Tickets**: cut the spec into vertical slices. Each slice goes through every layer, is checkable on its own, fits one fresh context window and lists what blocks it.
4. **Implement**: one ticket per session, test-first at a seam you agreed on.
5. **Review**: a fresh agent checks the work on two axes, Standards (does it follow our rules) and Spec (does it do what was asked). A human then reviews the system and tests the real thing.

## 2. Principles

1. Learn fundamentals, not the quirks of one tool.
2. An agent is a model plus a harness plus an environment. Improve the harness and environment before you swap the model.
3. Pick one model and one effort level and keep them. Consistency beats tuning each task.
4. The model is non-deterministic by nature. You cannot remove that, so limit permissions.
5. Quality drops as the context grows. Work early in the context (the "smart zone") and plan your exit before it gets long. The exact limit is a slope, not a cliff.
6. Everything loaded up front (system prompt, tools, skills, steering files) is paid for on every request, in money and in attention. Remove what you do not use.
7. Facts in front of the model beat facts it remembers. Give it the real file, not a hope.
8. The repo is the memory. Write down what must survive a session; be careful with automatic memory.
9. Make the code easy to explore. An agent rediscovers the repo each session.
10. Align before you build. Agents rush to produce things; plan mode only changes what they produce. A shared design idea is what you need.
11. Run the grilled work in the same session while the context is warm, then clear after you commit.
12. Compact only at a phase boundary and always with an instruction.
13. Point by default, push rarely: a steering line needs a stable path and a clear "when to read this". A stale pointer is worse than none.
14. Every line in a steering file earns its place. Prune duplicates, leftovers and lines that change nothing.
15. Team skills live at project level so they ship with the code; personal taste lives at user level.
16. A spec is temporary and editable; tickets are disposable. When the destination moves, edit the spec and regenerate the tickets.
17. More feedback means better work: types, fast tests, a real browser. Passing tests do not mean done.
18. When an agent repeats a mistake, write the rule down once in the coding standards, then enforce it at review.

## 3. Context decisions at a phase boundary

Check top to bottom; the first "yes" wins.

1. **Continue**: you still need this context as the source (just finished grilling) or the next job is tiny.
2. **Clear**: the context is unrelated to the next task. Fastest, but you lose the "why".
3. **Handoff**: you change agent or repo, or pass the work to a person. Write a short Markdown file and reference it.
4. **Subagent**: the job can run unattended and only the summary matters (review, exploration).
5. **Compact**: the default fallback, with a one-sentence instruction about what to keep.

## 4. Steering

- Long procedures go into a doc plus a one-line pointer, or into a skill. Skills load in three layers: name and description always, the body when triggered, extra files when needed.
- A navigation pointer in `AGENTS.md` names files that are hard to find by search or must be edited together. Do not build roads to everywhere.
- Prune with three questions per line: is it a duplicate, is it leftover, does it change anything if removed.

## 5. Shipping big work

- Use the issue tracker for specs and tickets; one skill sets up the tracker's rules.
- Check how the work was cut before you publish tickets; agents still cut by layer.
- Implement with TDD, then review in a fresh context. Finish with manual QA of the real app.
- Running a whole spec unattended is possible but early; a deterministic loop (a script) is steadier than an agent watching an agent (dated).
- Do not use a bundled "do everything" mode for a spec: it puts all the work in one context and ends in the weak part of it.
- A router skill (`ask-matt`) points a situation at the right flow; it is a router, not an oracle.

## 6. Common mistakes

- Prompting straight away without aligning first; the agent never asks.
- Letting context drift into the weak zone, or letting auto-compaction decide what to keep.
- Stuffing `AGENTS.md` with procedures and never pruning it.
- Keeping old specs in the repo: they are short, easy to believe and wrong.
- Cutting tickets by layer instead of by slice.
- Trusting green tests without opening the real app.
- Handing thinking to the agent (inference): chores go to AI, judgement stays with you.
