# How Orca loads skills and shares bots

Research for issue #16 (T6), parent spec #14. Version inspected: Orca 1.4.271 on Windows 11. All claims carry an evidence tag. Evidence was read from the installed app's code and its CLI help, plus public docs. No chats, tokens or user data were read.

Evidence tags:

- **[CODE]** read from Orca's own shipped code (`resources/app.asar`, files under `out/shared/...`, `out/cli/...`).
- **[CLI]** output of `orca ... --help`, `orca skills ...`, `orca skills get`.
- **[DOCS]** public docs at orca.dev.
- **[SESSION]** observed in this Claude Code session.

## Public docs say very little

`orca.dev/docs/bots` and `orca.dev/docs/bots/security` [DOCS] say only that a bot "lives in a folder on one computer" and that its soul, memory and abilities "are plain files in its folder". They do not name skill directories and do not mention share links. Everything below about layout and sharing therefore rests on [CODE] and [CLI]. Orca can change it in any release.

## 1. Bot-home skills

A bot's home is a folder holding `SOUL.md`, `MEMORY.md`, `memory/<topic>.md`, optional `avatar.png`, and `skills/`.

- A bot's own skills live at `skills/<name>/SKILL.md` in the bot home. [CODE: `shared/bots/bot-package.js`, `BOT_OWN_SKILLS_FOLDER = 'skills'`]
- Orca's own rule text given to every bot says: "Your own skills go in skills/<name>/SKILL.md in your home, never in .claude/skills or .agents/skills: when a chat starts, Orca links each one for every agent you can run on." [CODE: bot rules in the main bundle]
- The per-agent targets inside a bot home are `.claude/skills` (Claude) and `.agents/skills` (every other agent). Orca creates these links itself. [CODE: `BOT_AGENT_SKILLS_FOLDERS`]
- A bot's import guide also notes that "an older bot may also have some in `.claude/skills/` or `.agents/skills/`". [CLI: `orca skills get orca-cli --reference bot-import`]
- Skill names must be lowercase letters, digits and dashes (they become folder names). [CODE: `validateSkillPackageName`]
- A skill folder may hold other files next to `SKILL.md`. Shared bots carry them as `skills/<name>/<path>`. Limits: 512 files and 32 MiB per skill package, 64 skills per bot. [CODE]

## 2. Project skills (a repo's own skills)

Orca's skill discovery scans these roots in a repo, for every repo added to Orca and for the current directory. [CODE: discovery table in the main chunk, source kind `repo`]

| Root inside the repo | Read by |
|---|---|
| `.agents/skills` | all agents (the shared root) |
| `.claude/skills` | Claude Code |
| `.codex/skills`, `.cursor/skills`, `.github/skills`, `.qoder/skills`, `.opencode/skills` | the named agent |
| `.factory/skills`, `.continue/skills`, `.trae/skills`, `.grok/skills`, ... | the named agent (from the install-provider table) |

Facts that matter for this repo:

- **A top-level `skills/` folder is NOT scanned.** This repo keeps skills at `skills/<name>/`. Orca will not see them as project skills until they are installed or linked into `.agents/skills` (or `.claude/skills`). [CODE: the root list above has no bare `skills/`]
- `SKILL.md` must sit at most 5 directory levels deep under a root (plugins: 10). [CODE: `skill-discovery-depth.js`]
- `SKILL.md` front matter uses simple `name:` and `description:` keys. [CODE: `skill-metadata.js`]
- Global (home) roots are also read: `~/.agents/skills`, `~/.codex/skills`, `~/.claude/skills`, and more. [CODE]
- `npx skills add <repo>` (the community skills CLI) installs into `.agents/skills` for a project, or `~/.agents/skills` with `-g`, and links agent-specific folders such as `.claude/skills` to it. Orca's own installer does the same. [CODE: `.agents/skills` canonical root with per-agent roots] This is how the README's `npx skills add masonshare/bot-design-team` works.
- A bot can be linked to project folders ("skill projects"). For agents that read the linked folders, Orca prepares them at chat start. For agents that do not (grok, antigravity, cursor, hermes, kimi, kiro, goose and others), the bot gets a text list of skills instead. [CODE: `bot-skill-projects.js`, `resolveSessionLinkedSkills`]
- A skill that a linked project links in from outside the project is shared only if the owner ticks it in the share dialog. [CODE: `bot-share-skill-picks.js`]

### How this very session loads skills [SESSION]

`~/.claude/skills/<name>` entries are links to `~/.agents/skills/<name>` (`ls -l` shows `->`). Claude Code reads `~/.claude/skills`. `~/.agents/skills` is the canonical store. This matches Orca's model: one canonical `.agents/skills`, per-agent folders link to it. The `orca-cli` skill itself is a stub that loads its guide from the `orca` binary (`orca skills get orca-cli`), so guides are version-matched to the app. [CLI]

## 3. The bot share link

A bot is published from the bot's Share dialog. The link is a share id that resolves on `app.orca.dev`, `share.orca.dev` or `share.onorca.dev`, in the forms `orca://bots/share/<id>` or `https://<host>/bots/share/<id>`. [CODE: `skill-share-link.js`] The dialog says: "Anyone with the link can make a copy." The owner can republish to the same link ("Goes to the same link. Copies already made stay as they are.") or remove it ("The link stops working."). A link can expire and need re-preparing. [CODE: renderer strings; `BOT_SHARE_ERRORS` has expired and prepare-again codes]

What the package contains [CODE: `BotPackageV1Schema`, `botPackagePartOf`]:

