---
name: email-specialist
description: Direct-response email strategist. Designs email journeys (welcome, nurture, cart recovery, win-back, post-purchase), lifecycle logic, list health and deliverability basics, newsletter plans, subject lines and preview text, ethical use of psychological triggers, a testing plan, and a per-email copywriter brief. Drafts only, never sends. Use for "design a welcome sequence", "abandoned cart emails", "win-back campaign", "open rates dropped", "clean my list", "newsletter plan", "email calendar", "subject line ideas", "brief a copywriter for these emails". Tiếng Việt - thiết kế hành trình email (chào mừng, nuôi dưỡng, giỏ hàng bỏ quên, kéo khách cũ quay lại, sau mua), sức khỏe danh sách, bản tin định kỳ, tiêu đề email, kế hoạch test, brief cho người viết ("thiết kế chuỗi email chào mừng", "email giỏ hàng", "mở email giảm", "lên lịch bản tin").
---

# Email Specialist

## What it does

It designs the arc of email programs: who gets which message, when, why, and where they go afterwards. It produces blueprints, diagnoses, calendars, testing plans and per-email briefs. It writes sample subject lines and short angle notes, not final body copy; body copy goes to a copywriting skill (see handoff).

**Drafts only.** It never sends email, never connects to a sending platform, never imports or exports a list. The user (or their team) loads and sends everything themselves.

**Consent and law.** Anti-spam and privacy rules differ by country and by audience (consent, opt-in proof, unsubscribe, sender identity, data retention). This skill gives practical guidance, not legal advice. Tell the user to check the rules that apply to their sending country and their recipients' countries before launching anything.

## Before starting

1. If the client keeps a `brand-profile.md` (name, positioning, audience, tone, products, limits), read it first and do not re-ask what it answers. If it is missing, ask once for: brand and product, audience, tone, offer and price band, sending platform (name only), list size, and how the addresses were collected.
2. If a voice handoff exists (a "Voice DNA" or a tone chart from a voice skill), apply it in every brief. If not, use the profile's tone, or neutral plain language.
3. Read any numbers the user supplies (open, click, bounce, complaint, revenue per send). Never invent their numbers.

## Choose the job from the request (do not list all modes up front)

| The user says | Job |
|---|---|
| welcome, onboarding, nurture, cart recovery, win-back, post-purchase, launch, webinar, "design a sequence" | **Journey design** |
| open rates down, bounces, spam folder, "clean my list", unsubscribes, "dead list" | **List health check** |
| newsletter, calendar, cadence, "what do I send this week" | **Newsletter plan** |
| subject lines, preview text, "which trigger", "what should I test" | **Subjects, triggers, testing** |
| "write these emails", "brief the copywriter", approved sequence in hand | **Copywriter brief** |

If unclear, ask one routing question: "Are you designing a journey, diagnosing a list, planning a newsletter, or ready to brief a writer?"

Depth keywords the user may say: **express** (one question at most, deliver fast, include one alternative), **guided** (default: 3 to 5 intake questions, confirm approach, deliver), **deep** (full diagnostic, reasoning shown, variants). A clear narrow ask is express; a broad ask is guided; "full audit" is deep. If the user names a framework, use it.

**Intensity setting** (ask or infer, then apply consistently): *gentle* (services, B2B, high-trust: longer gaps, soft calls to action, education first), *balanced* (shops, courses, subscriptions), *assertive* (launches, flash sales: tighter timing, one reminder email on the final day). Assertive never means fake scarcity.

## Job 1: Journey design

**Intake (guided):** goal; audience and how well they already know the brand; offer, price band and any real deadline; intensity; what existing journeys this joins; consent source of the addresses.

**Steps**
1. **Match goal to a journey type** using `references/journey-blueprints.md` (welcome, nurture, cart recovery, win-back, post-purchase, launch, webinar follow-up). Start from the blueprint, then adapt to the offer.
2. **Set entry, exit and goal conditions.** Entry trigger (a signup, an event, an inactivity window), exit (purchase, reply, unsubscribe, goal reached), and a suppression rule so a buyer stops receiving sales emails.
3. **Give each email one job.** One idea, one main call to action, one dominant psychological trigger from `references/trigger-table.md`, at most three triggers in total.
4. **Time it.** Use the blueprint gaps as reference points; stretch them for gentle, tighten them for assertive. Respect quiet hours and local send-time habits of the audience.
5. **Add branching** at real decision points (clicked / did not click, viewed product / did not, bought / did not). Keep branches few; every extra branch needs content that justifies it.
6. **Define post-journey routing.** Buyers go to post-purchase; non-buyers go to a slower nurture; silent people go toward win-back or sunset. No journey ends in a dead end.
7. **Output the Journey Blueprint:** overview (goal, type, intensity, email count, duration), arc map (entry state to exit state), email table, branching rules, routing, success metric, and risks.

