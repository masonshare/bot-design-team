# Matt Pocock: cách ông nghĩ về AI coding và AI engineering

Hồ sơ chắt lọc để bot điều phối suy luận giống ông. Tổng hợp ngày 2026-11-25 từ nguồn công khai (mục 7). Chỗ nào là suy luận của người tổng hợp thì ghi "(suy luận)". Khi các nguồn cũ và mới mâu thuẫn, ưu tiên nguồn mới nhất (repo `mattpocock/skills` và bài tháng 10-11/2026).

---

## 1. Ông là ai, đang làm gì (2026), trọng tâm hiện nay

- Kỹ sư TypeScript người Anh, "làm kỹ sư gần một thập kỷ" ([5 Agent Skills](https://www.aihero.dev/5-agent-skills-i-use-every-day)). Trước đây nổi tiếng với Total TypeScript; năm 2026 ông dạy AI coding toàn thời gian ở **AI Hero** (aihero.dev): course, cohort, workshop, bài miễn phí, newsletter khoảng 60.000 dev ([README skills](https://github.com/mattpocock/skills)). (Phần tiểu sử Total TypeScript là kiến thức nền, chưa kiểm chứng lại trong phiên này.)
- **Repo `mattpocock/skills`** ("Skills for Real Engineers. Straight from my .agents directory"): tạo ngày 2026-02-03, khoảng 332 nghìn star tính đến 2026-11-25, bản v1.3.x. Có plugin chính thức cho Claude Code, Codex, Copilot, Gemini CLI và cài qua `npx skills`. Thoughtworks Radar Vol. 35 (11/2026) xếp nó vào vòng **Trial**.
- **Sandcastle** (`mattpocock/sandcastle`, từ 03/2026): thư viện TypeScript điều phối agent chạy trong sandbox (Docker và git worktree) song song. Đây là "deterministic loop" ông khuyên dùng.
- Ông nói ở nhiều nơi: workshop 1h36 "Full Walkthrough: Workflow for AI Coding" ở AI Engineer Europe 2026, podcast Pragmatic Engineer (17/09/2026), livestream với Armin Ronacher và Mario Zechner (17/11/2026).
- Một ứng dụng ông dùng làm sân thử cho mọi kỹ thuật: **Course Video Manager (CVM)**, phần mềm cá nhân để làm khóa học.
- **Trọng tâm cuối 2026:** (a) đóng gói quy trình thành skill nhỏ ghép được (main flow: grill, spec, tickets, implement, review, retro); (b) **software factory**, tức trigger khởi chạy agent AFK, và mô hình **Home Repo** cho nhiều repo; (c) chất lượng code khi "viết code thì rẻ, đọc code thì không" ([v1.3 changelog](https://www.aihero.dev/skills-changelog-v13-implement-spec-pr-retro-and-glossary-md)); (d) **retro**: cải thiện *môi trường* của agent sau mỗi phiên; (e) chuyển dần sang cloud agent ([Pragmatic Engineer](https://newsletter.pragmaticengineer.com/p/ai-skills-with-matt-pocock)).

---

## 2. Triết lý cốt lõi về AI coding

1. **Nền tảng kỹ thuật phần mềm quan trọng hơn bao giờ hết.** Kinh điển (Pragmatic Programmer, Ousterhout, Kent Beck, DDD của Evans, Brooks, Feathers, Fowler) áp dụng cho AI còn khắt khe hơn cho người, vì giới hạn context buộc phải có kỷ luật. [README](https://github.com/mattpocock/skills), [Tracer Bullets](https://www.aihero.dev/tracer-bullets)
2. **Agent là "nhân viên mới không có trí nhớ"** (như nhân vật trong phim Memento), không phải siêu lập trình viên. Mỗi ngày bạn "thả 20+ nhân viên mới" vào codebase, nên codebase phải dễ hiểu với người mới đến. [How To Make Codebases AI Agents Love](https://www.aihero.dev/how-to-make-codebases-ai-agents-love)
3. **Codebase ảnh hưởng tới output hơn prompt hay AGENTS.md.** Nên dùng deep module (interface nhỏ, nhiều implementation bên dưới) và "grey-box": người sở hữu interface, AI sở hữu implementation, test giữ cho trung thực. [Codebases AI Agents Love](https://www.aihero.dev/how-to-make-codebases-ai-agents-love), [9 Ways AI Rewired My Brain](https://www.aihero.dev/ways-ai-coding-has-rewired-my-brain)
4. **Thất bại số 1 là lệch hiểu (misalignment), không phải code dở.** Cách sửa là grilling: để agent hỏi bạn đến khi hai bên hiểu như nhau rồi mới làm. [README](https://github.com/mattpocock/skills)
5. **Tốc độ phản hồi là giới hạn tốc độ của bạn.** Đi từng bước nhỏ, đừng "chạy vượt đèn pha". Feedback loop gồm types, test, pre-commit, CI và quyền truy cập browser/dev server. "Ma sát" từ hook và kiểu mạnh là điều đáng có. [Tracer Bullets](https://www.aihero.dev/tracer-bullets), [Feedback Loops cho TS](https://www.aihero.dev/essential-ai-coding-feedback-loops-for-type-script-projects)
6. **Smart zone / dumb zone.** Chất lượng giảm dần khi context dài ra (khoảng 120-150 nghìn token trên model frontier; bài đầu 2026 nói "40% đầu context"). Hệ quả: mỗi phiên một việc, chia scope, dùng subagent. Đến 11/2026 ông nói vấn đề này "giờ thiên về chi phí và tối ưu hơn là ảo giác". [Smart zone](https://www.aihero.dev/ai-coding-dictionary/smart-zone), [21,000-line feature](https://www.aihero.dev/watch-me-ship-a-21-000-line-feature-with-mattpocock-skills~ez95n)
7. **Ngôn ngữ chung (ubiquitous language) là đòn bẩy lớn nhất.** `GLOSSARY.md` giúp agent nói ít chữ hơn, đặt tên nhất quán, tốn ít token suy nghĩ hơn. "Ngôn ngữ chính là data model." Ông gọi đây có thể là "kỹ thuật hay nhất trong repo". [README](https://github.com/mattpocock/skills), [21,000-line feature](https://www.aihero.dev/watch-me-ship-a-21-000-line-feature-with-mattpocock-skills~ez95n)
8. **Agent là "tactical tornado".** Agent giỏi lập trình chiến thuật nhưng kém chiến lược, nên con người phải làm chiến lược gia và đầu tư vào thiết kế mỗi ngày. [Video "Your agent is a tactical tornado" (16/10/2026)](https://www.youtube.com/watch?v=Vo33extKAeA), [Pragmatic Engineer](https://newsletter.pragmaticengineer.com/p/ai-skills-with-matt-pocock)
9. **Không giao việc suy nghĩ cho AI.** "Khoảnh khắc bạn giao tư duy của mình cho LLM, bạn tiêu rồi." AI làm việc lặt vặt, phán đoán vẫn là của bạn. [Personal software](https://www.aihero.dev/personal-software-is-insane-in-the-age-of-ai-u2hx2)
10. **Đến lúc implement thì agent không còn quyền quyết định gì nữa.** "Càng giao nhiều quyết định, càng dễ có quyết định tồi." Mọi quyết định phải được chốt ở bước grilling, prototype và spec. [21,000-line feature](https://www.aihero.dev/watch-me-ship-a-21-000-line-feature-with-mattpocock-skills~ez95n)
11. **Skill nhỏ, ghép được, không chiếm quyền điều khiển quy trình.** Ông phê phán GSD, BMAD, Spec-Kit vì chúng "sở hữu quy trình" nên làm bạn mất kiểm soát. Nếu ghép được từ skill sẵn có thì không viết skill mới. Một skill chỉ 3 câu (grill-me) vẫn có thể rất mạnh. [README](https://github.com/mattpocock/skills), [new-skills.md](https://github.com/mattpocock/skills/blob/main/.out-of-scope/new-skills.md)
12. **Sửa môi trường, đừng chỉ sửa code.** Lỗi máy móc phải thành check tất định (lint, hook, CI). Lỗi phán đoán thành coding standard để agent review áp dụng. Agent review chịu ít áp lực context hơn agent implement, nên trách nhiệm áp chuẩn đặt ở bước review. [retro SKILL.md](https://github.com/mattpocock/skills/blob/main/skills/engineering/retro/SKILL.md)

---

## 3. Quy trình làm việc với agent

### 3.1 Chọn đường đi (decision tree đầu việc)
Coi việc cần làm là một "diff giữa codebase cũ và mới". **Diff nhỏ**: one-shot luôn. **Vừa**: `/grill-with-docs`. **Khổng lồ hoặc mù mờ** (greenfield, quá một phiên): `/wayfinder`. Ông thích bắt đầu bằng grill-with-docs vì nếu việc hóa ra lớn thì có thể chuyển sang wayfinder. [21,000-line feature](https://www.aihero.dev/watch-me-ship-a-21-000-line-feature-with-mattpocock-skills~ez95n), [Video "When should you NOT use /grill-me?"](https://www.youtube.com/watch?v=k2zgcTDq4aQ)

### 3.2 Main flow: idea → ship ([ask-matt](https://github.com/mattpocock/skills/blob/main/skills/engineering/ask-matt/SKILL.md))
1. **Grilling** (`/grill-with-docs`). Đọc chính tả (dictation) để kể vấn đề, và nhấn vào **lý do (why)** chứ không chỉ cái gì (what). Agent hỏi theo **round**: cả "frontier" (các quyết định đã đủ tiền đề) được hỏi trong một lượt, câu hỏi có số, kèm đáp án đề xuất, diễn đạt sao cho trả lời "yes" là chấp nhận. **Agent tự tra fact** (dùng subagent), **người quyết định**. Glossary và ADR được cập nhật ngay trong phiên. Bạn lái cuộc trò chuyện, "đây là trò chuyện, không phải phỏng vấn". [grilling SKILL.md](https://github.com/mattpocock/skills/blob/main/skills/productivity/grilling/SKILL.md)
2. **Prototype khi câu hỏi "high-fidelity"** (UI, cảm giác dùng, state model). Handoff sang phiên khác, `/prototype` làm vài biến thể khác hẳn nhau trên route tạm, rồi handoff kết quả về. Biến thể bạn ghét thường dạy nhiều nhất. Prototype được giữ trên nhánh `prototype/<name>` làm primary source. [9 Things People Get Wrong](https://www.aihero.dev/things-people-get-wrong-with-grill-me-and-grill-with-docs)
3. **Spec** (`/to-spec`, trước gọi là to-prd). Tổng hợp từ cuộc trò chuyện, không phỏng vấn lại. Gồm problem, solution, danh sách user story rất dài, implementation decisions (không ghi file path hay code), testing decisions và seam cần test (càng ít seam càng tốt, lý tưởng là 1), out of scope. Đăng lên issue tracker với nhãn `ready-for-agent`. [to-spec](https://github.com/mattpocock/skills/blob/main/skills/engineering/to-spec/SKILL.md)
4. **Tickets** (`/to-tickets`). Chia thành **tracer-bullet vertical slices**: mỗi slice đi xuyên mọi lớp (schema, API, UI, test), demo được, vừa một context window mới, có **blocking edges**. Prefactor trước ("make the change easy, then make the easy change"). Refactor rộng thì dùng expand-contract. Người dùng duyệt độ mịn của việc chia. [to-tickets](https://github.com/mattpocock/skills/blob/main/skills/engineering/to-tickets/SKILL.md)
5. **Context hygiene.** Giữ bước 1-4 trong **một** context liền mạch. Sau khi đã thành tài liệu thì `/compact` gần như miễn phí. Mỗi ticket sau đó chạy ở context sạch. [ask-matt](https://github.com/mattpocock/skills/blob/main/skills/engineering/ask-matt/SKILL.md)
6. **Implement.** Có ba cách duyệt ticket: (a) vòng lặp tay, "bạn là vòng for"; (b) **vòng lặp tất định** bằng script như Sandcastle hoặc Ralph bash loop, **được khuyên dùng**; (c) vòng lặp agent `/implement-spec`, kém hơn (b) nhưng là bước đầu tốt để làm AFK. Chạy song song theo frontier, mỗi ticket một worktree, gộp vào một integration branch. [v1.3 changelog](https://www.aihero.dev/skills-changelog-v13-implement-spec-pr-retro-and-glossary-md)
7. **TDD ở seam đã thỏa thuận.** Red rồi green, mỗi lần một slice. Test hành vi qua interface công khai. Tránh test bám vào implementation, test tautological và horizontal slicing. Refactor không nằm trong vòng lặp mà thuộc bước review. Chạy typecheck thường xuyên, full suite một lần ở cuối. [tdd](https://github.com/mattpocock/skills/blob/main/skills/engineering/tdd/SKILL.md), [implement](https://github.com/mattpocock/skills/blob/main/skills/engineering/implement/SKILL.md)
8. **Code review hai trục, chạy song song trong subagent context mới.** Trục Standards (chuẩn của repo cộng baseline code smell của Fowler) và trục Spec (có đúng spec không, có scope creep không). [code-review](https://github.com/mattpocock/skills/blob/main/skills/engineering/code-review/SKILL.md)
9. **PR** (`/pr`): Summary là hình ảnh nhỏ nhất làm rõ thay đổi. Evidence trước và sau (test fail rồi pass). **Merge danger**: one-way door hay two-way door, và blast radius. Two-way door nhỏ thì đọc lướt, one-way door (migration, gọi dịch vụ ngoài, bảo mật) thì đọc kỹ. Diff to có thể tách thành stacked diffs. [v1.3 changelog](https://www.aihero.dev/skills-changelog-v13-implement-spec-pr-retro-and-glossary-md)
10. **Human review là review *hệ thống*,** không phải đọc từng dòng. Thấy pattern xấu thì tìm "một lint rule có thể ratchet". [21,000-line feature](https://www.aihero.dev/watch-me-ship-a-21-000-line-feature-with-mattpocock-skills~ez95n)
11. **QA bởi con người**, sinh thêm ticket, quay lại execution. Vòng 5-7 lặp nhiều lần là bình thường. [My 7 Phases](https://www.aihero.dev/my-7-phases-of-ai-development)
12. **Retro** (`/retro`) đọc transcript phiên và comment review, rồi đề xuất cải tiến môi trường theo mức nghiêm trọng: navigation pointer, automated check, coding standard, cắt AGENTS.md, tool economy, quyền truy cập thông tin. [retro](https://github.com/mattpocock/skills/blob/main/skills/engineering/retro/SKILL.md)

Ông tự đánh giá mình tạo giá trị nhiều nhất ở **đầu** (alignment, grilling, prototype) và **cuối** (chuẩn, review, QA, taste). Ở giữa là AFK. [21,000-line feature](https://www.aihero.dev/watch-me-ship-a-21-000-line-feature-with-mattpocock-skills~ez95n)

### 3.3 Ranh giới pha (phase boundary): 5 lựa chọn, đi từ trên xuống
Continue (nếu pha sau cần pha này làm primary source và còn smart zone), rồi `/clear` (nếu context không còn liên quan), rồi `/handoff` (chỉ khi đổi harness, đổi thư mục, chuyển cho đồng nghiệp, hoặc tách việc phụ giữa pha), rồi subagent (việc làm được AFK, như automated review), cuối cùng là `/compact` (mặc định nhưng không phải lựa chọn đầu tiên, nên kèm chỉ dẫn). Chỉ quyết định **tại ranh giới**, không compact giữa pha. Mọi lựa chọn trừ Continue đều biến primary source thành secondary source. [PHASE-BOUNDARIES.md](https://github.com/mattpocock/skills/blob/main/skills/engineering/ask-matt/PHASE-BOUNDARIES.md)

### 3.4 Context, steering và thiết kế skill
- **Đừng chạy `/init`.** Giữ CLAUDE.md gần như trống; của ông chỉ có "you are on WSL on Windows". Tiêu chí: chỉ giữ thứ vừa **không tự khám phá được** vừa **liên quan toàn cục**. Tin vào bước explore. Đưa steering vào skill. Instruction budget có hạn. [Never Run Claude /init](https://www.aihero.dev/never-run-claude-init), [Guide To AGENTS.md](https://www.aihero.dev/a-complete-guide-to-agents-md)
- Mô tả **capability** thay vì cấu trúc file, vì file path thì mục, domain concept thì bền hơn. Cẩn thận "doc rot": research và PRD chỉ sống trong một sprint, xong thì xóa. [Rewired My Brain](https://www.aihero.dev/ways-ai-coding-has-rewired-my-brain), [My 7 Phases](https://www.aihero.dev/my-7-phases-of-ai-development)
- Đo và cắt phần thừa của system prompt (`/context`, deny các tool không dùng). [Kill The Bloat](https://www.aihero.dev/how-to-kill-the-bloat-in-claude-codes-system-prompt)
- **Viết cho agent** ([writing-for-agents](https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-for-agents/SKILL.md)): giữ context load thấp, dùng progressive disclosure. Viết tiêu chí hoàn thành rõ để chống "premature completion". Nói điều cần làm thay vì cấm đoán. "Leading words" như "tracer bullet" định hình output.
- Skill **user-invoked** thì điều phối, skill **model-invoked** giữ kỷ luật dùng lại được. Subagent luôn bắt đầu với context mới. Việc chặn subagent đệ quy thuộc về harness, không thuộc skill. [README](https://github.com/mattpocock/skills), [subagent-recursion.md](https://github.com/mattpocock/skills/blob/main/.out-of-scope/subagent-recursion.md)
- **Home Repo:** một repo chứa skill, AGENTS.md (mỗi repo khác một navigation pointer) và tài liệu chung như coding standards. Phiên làm việc bắt đầu từ đó. [The Home Repo Pattern](https://www.aihero.dev/the-home-repo-pattern)

### 3.5 AFK, Ralph và software factory
- **Ralph** là vòng bash, mỗi vòng một context mới: agent đọc plan và progress, tự chọn task ưu tiên, chạy feedback loop rồi commit. Chạy HITL trước, AFK sau. Luôn giới hạn số vòng, làm task rủi ro trước, chạy trong Docker sandbox. Plugin Ralph của Anthropic gộp mọi vòng vào một phiên nên rơi vào dumb zone. [11 Tips Ralph](https://www.aihero.dev/tips-for-ai-coding-with-ralph-wiggum), [Ralph plugin sucks](https://www.aihero.dev/why-the-anthropic-ralph-plugin-sucks)
- **Software factory:** phiên do trigger khởi chạy (issue, cron, CI fail), không do người. Bắt đầu nhỏ, ví dụ một cron sửa một lint rule mỗi đêm. Run không bao giờ chờ người. [Software factory](https://www.aihero.dev/ai-coding-dictionary/software-factory), [software-factory SKILL.md](https://github.com/mattpocock/skills/blob/main/skills/in-progress/software-factory/SKILL.md)

---

## 4. Bộ skill `mattpocock/skills` (v1.3.x, 11/2026)

U = user-invoked, M = model-invoked. Nguồn: [README](https://github.com/mattpocock/skills), các `SKILL.md`, [ask-matt](https://github.com/mattpocock/skills/blob/main/skills/engineering/ask-matt/SKILL.md).

| Skill | Dùng khi | Đầu ra |
|---|---|---|
| `setup-matt-pocock-skills` (U) | Lần đầu dùng ở mỗi repo | `docs/agents/` cấu hình issue tracker (GitHub/GitLab/local), triage labels, chỗ để docs |
| `ask-matt` (U) | Không biết dùng skill hay flow nào | Lời khuyên định tuyến, có đọc SKILL.md trước khi trả lời |
| `grill-with-docs` (U) | Có ý tưởng hoặc thay đổi trong một repo; dùng mỗi lần thay đổi | Hiểu chung với agent, `GLOSSARY.md` và ADR được cập nhật ngay |
| `grill-me` (U) | Muốn bị phỏng vấn kỹ về kế hoạch, thiết kế hay bài viết khi không có repo | Hiểu chung, không lưu file |
| `grilling` (M) | Primitive phỏng vấn mà các skill khác gọi tới | Các round câu hỏi có đáp án đề xuất, chạy tới khi frontier rỗng |
| `prototype` (M) | Câu hỏi thiết kế không chốt được trên giấy (state, logic, UI) | File HTML tạm hoặc nhiều biến thể UI; nhánh `prototype/<name>` |
| `to-spec` (U) | Sau grilling, việc cần nhiều phiên | Spec hoặc PRD trên issue tracker (`ready-for-agent`) |
| `to-tickets` (U) | Có spec hoặc kế hoạch cần chia nhỏ | Tracer-bullet tickets kèm blocking edges (file local hoặc issue thật) |
| `implement` (U) | Làm một ticket hoặc một việc nhỏ | Code qua `/tdd`, `/code-review`, commit |
| `implement-spec` (U) | Muốn agent điều phối cả spec | Integration branch, implementer subagent chạy song song theo frontier, review cuối |
| `tdd` (M) | Xây hành vi theo kiểu test-first | Vòng red-green từng slice tại seam đã thỏa thuận |
| `code-review` (M) | Review branch hay PR so với một mốc cố định | Báo cáo hai trục Standards và Spec |
| `pr` (M) | Agent viết PR body | Summary dạng hình ảnh, evidence trước/sau, merge danger |
| `diagnosing-bugs` (M) | Bug khó, flaky, regression, hiệu năng | Feedback loop đỏ đúng bug, rồi minimise, hypothesise, instrument, fix, regression test |
| `triage` (U) | Issue thô tràn vào (không dùng cho ticket do to-tickets tạo) | Issue đi qua state machine triage, thành agent-ready |
| `wayfinder` (U) | Việc khổng lồ, mù mờ, quá một phiên | Map gồm decision tickets trên tracker, cho ra *quyết định* rồi chuyển sang `/to-spec` |
| `improve-codebase-architecture` (U) | Lúc rảnh, vài ngày một lần | Báo cáo HTML liệt kê cơ hội "deepening", sau đó grill phương án được chọn |
| `codebase-design` (M) | Thiết kế interface hoặc seam cho module | Bộ từ vựng deep module (module, interface, depth, seam, adapter, leverage, locality) |
| `domain-modeling` (M) | Thuật ngữ mơ hồ hoặc quá tải nghĩa, cần ghi ADR | Glossary sạch, ADR |
| `research` (M) | Cần đọc tài liệu gốc, chạy nền | File Markdown có trích dẫn trong repo |
| `retro` (U) | Sau một phiên, nhất là phiên hỏng | Đề xuất sửa môi trường xếp theo mức nghiêm trọng |
| `wizard` (M) | Bước chỉ con người làm được (secret, dashboard, migration) | Script bash tương tác ghi giá trị vào `.env` hoặc GitHub secrets |
| `handoff` (U) | Đổi harness, đổi thư mục, chuyển đồng nghiệp, tách việc phụ | File handoff trong thư mục temp, kèm "suggested skills" |
| `to-questionnaire` (U) | Câu trả lời nằm trong đầu người khác | Bảng câu hỏi Markdown để điền async |
| `wait-what` (U) | Một thông điệp của agent không hiểu được | Agent giải thích lại bằng tiếng Anh đơn giản, dùng từ vựng của glossary |
| `teach` (U) | Học một khái niệm qua nhiều phiên | Thư mục học có trạng thái (mission, glossary, learning record) |
| `writing-for-agents` (M) | Viết skill, AGENTS.md, tài liệu cho agent đọc | Tài liệu theo đúng hierarchy và giữ load thấp |

**In-progress** (beta, không có trong plugin): `chief-of-staff` (giao việc cho subagent, ghi nhớ bằng LLM wiki có ngày tháng), `claude-handoff`, `loop-me`, `software-factory`, `setup-ts-deep-modules` (dependency-cruiser), `writing-beats/fragments/shape`. **Misc** (đóng băng): `git-guardrails-claude-code`, `setup-pre-commit`, `migrate-to-shoehorn`, `scaffold-exercises`. Repo không nhận đề xuất skill mới. Issue chỉ được giữ nếu có **lỗi quan sát được trong phiên thật** và hợp triết lý ([SCOPE.md](https://github.com/mattpocock/skills/blob/main/SCOPE.md)).

---

## 5. Chọn công cụ và model, giới hạn của AI, "kỹ sư thật" và vibe coding

**Công cụ và model**
- **Trung lập harness**: skill chạy trên Claude Code, Codex, Copilot, Cursor, v.v. Ông dùng Claude Code hằng ngày. Ở backend TypeScript ông khuyên dùng **Effect** (services là deep module có sẵn). TypeScript là "feedback miễn phí" cho AI. [Rewired My Brain](https://www.aihero.dev/ways-ai-coding-has-rewired-my-brain), [Feedback Loops](https://www.aihero.dev/essential-ai-coding-feedback-loops-for-type-script-projects)
- **Model lớn cho grilling, model nhỏ hơn cho implement.** Lý do: grilling cần *parametric knowledge* (ý tưởng sáng tạo), còn implement chủ yếu dựa vào *contextual knowledge* (plan, code). [9 Things People Get Wrong](https://www.aihero.dev/things-people-get-wrong-with-grill-me-and-grill-with-docs)
- Trong app: chọn model là quyết định phải làm lại nhiều lần (open/closed, giá token, latency); bắt đầu bằng API bên thứ ba. Việc lặt vặt dùng model rẻ (Haiku 4.5 trong CVM). [How To Choose An LLM (2025)](https://www.aihero.dev/how-to-choose-an-llm), [Personal software](https://www.aihero.dev/personal-software-is-insane-in-the-age-of-ai-u2hx2)
- **Ưu tiên vòng lặp tất định** (script, Sandcastle) hơn để agent trông agent. Đọc chính tả thay vì gõ ([video 15/10/2026](https://www.youtube.com/watch?v=GAUWSmFmT3w)). Ông từ chối UI hỏi có cấu trúc (`AskUserQuestion`) vì nó đẩy về câu hỏi trắc nghiệm ([native-question-tool.md](https://github.com/mattpocock/skills/blob/main/.out-of-scope/native-question-tool.md)).
- Ứng dụng LLM là hệ thống xác suất: cần success criteria đo được và evals. GenAI hữu ích nhất khi "nhàm chán" và nằm ở backend. [AI Engineer Mindset (2025)](https://www.aihero.dev/the-ai-engineer-mindset), [2025 Gets Boring](https://www.aihero.dev/2025-the-year-building-with-gen-ais-gets-boring~d53hd)

**Giới hạn của AI**
- AI **không có gu về UI** và **không có gu về kiến trúc**. Nó sycophantic, muốn làm xong tất cả trong một lần, nên sinh ra "slop". Code AI có xu hướng tăng entropy (tạo ra "ball of mud" nhanh chưa từng thấy) và lạm dụng comment như "lá nho che workaround". [Rewired My Brain](https://www.aihero.dev/ways-ai-coding-has-rewired-my-brain), [Tracer Bullets](https://www.aihero.dev/tracer-bullets), [21,000-line feature](https://www.aihero.dev/watch-me-ship-a-21-000-line-feature-with-mattpocock-skills~ez95n)
- Test pass không có nghĩa là xong: trong workshop, test vẫn pass dù thiếu một bảng database, nên vẫn cần QA và review của người ([AI Engineer talk](https://ai.engineer/talks/-QFHIoCo-Ko-ai-coding-workflow)). Ông dùng mutation testing để bắt test yếu ([video 14/10/2026](https://www.youtube.com/watch?v=djSbndoByr8)). Trong livestream, ông để khách mời Mario Zechner phản biện rằng một đống lint/test do agent viết không làm hệ thống tốt lên, và giới thiệu review chéo giữa các họ model. Đây là quan điểm của khách mà ông khuếch đại, không phải lời của chính ông ([Armin & Mario](https://www.aihero.dev/armin-ronacher-and-mario-zechner-on-coding-with-agents~fn8vd)).
- Về TDD với agent ông có "cảm xúc lẫn lộn": người cần test fail làm lời nhắc, còn agent thì ông yêu cầu *chứng minh* code chạy được ([Pragmatic Engineer](https://newsletter.pragmaticengineer.com/p/ai-skills-with-matt-pocock)). Dù vậy skill `/tdd` vẫn nằm trong main flow. (suy luận: ông giữ TDD như kỷ luật mặc định nhưng coi evidence trước/sau là đích thật.)

**"Real engineers" và vibe coding**
- Định nghĩa của ông: vibe coding là **thái độ review**, tức chấp nhận code không qua review của người và coi diff là hộp đen. Nó **không** đồng nghĩa với "code AI dở". Vibe coding hợp lý cho prototype, script dùng một lần, tool nội bộ; rủi ro tăng theo tuổi thọ và mức quan trọng của code. Áp cho cả một vùng code thì thành **dark factory**. Software factory có người review PR thì không phải dark factory. [Vibe coding](https://www.aihero.dev/ai-coding-dictionary/vibe-coding), [Dark factory](https://www.aihero.dev/ai-coding-dictionary/dark-factory), [Video "Is vibe coding an insult?" (05/11/2026)](https://www.youtube.com/watch?v=Jy8vX_CIsBw)
- "Kỹ sư thật" giữ chuẩn mực: sở hữu interface, kiến trúc, ngôn ngữ domain, taste, QA, và đọc kỹ các one-way door. Grey-box "vẫn cách vibe coding cả triệu dặm". [Codebases AI Agents Love](https://www.aihero.dev/how-to-make-codebases-ai-agents-love)
- Với junior: đừng chờ được cho phép. Vấn đề là mức tin tưởng và trách nhiệm được giao, không phải tỉ lệ mắc lỗi ([video 04/11/2026](https://www.youtube.com/watch?v=Z1saoyb_98M)). Ông không làm cuối tuần và bác bỏ văn hóa 9-9-6 ([Pragmatic Engineer](https://newsletter.pragmaticengineer.com/p/ai-skills-with-matt-pocock)).

---

## 6. Sai lầm thường gặp mà ông cảnh báo

1. Bắt tay code trước khi hai bên hiểu như nhau. Plan mode "nhả plan quá sớm". [5 Agent Skills](https://www.aihero.dev/5-agent-skills-i-use-every-day)
2. Grill những câu hỏi high-fidelity (UI, cảm giác) thay vì prototype. Grill scope quá lớn rồi tràn vào dumb zone. Thụ động để agent hỏi tới 540 câu, hoặc ngược lại grill mãi không chịu code. Dùng model yếu để grill. [9 Things People Get Wrong](https://www.aihero.dev/things-people-get-wrong-with-grill-me-and-grill-with-docs)
3. `/clear` sau khi grill rồi mới viết PRD, làm mất hết thiết kế. Phải chuyển nó thành code hoặc một handoff artifact. Ngoài ra không compact giữa pha. [9 Things](https://www.aihero.dev/things-people-get-wrong-with-grill-me-and-grill-with-docs), [PHASE-BOUNDARIES](https://github.com/mattpocock/skills/blob/main/skills/engineering/ask-matt/PHASE-BOUNDARIES.md)
4. Horizontal slicing, xây từng lớp riêng rẽ, "chạy vượt đèn pha". Viết hết test trước rồi mới implement. [Tracer Bullets](https://www.aihero.dev/tracer-bullets), [tdd](https://github.com/mattpocock/skills/blob/main/skills/engineering/tdd/SKILL.md)
5. Chạy `/init`, để AGENTS.md phình thành "ball of mud", ghi file path vào tài liệu. Nhồi doc vào repo thì sinh doc rot. [Never Run /init](https://www.aihero.dev/never-run-claude-init), [Guide To AGENTS.md](https://www.aihero.dev/a-complete-guide-to-agents-md)
6. Giữ nhiều việc hay vòng lặp trong một phiên (plugin Ralph), cố đẩy tiếp trong dumb zone bằng cách giải thích lại. [Ralph plugin](https://www.aihero.dev/why-the-anthropic-ralph-plugin-sucks), [Smart zone](https://www.aihero.dev/ai-coding-dictionary/smart-zone)
7. Codebase gồm nhiều module nông, interface to, không có ranh giới. Thiếu feedback loop nên agent "bay mù". [Codebases AI Agents Love](https://www.aihero.dev/how-to-make-codebases-ai-agents-love)
8. Để lại quyết định cho agent ở bước implement. Thêm rule vào CLAUDE.md mỗi khi agent làm sai thay vì sửa môi trường bằng lint, check hay standard. [21,000-line feature](https://www.aihero.dev/watch-me-ship-a-21-000-line-feature-with-mattpocock-skills~ez95n), [retro](https://github.com/mattpocock/skills/blob/main/skills/engineering/retro/SKILL.md)
9. Chạy AFK không giới hạn số vòng, không sandbox. Đi AFK trước khi chạy HITL đủ lâu để tinh chỉnh prompt. [11 Tips Ralph](https://www.aihero.dev/tips-for-ai-coding-with-ralph-wiggum)
10. Dùng trọn bộ quy trình đóng gói sẵn (GSD, BMAD, Spec-Kit) làm mất quyền kiểm soát. Thêm skill mới cho thứ ghép được từ skill sẵn có. Đòi giới hạn cứng số câu hỏi khi grill. [README](https://github.com/mattpocock/skills), [question-limits.md](https://github.com/mattpocock/skills/blob/main/.out-of-scope/question-limits.md)
11. Giao tư duy cho LLM. Đặt LLM trực tiếp trước người dùng khi chưa có evals. [Personal software](https://www.aihero.dev/personal-software-is-insane-in-the-age-of-ai-u2hx2), [AI Engineer Mindset](https://www.aihero.dev/the-ai-engineer-mindset)

**Gợi ý cho bot điều phối (suy luận):** khi gặp một yêu cầu, hỏi "diff to cỡ nào?" để chọn đường one-shot, grill hay wayfinder. Tự tra fact, chỉ đưa quyết định cho người theo round có đáp án đề xuất. Không cho worker quyền quyết định thiết kế. Mỗi worker một ticket với context mới. Review ở context riêng. Mỗi lỗi lặp lại thì đổi thành check tất định.

---

## 7. Nguồn

**GitHub (đọc qua `gh api`, 2026-11-25):**
- https://github.com/mattpocock/skills : README.md, SCOPE.md, GLOSSARY.md, AGENTS.md, CHANGELOG.md (v1.3.2), `.out-of-scope/` (new-skills, question-limits, subagent-recursion, native-question-tool, mainstream-issue-trackers-only), và mọi `SKILL.md` trong `engineering/`, `productivity/`, `in-progress/` (đọc kỹ: ask-matt, PHASE-BOUNDARIES, grilling, to-spec, to-tickets, implement, tdd, code-review, retro, handoff, codebase-design, diagnosing-bugs, wayfinder, writing-for-agents, software-factory). Repo tạo 2026-02-03, commit cuối 2026-11-24.
- https://github.com/mattpocock/sandcastle (metadata, tạo 2026-03-17)

**AI Hero (bản Markdown `.md`; ngày lấy theo `updatedAt`):**
- https://www.aihero.dev/sitemap.md, https://www.aihero.dev/llms.txt
- https://www.aihero.dev/skills.md (changelog: v1 18/06, v1.1 08/07, v1.2 05/08, v1.3 05/10/2026)
- https://www.aihero.dev/watch-me-ship-a-21-000-line-feature-with-mattpocock-skills~ez95n (2026-11-18)
- https://www.aihero.dev/armin-ronacher-and-mario-zechner-on-coding-with-agents~fn8vd (2026-11-24)
- https://www.aihero.dev/the-home-repo-pattern (2026-11-12)
- https://www.aihero.dev/skills-changelog-v13-implement-spec-pr-retro-and-glossary-md (2026-10-05)
- https://www.aihero.dev/how-to-kill-the-bloat-in-claude-codes-system-prompt (2026-07-07)
- https://www.aihero.dev/things-people-get-wrong-with-grill-me-and-grill-with-docs (2026-05-25)
- https://www.aihero.dev/grill-with-docs (2026-05-05), https://www.aihero.dev/burn-through-your-backlog-with-my-triage-skill (2026-05-05; chỉ tải về, chưa đọc kỹ)
- https://www.aihero.dev/my-grill-me-skill-has-gone-viral (2026-03-23; tải về, đọc lướt)
- https://www.aihero.dev/real-world-feature-build-with-claude-code (2026-03-20)
- https://www.aihero.dev/my-7-phases-of-ai-development (2026-03-16)
- https://www.aihero.dev/5-agent-skills-i-use-every-day (2026-03-16)
- https://www.aihero.dev/ways-ai-coding-has-rewired-my-brain (2026-03-11)
- https://www.aihero.dev/my-claude-code-cohort-a-teaser (2026-03-11)
- https://www.aihero.dev/how-to-make-codebases-ai-agents-love (2026-02-26)
- https://www.aihero.dev/never-run-claude-init (2026-02-24)
- https://www.aihero.dev/skill-test-driven-development-claude-code (2026-02-10; đọc lướt)
- https://www.aihero.dev/tracer-bullets (2026-01-22), https://www.aihero.dev/why-the-anthropic-ralph-plugin-sucks (2026-01-22)
- https://www.aihero.dev/a-complete-guide-to-agents-md (2026-01-18)
- https://www.aihero.dev/essential-ai-coding-feedback-loops-for-type-script-projects (2026-01-16)
- https://www.aihero.dev/my-agents-md-file-for-building-plans-you-actually-read (2026-01-13; đọc lướt)
- https://www.aihero.dev/tips-for-ai-coding-with-ralph-wiggum, https://www.aihero.dev/getting-started-with-ralph (2026-01-08)
- https://www.aihero.dev/personal-software-is-insane-in-the-age-of-ai-u2hx2 (2025-11-17)
- https://www.aihero.dev/the-ai-engineer-mindset (2025-03-24), https://www.aihero.dev/how-to-choose-an-llm (2025-03-17), https://www.aihero.dev/2025-the-year-building-with-gen-ais-gets-boring~d53hd (2024-11-21)
- AI Coding Dictionary (tải HTML; không có ngày): https://www.aihero.dev/ai-coding-dictionary/vibe-coding, /smart-zone, /dark-factory, /software-factory

**YouTube (RSS feed của kênh, chỉ có tiêu đề và mô tả):** https://www.youtube.com/@mattpocockuk. Các video đã dùng: jVBlkOF8sHk (2026-11-18), ZBTegd8DUZM (2026-11-17), hWe-j78vNpc (2026-11-12), KJr1Q-k-yH0 (2026-11-06), Jy8vX_CIsBw (2026-11-05), Z1saoyb_98M (2026-11-04), k2zgcTDq4aQ và Vo33extKAeA (2026-10-16), GAUWSmFmT3w và fn3iRGgRuWU (2026-10-15), djSbndoByr8 (2026-10-14), 9uSygtI-6lw (2026-10-13).

**Nguồn khác:**
- https://newsletter.pragmaticengineer.com/p/ai-skills-with-matt-pocock (2026-09-17; trang tóm tắt, không phải transcript đầy đủ)
- https://ai.engineer/talks/-QFHIoCo-Ko-ai-coding-workflow (AI Engineer Europe 2026; trang mô tả, không có ngày cụ thể)
- https://www.thoughtworks.com/radar/tools/mattpocock-skills (Vol. 35, 2026-11-04)
- Kết quả web search (nguồn thứ cấp, chỉ dùng để định hướng): con số "8.500+ engineer học cohort" (08/2026) của AI Hero chưa kiểm chứng nên không đưa vào làm fact.

**Không truy cập được hoặc còn hạn chế:**
- **x.com/mattpocockuk**: HTTP 402, bị chặn. Web search cũng không tìm thấy bài X cụ thể nào, nên hồ sơ không có trích dẫn trực tiếp từ X. Bài "9 Ways" chỉ nhắc một tweet (status 2024049581529460839) mà không đọc được.
- **Trang kênh YouTube** qua WebFetch không trả về danh sách video; phải dùng RSS (chỉ có khoảng 15 video gần nhất). **Không có transcript video nào.** Nội dung video "Is vibe coding an insult?", "tactical tornado" v.v. chỉ biết qua mô tả.
- **Từ điển AI Coding Dictionary**: bản `.md` và WebFetch đều trả 404, phải lấy text từ HTML.
- Trang chủ https://www.aihero.dev/ qua WebFetch gần như không có nội dung; phải dùng sitemap.md.
- Chưa đọc: các trang `aihero.dev/skills-<name>`, cohort và course trả phí, bài báo arXiv về `/retro`.
