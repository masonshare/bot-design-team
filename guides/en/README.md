# Guides: set up your bots

This folder helps you turn the three bots of this repo into working bots, in OpenMausBot or in Grok Bot. The Vietnamese edition is in `../vi/`.

## Which guide to read when

| You want to... | Read |
|---|---|
| Design a bot before touching any app | [00-platform-neutral.md](00-platform-neutral.md) |
| Set up the 3 bots in OpenMausBot, fast or by hand | [openmausbot.md](openmausbot.md) |
| Set up a bot in Grok Bot | [grok-bot.md](grok-bot.md) |
| See which spec field goes where in each app | [field-mapping.md](field-mapping.md) |

Suggested order: fill in the neutral spec first, then follow the guide for your app, then check the mapping table.

## Install the skills

The three skills (`prompt-design`, `skill-design`, `bot-design`) install with the `skills` command line tool. Run these in a terminal.

Install all three skills into the current project:

```
npx skills add masonshare/bot-design-team
```

Install one skill only:

```
npx skills add masonshare/bot-design-team --skill prompt-design
```

Install globally, for every project on your computer, by adding `-g`:

```
npx skills add masonshare/bot-design-team -g
npx skills add masonshare/bot-design-team --skill prompt-design -g
```

Each skill works alone, so you can install only the one you need.

Which tool receives the skills depends on the agents the command detects on your computer. Run `npx skills add --help` to see the options. These commands target coding agents. For OpenMausBot and Grok Bot, use the paths in the app guides below.

## Safety note

Never paste passwords, API keys or tokens into a bot chat, a skill or a soul. Use the secret store of your app: Vault in both OpenMausBot and Grok Bot.

## Notes on accuracy

Steps marked "(unverified)" come from documentation that was not tested in the live app, or from sources that disagree. Check the label on screen before you rely on it.
