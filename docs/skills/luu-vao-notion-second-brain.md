# luu-vao-notion-second-brain

## What it does

An optional storage module. When the user switches it on, outputs (notes, tasks, new projects) are saved into their Notion second-brain workspace instead of the default Google Docs, Sheets and Slides, under strict rules: create only, never edit or delete, mark every page with a user-chosen prefix and tag, and report a back-link after each save. Body in Vietnamese, description bilingual.

Other skills save to Google by default. Some people keep a second brain in Notion and want results there without giving the agent broad rights. The module uses only three databases (notes, tasks, projects), announces a new project in one line before creating it, and asks its setup questions once. The setup answers (database names or links, prefix, tag) are stored only in the user's own profile document, kept in the same place as `brand-profile.md`, never inside the skill; the skill holds no IDs, links or account details. The skill is honest about its limits: the rules are what the agent obeys, not what the Notion connection enforces, so for more safety share just those three databases with the connection. Full content, including figures, is saved as is in a note for named customer work, never shortened. Reference points: 3 databases; one line of notice before creating a project; one round of setup questions. In testing it asked five questions at once and once leaked a phrase about the test session into an answer, so check the wording on a real run.

Source: [`packs/starter/ask-masonshare/skills/luu-vao-notion-second-brain/SKILL.md`](../../packs/starter/ask-masonshare/skills/luu-vao-notion-second-brain/SKILL.md)

## When to reach for it

The user says "save to Notion", "lưu vào Notion", "turn on Notion", "write to my second brain" or "create a task in Notion". Other skills may point to it as a soft suggestion. It works with a workspace shaped like a ready-made second-brain template (notes, tasks, projects, goals, people, plans); it contains none of that template's content.

## Common questions

**Can it edit or delete my pages?** No. It only creates pages. Editing and deleting stay with you.

**Where are my database names stored?** In your own profile document, next to `brand-profile.md`, not in the skill.

**Is the Notion connection restricted by these rules?** No. They are rules the agent follows. Share only the three databases with the connection if you want a hard limit.

## It's working if

- Every page it creates carries your prefix and tag and links back in the report.
- Nothing existing was edited or deleted, and no goals, people or other databases were touched.
- No database name, link or ID appears inside the skill files.
