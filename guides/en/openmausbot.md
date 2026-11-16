# Set up the bots in OpenMausBot

Two ways. Path A takes minutes. Path B gives you full control and works for any bot, not only the three in this repo.

Before either path, fill in [the neutral spec](00-platform-neutral.md).

## Where the souls live

The three bots (Pink Pepper Coated Lotus Seeds, Mango Spring Roll, Dried Plum) are defined in `team.md` at the root of this repo. Each bot has its own entry there with its role and its soul, which is its standing instructions. The same souls sit as plain files in `bots/` (Vietnamese reading copies in `bots/vi/`). OpenMausBot stores them in the bot's Instructions field.

## Path A: import the repo (fast)

OpenMausBot looks for `botmrr.md` or `team.md` at the root of the repo, on the `main` or `master` branch. This repo has `team.md`.

1. Open **Teams → Import**. The label differs between OpenMausBot sources; one calls it **Templates → Import** (unverified). Use whichever your version shows.
2. Paste the repo link: `https://github.com/masonshare/bot-design-team`.
3. Read the review screen, then confirm. The import creates the 3 bots, their souls, their skills (switched off) and their routines (paused).
4. Open each bot's profile, go to **Skills**, and switch on the skills you want.
5. Pick a model for each bot. Import does not carry models, so each bot starts on your default. Use a stronger model for design work and a lighter one for light checks.
6. Check the access level. Imported bots start at Full access. Choose **Ask for approval** if you want risky actions to wait for you.
7. Leave routines paused until you have tested each one (see Path B, step 9).

What the import does not carry: models, credentials, memory, connected-app access, and a skill's `references/` and `scripts/` folders. Only the `SKILL.md` text arrives. The skills in this repo are written to work from `SKILL.md` alone. If you want the optional `references/` files too, bring the skill folder in from this computer: **Bot profile → Skills**, import a folder (unverified; the docs describe the route but not the button label).

Add your own memory notes and connect your own apps afterwards.

## Path B: create each bot by hand

Repeat for each of the three bots.

1. **Create the bot.** In the sidebar choose **New or share** (or `Ctrl/Cmd+N`), then **New bot**. It appears at once with a unique name and the default AI. Under the greeting, **Set me up** lets you describe the job in one sentence.
2. **Open Bot settings** and fill in this order. The docs list the items but not the on-screen order, so this order is a recommendation (unverified layout).
   1. Name.
   2. Title and description: the role line from your spec.
   3. Avatar and colour.
   4. Instructions: open this bot's file in `bots/` (`prompt-designer.md`, `skill-designer.md` or `bot-architect.md`), copy it all, paste it here. The limit is 24 KB.
   5. Engine and model. Advanced mode lists models; Simple mode uses the default AI.
   6. Working folder (optional).
   7. Computer. Local control is off by default.
3. **Set the access level.** New bots start at Full access. Choose **Ask for approval** while you test.
4. **Seed memory.** Memory is on by default. Add your starter notes to `MEMORY.md`.
5. **Add skills.** Open the bot's profile, then **Skills**. Paste the `SKILL.md` text from `skills/<name>/SKILL.md` or import the folder. Imported skills arrive switched off, so switch each one on.
6. **Connect apps.** Grant each service one of: all tools, an exact list of tools, or none. Choose the narrowest option that works.
7. **Store secrets in Vault.** Use a Vault reference or a credential card. Never paste a key into chat or a skill.
8. **Team settings (optional).** Put the three bots in one department. Make Dried Plum the Chief of Staff with **Also in charge of**. Use **Bots it may talk to** to let them hand work to each other.
9. **Add routines last.** Choose once, interval or weekdays. Keep each routine paused. Run it once by hand, read the result, then enable it. A routine can use its own model, such as a lighter one.

Tip: **App settings → General → Defaults for new bots → Edit** sets defaults for future bots. It does not change existing ones.

## Check it works

- Send each bot one request from your spec and compare the result with your "done when".
- Ask the bot to show its skill list and its instructions; confirm they match what you pasted.
- Confirm no routine is enabled that you have not tested.

## Related

- [field-mapping.md](field-mapping.md) shows each spec field and its place in OpenMausBot.
- Coming from Grok Bot: **Settings → Import & export → Move from Grok Bot** carries a Bot's profile, instructions, skills and paused routines (verified in the OpenMausBot docs).