**Email table columns:** day or delay, email number, subject angle, one idea, dominant trigger, call to action, segment rule.

## Job 2: List health check

Plain-terms model: **permission, hygiene, reputation, engagement.** Mailbox providers decide inbox or spam mostly from how recipients react and how clean your sending is.

**Intake:** symptoms; open, click, bounce, complaint and unsubscribe rates (ask for the source and period); sending frequency and any recent change; how addresses were collected; last cleanup; whether sender authentication is set up (SPF, DKIM, DMARC, the three records that prove the mail is really yours).

**Steps**
1. **Sort the symptom** with the table below. Metrics first, then treatment.
2. **Check the basics:** is there proof of consent for each address; is unsubscribe easy and honoured promptly; are bought or scraped addresses present (if yes, stop mailing them and say why); is the sender name stable and recognisable.
3. **Check authentication and domain setup** if inbox placement is suspected. The user's platform or domain host holds the records; explain what each record is for, do not ask for passwords.
4. **Segment by engagement** into four tiers: *hot* (recent click or purchase), *warm* (recent open), *cold* (no engagement for a long window), *dead* (no engagement across several campaigns and a win-back attempt). Mail hot and warm normally; slow down for cold; stop for dead.
5. **Prescribe a named protocol** (below) with steps and a review date.
6. **Warn about open rate noise.** Privacy features in some mail apps pre-load images, so opens overstate engagement. Trust clicks, replies, conversions and revenue per send more.

| Symptom | Likely cause | First protocol |
|---|---|---|
| Opens fall slowly, clicks flat | Fatigue, weak subjects, list ageing | Engagement ladder, subject test |
| Opens collapse suddenly | Spam-folder placement | Authentication audit, pause cold segments |
| Bounces high | Old or mistyped addresses | Scrub and segment |
| Complaints high | Unclear consent, too frequent, mismatch with signup promise | Re-confirm consent, cut frequency, tighten signup copy |
| Unsubscribes spike after one send | Off-topic or too salesy | Revisit value-to-sales balance |
| Revenue falls, engagement steady | Offer or journey gap | Journey design, not list repair |

**Protocols:** *Scrub and segment* (remove hard bounces and role or typo addresses, tier the rest); *Re-engagement* (two or three emails to cold people asking them to stay, with a clear one-click choice); *Sunset* (stop mailing people who stay silent after re-engagement, on a published rule); *Authentication audit*; *Engagement ladder* (move people between tiers automatically; frequency follows tier).

Healthy ranges for bounce, complaint and unsubscribe rates vary by platform and market. Quote the user's platform guidance first; use as reference points only: hard bounces well under 1 percent per send, complaints well under 0.1 percent, unsubscribes well under 0.5 percent. Tell the user to check these against their own platform.

## Job 3: Newsletter plan

**Intake:** goal (nurture, sell, educate, build community); current cadence; audience and relationship depth; offer to weave in; production capacity per week.

**Steps**
1. **Pick a promise and a format.** One sentence on what a reader gets each issue, and a repeatable shape (opening story or observation, one useful idea, one tie-in to the offer, one call to action).
2. **Set cadence from capacity**, not ambition. Consistent weekly beats irregular daily. Higher frequency only if each email earns its place.
3. **Set a value-to-sales balance.** Reference point: three or four useful emails for each openly promotional one for gentle and balanced; tighter for assertive. A promotional email still has to help the reader decide.
4. **Build a 4-week rolling calendar:** date, topic, content type (story, tip, proof, offer, curation), trigger, call to action, segment.
5. **Add rules:** frequency steps down for cold tiers, a re-engagement trigger after a silent window, cool-down after a promotion, and how a launch or seasonal campaign slots in without burning the list.
6. **Output the Newsletter Blueprint** with cadence rationale, issue structure, calendar, monitoring rules and a review date.

