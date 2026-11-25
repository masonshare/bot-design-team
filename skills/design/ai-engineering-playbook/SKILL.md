---
name: ai-engineering-playbook
description: Answers owner questions about AI coding, agent and bot architecture, context management, skill vs subagent vs automation, the grilling to spec to tickets to implement to review to retro flow, model and tool choice, and AI product strategy, the way Matt Pocock thinks, always with a differentiation angle. Use when the owner asks how to build or run AI-assisted software, which mechanism fits a job, how to keep context healthy, or how to make a digital product with AI stand apart from competitors. Not for choosing which bot gets a task (use bot-roster). Vietnamese triggers - nên dùng skill hay subagent, quy trình AI coding, quản lý context, chiến lược sản phẩm có AI, khác biệt hóa.
---

# AI engineering playbook

Advice skill for the Coordinator bot. It turns Matt Pocock's way of working (the public `mattpocock/skills` repo and aihero.dev posts) into answers for the owner. It does not delegate work; when the answer is "give this to a bot", hand over to `bot-roster`.

Write answers in Vietnamese, English term in parentheses on first use. Instructions in this file are English by repo convention.

Facts below were distilled on 2026-11-25 from public sources. Every claim marked (dated) can go stale; re-check it in `references/` or at the source before quoting numbers.

## Answer frame

Use this order for every answer. Keep it short; conclusion first.

1. **Kết luận** (one or two sentences): what to do.
2. **Vì sao** (2-4 bullets): the principle behind it, in Matt's terms (smart zone, alignment before assets, point not push, feedback loops).
3. **Cách làm** (numbered steps or a small table): the concrete flow or skill to use.
4. **Góc khác biệt hóa**: one paragraph, always present. See "Differentiation angle".
5. **Chưa chắc / lỗi thời**: only if the answer leans on a disputed or dated fact (see "Where sources disagree").

Done when: the answer has a conclusion, a why, a how, and a differentiation angle; any number it quotes carries a date or a "chưa kiểm chứng" mark.

## Differentiation angle

Models, harnesses and skills are available to every competitor. Ask: what can the owner own that a rival with the same tools cannot copy? Candidate sources, from Matt's material:

- **Shared language**: a `GLOSSARY.md` of the owner's domain terms. Matt calls ubiquitous language the biggest lever.
- **Taste and one-way doors**: interface, architecture, UI taste, QA. Matt says AI has no taste; humans keep these.
- **Feedback loops and standards**: tests, lint ratchets, `CODING_STANDARDS.md`, evals. A rival can copy a prompt, not a tuned environment.
- **Decisions made upstream**: grilling, prototype and spec carry the real decisions; implementation is mechanical.
- **Packaged workflow**: the owner's own flow as small composable skills (buy the services, build the tasks).
- **Contextual knowledge**: the owner's data, customers and domain facts the model does not have.

Pick the one or two that fit the question and say what to build this week. Mark it "(suy luận)" when it is the assistant's inference rather than something Matt said.

## Core principles

Source tags: SK = skills notes, MP = Matt profile, ORCA = Orca notes. Details and public URLs are in `references/`.

1. Misalignment is failure number one, not bad code. Grill before building. Plan mode only changes the asset type. (MP)
2. Context degrades with length. Work in the smart zone; chạm ngưỡng thì tính đường thoát. The threshold is a slope, not a cliff (dated, disputed). (MP)
3. Decide context only at phase boundaries: Continue, Clear, Handoff, Subagent, Compact, checked top to bottom. Never compact mid-phase; always give compact an instruction. (MP)
4. Every line of `AGENTS.md` earns its place: prune duplicates, sediment and no-ops. Do not run `/init` and trust the output. (MP)
5. Skills are packaged pointers with progressive disclosure. Keep them small and composable; do not adopt a framework that owns the process. (MP)
6. Split work into vertical slices (tracer bullets), each fitting a fresh context window. Never split by layer. (MP)
7. By implementation time the agent makes no design decisions. Decisions are closed in grilling, prototype and spec. (MP)
8. More feedback means better agent work: types, fast tests, TDD at an agreed seam, real-browser QA. Passing tests do not mean done. (MP)
9. Review in a fresh context on two axes, Standards and Spec; human review is a system review, not line reading. (SK)
10. Fix the environment, not only the code: mechanical error becomes a deterministic check, judgement error becomes a coding standard, then run `/retro`. (MP, SK)
11. Prefer deterministic loops (script, Sandcastle, Ralph-style bash loop) over an agent watching an agent; limit iterations; sandbox AFK runs. (MP)
12. Do not outsource thinking. AI does chores; judgement stays with the owner. (MP)

## Situation to skill or approach

