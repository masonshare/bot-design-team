# Set up a bot in Grok Bot

This guide covers xAI's Grok Bot app (docs: https://docs.x.ai/grok-bot). It is not the Grok chat app and not the Grok Build command line tool. Everything below comes from the official docs. Labels were read from the docs, not tested in the app, so confirm them on screen.

Before you start, fill in [the neutral spec](00-platform-neutral.md).

## What to expect

- A personal Bot has no settings page. You configure it by telling it what to do in chat.
- There is no instructions box. The first message you send takes that role.
- There is no model picker. Grok Bot picks the model for each task.
- A repo link cannot be installed. No documented command or link imports a GitHub repo into Grok Bot, so you paste text into chat instead.

## Steps

1. **Install and sign in.** Install from x.ai/bot and sign in with a Cursor account. Check your plan on the get-started page of the docs.
2. **Create the Bot.** Click **+** at the top of the sidebar (or press `Ctrl/Cmd+N`). On a team, **+** opens a menu: choose **Create a Bot**. In **Create New Bot**, enter a name, pick a shape and colour, then choose **Create**.
3. **Send the first message.** Give the Bot one job, its sources, and where it must ask before acting. Ask it to remember all of this. Build the message from your spec: job, user, inputs, outputs, and the gates. Paste the bot's soul from `bots/` here (pasting the soul as the first message is the documented chat route).
4. **Add skills.** Ask the Bot in chat to save a procedure as a skill, and paste the procedure text. Or use **Teach a task**: open a one-to-one chat, open the computer view, choose **Teach a task**, describe the result, do it once, stop, then review the draft. Whether Grok Bot reads a pasted `SKILL.md` file as a skill is not documented (unverified). Skills you save are private and shared by all your Bots. Enable them per Bot from **Connect apps**, the connected count, then **Private skills**.
5. **Connect apps.** Open **Connect apps**, search, add, then **Authorize**. Type `@` in a task to use an app. For a custom MCP server, choose **Add a custom connector** and fill in Name and Type (**Remote HTTPS** or **Command**).
6. **Keep secrets out of chat.** Use **Vault** (Settings > Vault), 1Password, or the secure secret card the Bot shows. Never paste a key into a message.
7. **Set permissions.** Go to **Settings > General > Bot**. **Auto Review** is on by default. Under **Custom Rules**, write "When Grok Bot wants to:" and "It should:" with **Allow automatically** or **Ask first**, then **Add Rule**. Ask first wins when rules overlap. Approval cards offer Allow once, Always allow, Deny.
8. **Add memory.** Tell the Bot "remember: ...". There is no memory screen. Ask the Bot to show, correct or forget a memory when you need to.
9. **Add routines last.** Ask the Bot in chat to create the routine. Open the Bot name, then the **Details** tab, to Pause, Resume, Test, Edit or Delete. New routines wait for their next time. **Test** runs at once and does real work, so test only with a safe task. Check the time zone under **Settings > Bot > Timezone**.
10. **Teams (optional).** Choose a primary Bot, which coordinates the others, and use group chats. Team Bots need a Team or Enterprise plan. The official limit on Bots per group chat was not found (unverified).

## Share what you built

Bot details > **Share** > **Create a copy** > **Publish** > **Copy link** makes a template. A template carries instructions, skills, first-party plugins and routines. It leaves out personal memories, private skills, secrets, scripts and MCP servers; the docs disagree on whether memories travel (unverified). Whoever imports it opens the link, chooses **Add to Grok Bot**, reviews, then **Add Bot**, and must re-add secrets and MCP servers.

## Check it works

- Ask the Bot to repeat its job and its approval rules back to you.
- Run each routine once with **Test** before you leave it enabled.

## Related

[field-mapping.md](field-mapping.md) lines up each spec field with OpenMausBot and Grok Bot.
