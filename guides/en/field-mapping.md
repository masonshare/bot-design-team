# Field mapping

Where each field of the [neutral spec](00-platform-neutral.md) goes in each app. "Chat" means you set it by telling the Bot in its chat, because a personal Grok Bot has no settings page.

| Spec field | OpenMausBot | Grok Bot |
|---|---|---|
| Name | Bot settings, Name (or **Set me up**) | **Create New Bot**, name |
| Job (role line) | Title and description | Label (called Title on phones); first message |
| User | Instructions text (part of the soul) | First message, in chat |
| Inputs | Instructions text; connected apps and working folder | First message; **Connect apps** |
| Outputs | Instructions text (format and recipient) | First message, in chat |
| Soul | Instructions field (up to 24 KB); stored as `SOUL.md` (source: product repo, unverified) | No field. Send it as the first message and ask the Bot to remember it |
| Skills | Bot profile, **Skills**: paste `SKILL.md` or import a folder, then switch on | Ask the Bot to save a skill, or **Teach a task**; enable per Bot under **Connect apps** > **Private skills**. `SKILL.md` support is not documented (unverified) |
| Memory | Memory: `MEMORY.md` plus topic notes, editable | Say "remember: ..." in chat; no memory screen |
| Access (apps, tools) | Connected apps: all tools, exact list, or none; MCP servers | **Connect apps**; **Add a custom connector** |
| Secrets | Vault references, credential cards | **Vault**, 1Password, secure secret card |
| Permissions | Access level, such as **Ask for approval** or Full access | **Settings > General > Bot**: **Auto Review**, **Custom Rules** (Allow automatically or Ask first) |
| Routines | Per-bot routines: once, interval, weekdays; test, then enable | Ask the Bot in chat; **Details** tab with Test and Pause |
| Model | Engine and model per bot, per thread and per routine | No picker; chosen automatically |
| Team and coordinator | Department, Chief of Staff (**Also in charge of**), **Bots it may talk to** | Primary Bot, group chats, Team Bots (Team or Enterprise plans) |
| Share | Import this repo through **Teams → Import** (unverified label); department packages | Template link: **Share** > **Create a copy** > **Publish** |

## What travels when you share

| | OpenMausBot import | Grok Bot template |
|---|---|---|
| Soul or instructions | Yes | Yes |
| Skills | Yes, `SKILL.md` text only, switched off | Yes, except private skills |
| Routines | Yes, paused | Yes |
| Memory | No (for repo import) | Docs disagree (unverified) |
| Models | No | Not applicable |
| Secrets and credentials | No | No |
| MCP servers | No | No |