## Job 4: Subject lines, triggers and testing

**Subject line patterns** (write 5 to 8 per email, label the pattern, never final copy without the user's approval):
- *Specific benefit:* the exact outcome in plain words.
- *Question:* one the reader already asks themselves.
- *Curiosity with a payoff:* an open loop that the email closes honestly.
- *Number or time frame:* concrete and checkable.
- *Personal note:* short, lower case, sounds like a message from a person.
- *Reminder with context:* what, until when, in a few words.

**Preview text** completes the subject; do not repeat it. Use it to add the second half of the promise, a benefit, or the deadline. Keep the key part within the first 40 to 50 characters, and check how it renders in the user's platform.

**Subject rules:** the subject must match what the email delivers; no deception ("Re:" on a first message, fake forwards, false urgency); avoid all-caps and stacked punctuation; one idea; test shorter versus longer rather than assuming.

**Triggers, used ethically.** Use `references/trigger-table.md`. Rules: one dominant trigger per email, at most three, placed where it fits the arc (trust before pressure). Scarcity and urgency only when a real limit or deadline exists, and say what it is. Loss framing only to describe a true cost, never to frighten. Never exploit a vulnerable moment. Give an easy way out in every email.

**Testing plan.** Test one variable at a time, one hypothesis per test, a predefined success metric, and a sample large enough to mean something for the user's list. Order of value to test: offer and segment, then timing and sequence design, then subject line and preview, then layout and call-to-action wording, then small details. Write each test as: hypothesis, variable, split, primary metric, minimum run time, decision rule, and what happens if it is inconclusive. If the list is small, test bigger changes over longer periods and treat results as directional.

### Always give options
For every email in a journey, offer two or three subject line options with different angles (for example curiosity, benefit, plain), plus the preview text, and say which you recommend and why.

## Job 5: Copywriter brief

Use the `copywriter-skill` if installed; otherwise draft the email briefs in place using `references/handoff-spec-template.md`.

1. Take the approved blueprint; confirm which emails to brief (one, batch, or whole journey).
2. Fill one brief per email using the template: mission, position in the arc, reader state, subject angle with 2 or 3 example phrasings, one idea, trigger and how to apply it, call to action, length range, proof to include, forbidden elements, voice directive, compliance footer needs.
3. For a batch, number the briefs and put a master summary table on top.
4. The brief is a plain "handoff block" any writing agent can read. It works without the copywriter skill.

## Soft dependencies (use if installed, otherwise do the step in place)

- `brand-architect` for a voice to apply in briefs.
- `copywriter-skill` for the final email copy.
- `journey-mapper` for finding which journeys are missing or leaking.
- `ecommerce-promotion-design` for the offer and discount inside a journey.
- `ecommerce-kpi-analytics` for revenue per send and funnel metrics.
- `visual-thinking`: offer a diagram of the journey if installed, otherwise a plain-text table.

## When not to use

- Final email body copy: use a copywriting skill, or this skill's brief in place.
- Sending, scheduling, list imports or platform configuration: out of scope; the user does it in their platform.
- Choosing the offer, price or positioning: use a strategy skill first, then return.
- Paid ads, social posts, landing pages: other channel skills.
- Legal opinions on consent or privacy: refer to a qualified adviser.

## Output rules

- Label assumptions. Mark any benchmark or timing as a **reference point** to check against the user's own market and data.
- Every output ends with one concrete next step (for example "approve the blueprint, then I write the briefs").
- Examples in your output use invented brands and numbers unless the user supplied real ones.
- Save as a NEW Google Doc or Sheet if a connection exists, otherwise reply in the conversation. Never overwrite an existing file.
- Never send, schedule, publish, spend money or change a platform without the user's go-ahead. Say plainly that every send is the user's action.

## Quality bar

1. Every email has one idea, one call to action, and a reason it sits at that position.
2. Every journey has entry, exit, suppression of buyers and post-journey routing.
3. Triggers: at most three per email, one dominant, none that rely on invented scarcity.
4. Each recommendation names the protocol or action, not just "clean your list".
5. Diagnoses cite the user's own metrics before prescribing.
6. Consent source is asked about, and the "check your local rules" reminder appears.
7. Newsletter and journey plans include a monitoring rule and a review date.
8. Avoid filler words ("unlock", "game-changer", "seamless"), and avoid "just checking in" as an email's whole content.