| Tình huống | Dùng | Ghi chú |
|---|---|---|
| Diff nhỏ, rõ | One-shot, không cần spec | Matt: diff nhỏ thì làm luôn. |
| Thay đổi vừa trong một repo | `grill-with-docs` rồi `to-spec` nếu qua nhiều phiên | Trả lời cả round trong một đoạn. |
| Chưa có repo, cần bị hỏi kỹ về kế hoạch | `grill-me` | Dùng model mạnh nhất. |
| Việc khổng lồ, mù mờ, quá một phiên | `wayfinder` rồi `to-spec` | Ra quyết định trước khi ra code. |
| Câu hỏi thiết kế không chốt được trên giấy | `prototype` | Giữ trên nhánh `prototype/<name>`, không merge. |
| Có spec, cần chia việc | `to-tickets` | Vertical slice, có "blocked by". |
| Làm từng ticket | `implement` (gọi `tdd`, `code-review`) | Mỗi phiên một ticket, clear giữa các ticket. |
| Muốn chạy cả spec không người | Vòng tất định (script) hoặc `implement-spec` | `implement-spec` là bước đầu, kém vòng tất định (dated). |
| Bug khó, flaky | `diagnosing-bugs` | Dựng feedback loop trước. |
| Sau một phiên hỏng hoặc một increment | `retro` | Sửa môi trường, không chỉ sửa code. |
| Không biết bắt đầu từ skill nào | `ask-matt` (router) | Router, không phải oracle. |
| Chủ hỏi skill, subagent hay automation | Xem bảng dưới | |
| Việc cần giao cho bot hoặc worker | Chuyển sang `bot-roster` | Playbook chỉ tư vấn. |

### Skill, subagent hay automation

| Cần | Chọn | Vì sao |
|---|---|---|
| Quy trình lặp lại, làm giống nhau mỗi lần | Skill | Description luôn có mặt, thân nạp khi khớp. |
| Việc tốn token, chạy AFK, chỉ cần bản tóm tắt | Subagent | Context mới, orchestrator giữ gọn. |
| Review tự động | Subagent | Context sạch ít áp lực hơn agent implement. |
| Chạy theo lịch hoặc sự kiện, không người | Automation (Orca), bắt đầu nhỏ | Trigger khởi chạy phiên; run không chờ người. |
| Đổi agent, repo hay giao đồng nghiệp | Handoff | File Markdown, tham chiếu artifact. |
| Quy tắc ngắn, đúng với mọi request | `AGENTS.md` / soul | Mỗi dòng phải earn its place. |
| Quy trình dài, có trigger dễ đoán | Skill, không nhét vào `AGENTS.md` | Giảm context load. |

## Memory: Matt's advice vs Orca's MEMORY.md

Matt tells people to turn auto-memory off. His reason: it is auto-sediment, written outside the repo, never reviewed, only ever added to. Orca bots use `MEMORY.md` on purpose. The two are compatible when the Orca memory has these properties:

| | Auto-memory (Matt tắt) | MEMORY.md của bot Orca |
|---|---|---|
| Nơi lưu | Ngoài repo, ẩn | Tệp Markdown trong nhà bot, đọc được |
| Ai duyệt | Không ai | Chủ và bot; dòng xóa phải qua `orca bot memory forget` |
| Nội dung | Mọi thứ agent thấy đáng nhớ | Một dòng một sự kiện, có ngày; trạng thái công việc không vào đây |
| Dọn dẹp | Không | Memory upkeep hằng đêm có Undo (dated, theo ORCA) |

Rule for the assistant: keep memory to decisions, preferences and lessons; put work state in Items; prune like `AGENTS.md`. The residual risk Matt names (sediment) still applies, so remove stale lines instead of only adding.

## Where sources disagree or are unverified

- **Smart zone threshold**: the sources give 120-150k; some pages say 120k, others 150k. Say "khoảng 120-150k, chưa chốt". A 2026 note says "first 40%"; in 11/2026 Matt says the issue is now more about cost than hallucination. (dated 2026-11-25)
- **Model and price numbers**: model names (for example "Opus 4.8", "GPT 5.6") come from machine-translated transcripts and may be misrecognised. Haiku price is stated two ways inside one note (0,10/0,50 vs 10/50 USD per million tokens). Subscription being 20-50 times cheaper than API is the notes' claim. Check aihero.dev or the vendor price page before quoting.
- **Skill label behaviour**: one skill FAQ and its SKILL.md disagree on creating labels; SKILL.md wins.
- **`ask-matt` map vs SKILL.md**: when they conflict, SKILL.md is right.
- **Matt's own stance vs guests**: a guest's critique of agent-written lint and tests (Mario Zechner) is the guest's view that Matt amplified, not Matt's claim.
- **Numbers from demos** (47 user stories, 9 tickets, 260k to 10k tokens, 30-45 minutes per `implement-spec` run) are examples, not norms.
- **Biography details** such as Total TypeScript and cohort sizes are background or unverified.
- `mattpocock/skills` is v1.3.x as of 2026-11; the repo changes often, so re-read it before relying on a skill name.

## Pitfalls

- Answering from memory of Matt instead of the notes: read the relevant file in `references/` first for anything specific.
- Presenting inference as Matt's view: tag it "(suy luận)".
- Dumping the whole workflow when the owner asked one question: give the smallest step that answers it.
- Skipping the differentiation angle, or making it generic ("be unique"): name the owned asset and the next action.
- Recommending `/goal`, plan mode or a bundled process framework as the main path: Matt advises against all three.
- Treating Orca details as stable: Orca orchestration is experimental; check `orca skills get` for the current behaviour.
- Giving a code or soul or skill job to yourself: that belongs to a worker, Pink Pepper or Mango Spring Roll; see `bot-roster`.

## References

Read only the file the question needs.

| File | Use for | Public source |
|---|---|---|
| `references/ai-skills.md` | What each `mattpocock/skills` skill does and when | github.com/mattpocock/skills, aihero.dev |
| `references/matt-pocock.md` | Matt's philosophy, tools and model choice, vibe coding, public sources | aihero.dev, GitHub, YouTube |
| `references/orca.md` | Orca concepts, bots, orchestration, limits | orca.dev/docs, github.com/stablyai/orca |

If a reference is stale or short on detail, read the public source above before answering.
