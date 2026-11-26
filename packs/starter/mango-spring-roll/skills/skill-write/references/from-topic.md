## Starting from a topic (no SOP or notes yet)

Use this route when the user says "make a skill about X" and has no written process. The aim is to get knowledge on paper first, then fit it into the usual steps (size tier, description, body).

### A. Intake: ask once, each question with a default
1. Topic, and who will use the skill (required, no default).
2. Detail level: high, medium or low (default high).
3. Output language (default: the user's language).
4. Execution mode: **coach** (asks the user at every step, hard gates), **auto** (runs end to end, stops only at strategic checkpoints) or **hybrid** (auto by default, coach if the user says so). Default hybrid. Ask this early: it decides the gate structure of the whole body, and changing it later means rewriting.
5. Where the skill will live (for example the user's global skill folder, the project folder, or project-only). Default: the global skill folder. If the project has its own rule about where skills go, follow that rule.

If any answer is vague, ask again. Do not guess.

### B. Quick probe before researching
Run one search for an existing skill on the exact topic (use `skill-search` if installed). If a candidate matches about 90% or more, show it and offer: install it instead, still build a custom one, or search more widely first. Only continue if the user chooses to build. This saves a full research pass when an exact match exists.

### C. Gather knowledge in two passes
1. **From what you already know**: write a self-contained section about the topic for that user and detail level. Mark each claim as from-memory. List the gaps and uncertainties at the end.
2. **From outside sources**, only for the gaps. Count these signals in the gap list: schools of thought that disagree; need for figures or benchmarks that can be checked; a fast-moving or new field beyond your knowledge cut-off; three or more important gaps left. With 0 or 1 signal, do a short targeted search yourself. With 2 or more, stop and ask the user whether to do a quick search or a deeper research run, with the time cost of each. Tag every outside claim with where it came from.

### D. Structure it
Turn the knowledge into a workflow before writing: the steps, who decides at each step, what the output looks like, and where a gate is needed. Mark each step as **auto** (just run), **soft** (run, then show a one-line summary and ask to continue) or **gated** (stop and wait for an answer). Keep gates few; more than three in a run usually means the skill should be split.

### E. Write, then audit
Hand over to steps 1 to 5 of SKILL.md (size tier, description, body, self-check). After writing, do a short audit: does the description trigger on the real phrases, do the files link correctly, does the skill clash with an installed one, and has a design-notes file been written outside the skill folder (`skill-spec-generate`, if installed).

### F. Folder names and resuming
Make the skill folder name from the topic: lowercase, no accents, words joined by hyphens, at most 30 characters. If a previous partial run exists for the same name, ask whether to resume from it or start fresh. Never overwrite an existing skill without asking.