| Part | Shared as |
|---|---|
| Manifest | `dev.orca.bot-sharing/bot.json` (schemaVersion 1) |
| Soul | `SOUL.md` |
| Avatar | `avatar.png` or a mascot id |
| Skills | `skills/<name>/...`, the owner ticks which |
| Memory | `memory/<topic>.md`, only if the owner ticks it |
| Tools (MCP) | URL and header names only, never header values. The recipient ticks each one |
| Connectors | kind only (github, slack, linear, google, composio) |
| Schedules | prompt, rrule, timezone, result kind. Arrive disabled |
| Event suggestions | trigger definitions, not enabled |
| Setup note | up to 2000 characters, shown to the recipient as untrusted text |
| Purpose, agent hint | up to 200 characters; the sharer's agent is only a hint, the recipient picks their own |

What is not shared: connector sign-ins, secrets, chats, memory beyond what is ticked, and the channels and issues that results go to (the recipient picks). The Share dialog scans for secrets and blocks publishing until they are removed ("Remove the secret to publish"). [CODE: renderer strings]

On the recipient side, the link opens a review dialog showing each part and flagged lines. Creating the bot writes `SOUL.md`, `memory/...` and `skills/<name>/...` into a new bot home and then the normal home-skill linking applies. [CODE: `planBotFromPackage`, `bot-share-review-files.js`]

`orca skills share --skill <name> --bundle-name "<Name>"` is a separate feature for plain skills: it publishes selected installed skills behind one unlisted link. It needs the default-off setting Settings, Share Skills. Only discovered skill directories can be selected. [CLI]

## 4. What this means for T2 (skills layout)

1. Keep `skills/<name>/SKILL.md` as the authored source, one folder per skill, names lowercase-dash, flat. Do not rely on a bare top-level `skills/` being discovered by Orca.
2. Provide an install path so Orca and agents see them: `npx skills add masonshare/bot-design-team` (already documented) installs into `.agents/skills`. For work inside this repo itself, a link or copy into `.agents/skills` is needed. Decide the exact mechanism after owner step V1.
3. Keep each skill self-contained: everything it needs in its own folder, at most 5 levels under the root, under 512 files and 32 MiB.
4. Use only `name:` and `description:` front matter keys with simple values.
5. Skills must work for any agent: no Claude-only paths, since Staff bots run on Codex.

## 5. What this means for T7 (pack layout)

1. The pack is delivered by the bot share link (the bot package), not by repo scanning. A pack therefore needs: a SOUL.md, a skill list (each `skills/<name>/`), optional `memory/<topic>.md`, a short setup note, and connectors by kind (`google`).
2. Put the pack's skills in the bot's `skills/<name>/` form. Do not tell anyone to place them in `.claude/skills` or `.agents/skills` inside a bot home. Orca links them.
3. Real data never goes in the package (the link is "anyone with the link"). Sheet IDs, prices and chats stay in the owner's Google account. Use fake data only.
4. Staff bot (read-only, Codex): keep it a separate shared bot from the Editor bot. The agent field is a hint, so the pilot staff member confirms Codex on their machine.
5. Schedules and event suggestions arrive disabled. Do not make a pack depend on a schedule being on.
6. Keep the setup note short and treat it as untrusted text (no instructions the bot must obey).
7. For project-level use (without a bot), the repo needs skills in `.agents/skills` (see T2).

## 6. Unverified items and exact owner steps

The agent cannot drive the Orca UI or use the owner's account. These were verified from code only and need an owner check.

| # | Unverified | Owner steps |
|---|---|---|
| V1 | A repo's top-level `skills/` is not discovered by Orca as project skills. | In Orca add this repo as a project. Open the Skills page and look for the repo's skills. Report whether any appear. Then run `npx skills add masonshare/bot-design-team --skill prompt-design` inside a test project and confirm they now appear under `.agents/skills`. |
| V2 | Orca links bot-home `skills/<name>/` into `.claude/skills` and `.agents/skills` at chat start, including on Windows. | Create a test bot. Put `skills/hello/SKILL.md` (name `hello`, any description) in its home folder. Start a new chat. Ask the bot "which skills do you have?". Then list `.agents\skills` and `.claude\skills` in the bot home. Report whether `hello` is listed and whether the entries are links, junctions or copies. |
| V3 | The share link contents match section 3 and secrets are blocked. | In the test bot's Share dialog, tick a skill, skip memory, publish. Copy the link. Open it on a second Orca (or the same one, new bot) and read the review dialog. Report the parts shown and whether any real path, token or header value appears. Then put a fake secret such as `sk-test-0000` in SOUL.md and confirm publishing is blocked. |
| V4 | Link lifetime and recipient needs. | Report whether the link needs an Orca account for the recipient, whether it expires (and after how long), and whether republishing keeps the same link. Test with a second machine or user. |
| V5 | A Staff bot created from a link runs on the recipient's Codex. | On a pilot staff machine, open the link, choose Codex, start a chat, and ask it to use a skill. Report the result. |
| V6 | Orca may differ after 1.4.271. | Run `orca --version` and report it, so the doc can be dated to the version tested. |

## Reproducing the evidence

```
orca --version
orca skills share --help
orca skills get orca-cli --references
orca skills get orca-cli --reference bot-import
npx @electron/asar extract "%LOCALAPPDATA%\Programs\Orca\resources\app.asar" <empty-dir>
# then read out/shared/bots/bot-package.js, out/shared/skills/**, out/shared/bots/bot-share-*.js
```
