# Step 0: the platform-neutral spec

Fill in this spec before you open any app. It stays the same whichever app you choose, and it makes every later screen a copy-and-paste job. For a fuller template with a scorecard, see [profile-template.md](../../skills/bot-design/references/profile-template.md).

Give each bot one job. Write short answers. Leave a field blank when you do not know yet, and mark it "to decide".

## The spec

1. **Job.** What does this bot do, in 3 to 5 sentences? Finish with one sentence that starts "This bot does not...".
2. **User.** Who talks to the bot, and what do they already know?
3. **Inputs.** What does the bot receive each time (a goal, a file, a link, an event)? Where does it find missing facts?
4. **Outputs.** What does it hand back (a draft, a report, a file)? In what format? Who receives it next?
5. **Soul.** The standing instructions, kept short: role, tone, work loop (clarify, research, plan, build, verify), and where it must stop and ask. Put long procedures in skills, not in the soul.
6. **Skills.** One skill per repeatable procedure. For each: the trigger, the steps, and how you check the result.
7. **Memory.** A few starter facts worth remembering (preferences, naming rules, recurring context). Keep bulk data elsewhere.
8. **Access.** Which apps, folders and tools the bot may use. Start with the least it needs. Note which secrets are required, and store them in the app's secret store, never in the spec.
9. **Permissions.** Which actions run alone and which wait for your approval. Put an approval gate before anything hard to reverse: publishing, sending, deleting, spending, installing, giving write access, enabling a schedule.
10. **Routines.** What runs on a schedule or on an event. Write the schedule, the task, and the test you will run before switching it on.
11. **Model.** Which model tier fits the job: a stronger one for reasoning and design, a lighter one for routine checks. Note that some apps pick the model for you.

## Check before you build

- The job fits in one paragraph.
- Every output has a "done when" you can check.
- Every gate has a named action behind it.
- No secret appears in the spec.

## Next

Take the filled spec to [openmausbot.md](openmausbot.md) or [grok-bot.md](grok-bot.md). The table in [field-mapping.md](field-mapping.md) shows where each field goes.
