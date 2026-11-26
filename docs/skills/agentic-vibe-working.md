# agentic-vibe-working

## What it does

A six-step framework that lets an AI agent run a complex, multi-step job end to end: clarify, research, plan, execute, verify, package. It keeps a checkbox plan file the agent re-reads after its context is compacted, and stops at fixed points for the user to decide. An optional last step packages the result as a skill. Body in Vietnamese, description bilingual. `scripts/context-recovery.py` prints the unticked items of a plan file (standard library only, runs on Windows and Linux).

Handing a complex job to an agent usually fails in three places: misreading the request, taking the first approach that comes to mind, and declaring it done with no evidence. The fixed stops are after clarifying, after planning, after verification and at the packaging decision. A first test run stopped at the clarifying step without delivering, so the skill now has a "when the user cannot be asked" section. Instead of a session hook (which Codex lacks), recovery works by re-reading the plan file at the start of every turn. Reference points: 3 to 5 questions in step 1; at most 7 to 10 plan steps; escalate to deep research when 2 of 4 signals are present; retry a failed step twice, then find the root cause and fix the plan; at most 3 self-correction rounds in step 5a, then tell the user. Every number in this skill is a labelled reference point; adjust it to your kind of work. The test run did not execute the script beyond the author's own try with a sample plan; CI runs it on a FAKE plan.

Source: [`packs/starter/ask-masonshare/skills/agentic-vibe-working/SKILL.md`](../../packs/starter/ask-masonshare/skills/agentic-vibe-working/SKILL.md)

## When to reach for it

The user hands over a big job (build this feature, write a full guide, analyse this problem, do it end to end) that needs research, a plan and checks. Not for one-step jobs. It sits with Ask Masonshare, the chief of staff, because it is a way of running work rather than a bot or skill design job.

## Common questions

**Does it run without asking me anything?** No. It stops for you at the clarifying, planning, verification and packaging points. If you cannot be asked, it states its assumptions and carries on to a deliverable.

**What does the script do?** It reads a Markdown plan file and prints the items still unticked, so the agent can find its place after its context was cut.

**Do I have to package the result as a skill?** No. Packaging is a choice at the last stop.

## It's working if

- A plan file with checkboxes exists and the agent re-reads it after a context cut.
- The agent stopped at the fixed points and did not claim done without evidence.
- The final answer lists what was verified and how.
