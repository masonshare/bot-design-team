# AI Skills for Real Engineers: bản chưng cất

Nguồn: repo công khai `mattpocock/skills` (snapshot `abeeaf9`, 19/11/2026; các phần có thể ở bản v1.2.3 đến v1.3.2), bài và video trên aihero.dev. Tệp này được tổng hợp ngày 25/11/2026. Chỗ nào ghi "(suy luận)" là phần người tổng hợp tự rút ra, không có trong nguồn.

## 1. Tóm tắt 10 dòng

1. Đây là một hệ thống skill thực dụng giúp kỹ sư dùng coding agent mà không phải hạ chuẩn. Có 9 nhóm: Getting Started, Main Flow, Shaping, Engineering, Productivity, Reference, Misc, In-progress và Archived.
2. Main Flow: `grill-with-docs → to-spec → to-tickets → implement (bên trong chạy tdd) → code-review → retro`.
3. Con người giữ hai đầu: alignment ở đầu (WHY, glossary, prototype) và taste/standards ở cuối (review, retro, lint). Đoạn giữa chạy AFK.
4. Grilling là primitive phỏng vấn. Mỗi round hỏi toàn bộ frontier của design tree, mỗi câu có kèm khuyến nghị. Fact thì agent tự tra, decision thì người quyết.
5. Ngôn ngữ domain (ubiquitous language) được ghi ngay vào `GLOSSARY.md`, trước đây tên là `CONTEXT.md`. Chỉ viết ADR khi quyết định khó đảo ngược, gây bất ngờ nếu thiếu ngữ cảnh, và là một đánh đổi thật.
6. Spec tồn tại vì context window sẽ kết thúc. Ticket là tracer bullet (vertical slice), có blocking edge, và mỗi ticket vừa một fresh context window.
7. Test viết ở seam đã thống nhất trước, qua public interface. Không tautological, không horizontal slicing.
8. Context hygiene: smart zone khoảng 120–150k token. Chỉ chọn Continue, `/clear`, `/handoff`, subagent hoặc `/compact` tại phase boundary.
9. Review tách hai trục, Standards và Spec, không gộp thành một kết luận. Retro biến lỗi lặp lại thành check tự động trước, rồi mới đến standards và docs.
10. Viết cho agent theo hướng "delete, don't explain": dùng context pointer, progressive disclosure, leading word, và săn no-op. Model-invoked hay user-invoked là lựa chọn giữa context load và cognitive load.

## 2. Nguyên tắc

1. **Plan trước, build sau. Không mở lại plan khi đang implement.** Vì sao: implement chỉ dựng việc đã chốt, còn một agent được bảo "build this" sẽ tự redesign. *(/implement, /ask-matt)*
2. **Mỗi round hỏi trọn frontier, mỗi câu có khuyến nghị, trả lời "yes" nghĩa là chấp nhận khuyến nghị.** Vì sao: câu trong cùng round độc lập nhau, nên không câu nào bị một câu khác làm mất hiệu lực. Ví dụ 13 câu chỉ cần khoảng 3 round. *(/grilling)*
3. **Fact là việc của agent, decision là việc của người.** Vì sao: agent tự trả lời decision là làm hỏng phiên grilling, và một phiên không có người trả lời chỉ còn là ý kiến của agent. *(/grilling, /wayfinder)*
4. **Ghi glossary ngay lúc chốt term, không dồn đến cuối phiên.** Vì sao: phần ghi inline mới là output thật. Glossary chỉ chứa từ vựng (term là gì, kèm `_Avoid_`), không chứa spec hay chi tiết hiện thực. *(/domain-modeling, /grill-with-docs)*
5. **ADR phải qua đủ ba cửa: khó đảo ngược, gây bất ngờ, là đánh đổi thật.** Vì sao: phần lớn phiên không sinh ADR nào là đúng thiết kế. Tinh thần là Chesterton's Fence: đừng gỡ thứ mình chưa hiểu vì sao nó có. *(video 21k dòng)*
6. **Spec chỉ ghi quyết định đã có. Mọi điều spec khẳng định mà bạn chưa từng nói là bug.** Vì sao: spec là bản ghi sống lâu hơn context window. Ticket thì dùng xong bỏ, còn lý do nằm trong spec. *(/to-spec)*
7. **Cắt ticket theo tracer bullet, không theo layer.** Vì sao: horizontal slice không ship được gì cho đến khi mọi layer xong. Ví dụ: 26 ticket cắt theo layer cho khoảng 20 turn trên mỗi ticket, khoảng ¾ trong đó là rework. *(/to-tickets)*
8. **Thống nhất seam trước, và càng ít seam càng tốt (lý tưởng là một).** Vì sao: tdd chỉ chạy ở seam đã thống nhất, code-review đối chiếu diff với spec. Không ai chốt seam thì cả lượt chạy âm thầm biến thành "cứ viết code". *(/tdd)*
9. **Interface là test surface. Depth thuộc về interface, không thuộc implementation.** Vì sao: test xuyên qua interface sẽ gãy khi refactor. Deletion test: xoá module đi mà complexity dồn lại một chỗ thì module đó xứng đáng tồn tại. *(/codebase-design)*
10. **Một adapter là seam giả định, hai adapter mới là seam thật.** Vì sao: chỉ thêm port khi thực sự có thứ thay đổi qua seam đó.
11. **Không có feedback loop thì không được lý thuyết hoá.** Vì sao: có đúng loop là bug đã sửa được 90%. Loop deterministic 2 giây là "siêu năng lực", còn loop 30 giây chập chờn gần như vô dụng. *(/diagnosing-bugs)*
12. **Review hai trục tách biệt, mỗi trục một subagent với fresh context.** Vì sao: nếu gộp, trục đạt sẽ che trục trượt. Để cùng context tự review mình là "confirmation bias with a slash command". *(/code-review)*
13. **Lỗi máy kiểm được thì làm deterministic check. Chỉ phán đoán mới ghi vào CODING_STANDARDS.** Vì sao: repo chưa có lint/CI là "standing missed opportunity". Reviewer có ít context pressure nhất nên là người thực thi standards. *(/retro)*
14. **CLAUDE.md/AGENTS.md dùng "incredibly sparingly", chủ yếu cho navigation pointer.** Vì sao: thứ dùng ở 1/10 ngữ cảnh vẫn tốn context load ở 9 ngữ cảnh còn lại. *(/writing-for-agents)*
15. **Chỉ quyết định chuyển context tại phase boundary, theo thứ tự Continue → /clear → /handoff → subagent → /compact.** Vì sao: mọi tóm tắt đều biến primary source thành secondary source và làm mất thông tin. Lỗi điển hình là phiên mới tự tin nhưng sai. *(/ask-matt, /handoff)*
16. **Prototype cho câu hỏi "ungrillable".** Vì sao: tranh luận vòng quanh những câu này là chỗ phiên phình to. Prototype tồi dạy nhiều vì cho thấy mình *không* muốn gì. *(/prototype, /grill-me, video)*
17. **Research chỉ từ primary source, mỗi claim một citation. Đây là legwork được giao, không phải giao việc suy nghĩ.** Vì sao: năm subagent trỏ vào nguồn rác cho ra năm câu trả lời sai đầy tự tin nhanh hơn. *(/research)*
18. **Thu hẹp decision space.** Vì sao: càng ít lựa chọn càng ít sai, và mỗi quyết định AI tự phát làm rủi ro tăng lên. *(video 21k dòng)*
19. **Ratchet: khoá rule ngay với code mới, giảm vi phạm cũ dần theo lộ trình.** Vì sao: mỗi ngày một PR nhỏ giữ human review rẻ, và check chỉ chặt thêm chứ không lỏng ra. *(video, /software-factory)*
20. **Start slow: mỗi trigger là chân ga, nên cần ba phanh: automated checks, automated review, human review.** Vì sao: ga mà không có phanh là "slop cannon". *(/software-factory)*
21. **Viết cho agent: delete, don't explain. Prompt điều tích cực thay cho phủ định.** Vì sao: câu giải thích điều model đã biết là no-op, và phủ định gợi đúng thứ mình muốn tránh ("don't think of an elephant").
22. **Viết lịch sử, không viết hiện tại.** Vì sao: claim có ngày hoặc `repo@commit` thì không bị stale ngầm. Claim cũ được đánh dấu superseded chứ không viết lại. *(/chief-of-staff)*

## 3. Các skill và quy trình

### 3.1 Getting Started
- **/setup-matt-pocock-skills.** Chạy một lần cho mỗi repo, trước mọi skill engineering. Skill dò `git remote`, CLAUDE.md/AGENTS.md, glossary và ADR. Sau đó hỏi từng phần: tracker (GitHub/GitLab/local `.scratch/`/khác), triage labels, domain docs. Output: `docs/agents/issue-tracker.md`, `domain.md`, `triage-labels.md`, cùng khối `## Agent skills`. Có 5 role triage: `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`. Nguyên tắc "config is death": skill chỉ cấu hình tracker, labels và docs layout.
- **/ask-matt.** Router: mô tả tình huống, nó chỉ skill cần dùng rồi dừng. Bản đồ này viết tay nên thường chậm hơn repo. Khi nó mâu thuẫn với SKILL.md thì SKILL.md đúng. Nó chứa cây phase-boundary nêu ở nguyên tắc 15.

### 3.2 Main Flow
- **/grill-with-docs.** Dùng ở đầu một thay đổi trong repo, khi kế hoạch gói gọn trong một phiên. Bản thân skill chỉ là một dòng ủy quyền cho `grilling` và `domain-modeling`, nên phải cài cả hai. Các bước: trả lời câu hỏi về ngôn ngữ, glossary được cập nhật từng term, ADR nếu đủ ba cửa, rồi chuyển sang `/to-spec` trong cùng hội thoại. Output: `GLOSSARY.md` và `docs/adr/NNNN-*.md`. Mọi quyết định khác chỉ sống trong hội thoại.
- **/to-spec.** Dùng khi đã chốt xong nhưng công việc kéo dài nhiều phiên. Không phỏng vấn mà tổng hợp từ thread, code và glossary. Các bước: explore, phác seam và xác nhận với user, viết theo template, publish kèm `ready-for-agent`. Template: Problem Statement, Solution, User Stories (danh sách dài), Implementation Decisions (không có path hay code), Testing Decisions, Out of Scope, Further Notes. Không clear hay compact giữa to-spec và to-tickets.
- **/to-tickets.** Dùng khi đã có spec hoặc plan. Các bước: gom context, tìm prefactoring ("make the change easy, then make the easy change"), nháp các vertical slice cùng "Blocked by", quiz user, publish theo thứ tự dependency. Bản local là `.scratch/<slug>/issues/NN-*.md`, mỗi ticket một file. Refactor diện rộng dùng expand → migrate theo batch → contract. Acceptance criteria phải có khả năng fail ở commit gốc.
- **/implement.** Mỗi phiên một ticket, nhịp là clear → implement → commit → clear. Các bước: restate ticket, chạy `/tdd` ở seam, typecheck thường xuyên, chạy full suite một lần, `/code-review`, commit lên branch hiện tại. Skill không tạo branch, không mở PR và không tự đóng ticket.
- **/code-review.** Bắt buộc có fixed point. Diff dùng `<fp>...HEAD`, nên phần chưa commit sẽ không được review. Tìm spec theo thứ tự: issue ref trong commit → argument → file trong `docs/`/`specs/`/`.scratch/` → hỏi user. Không có spec thì báo "no spec available". Hai subagent, mỗi bên dưới 400 từ. Có baseline 12 code smell của Fowler, nhưng smell luôn chỉ là judgement call. Output: `## Standards` và `## Spec`, kèm vấn đề nặng nhất của mỗi trục.
- **/retro.** Dùng sau một increment hoặc một bug fix. Đọc log của phiên rồi tìm ứng viên theo 7 loại: navigation, automated checks, coding standards, AGENTS.md toàn cục, tool economy, no-op, information access. Output là danh sách đề xuất cải thiện môi trường, xếp theo severity.

### 3.3 Shaping
- **/wayfinder.** Dùng cho nỗ lực kéo dài nhiều phiên mà đường đi còn mờ. Nguyên tắc "plan, don't do". Chart mode: tạo map issue (`wayfinder:map`) gồm Destination, Notes, Decisions so far, Not yet specified, Out of scope, rồi tạo các decision ticket. Có 4 loại ticket: grilling, prototype (HITL), research (AFK), task. Work mode: claim bằng self-assign, mỗi phiên một ticket, resolve rồi cập nhật map. Khi map đã rõ thì chạy `/to-spec #map`.
- **/prototype.** Code thử nghiệm có thể bỏ đi, trả lời một câu hỏi thiết kế. Nhánh LOGIC là một file HTML tự chứa, logic viết dạng pure reducer. Nhánh UI mặc định 3 biến thể (tối đa 5), đổi qua `?variant=` và một switcher bar. Không test, không DB thật, không abstraction. Sau khi xong, commit lên branch `prototype/` để làm primary source, không merge.
- **/research.** Một background agent với fresh context viết một file markdown có citation đặt trong thư mục notes. Ranh giới với ADR là shelf life. Lỗi đã biết: skill có thể tự spawn lại agent con, có lượt chạy tốn khoảng 450k token.

### 3.4 Engineering
- **/improve-codebase-architecture.** Khảo sát tìm deepening opportunity rồi xuất báo cáo HTML ra temp: mỗi candidate một card, có badge Strong/Worth exploring/Speculative. Skill không sửa code. Sau khi chọn một candidate thì grill tiếp trên candidate đó. Prompt hiệu quả nhất: "how can we make this change easy?"
- **/diagnosing-bugs.** 6 phase: (1) feedback loop, với thang 10 nấc từ failing test đến HITL script; (2) reproduce và minimise; (3) 3–5 giả thuyết falsifiable; (4) instrument từng biến, log gắn tag `[DEBUG-xxxx]`; (5) regression test viết trước fix, đặt ở seam đúng; (6) cleanup checklist. Redact secret.
- **/triage.** Chỉ dùng cho issue hoặc PR từ bên ngoài. Skill đề xuất rồi chờ maintainer. Các bước: gom context, đề xuất, verify, grill nếu cần, rồi apply: viết agent brief (`## Agent Brief`), Triage Notes, hoặc `wontfix` kèm file `.out-of-scope/<concept>.md`. Không triage ticket do to-tickets sinh ra.
- **/wizard.** Sinh script bash dẫn người làm các bước chỉ người làm được: dashboard, key, cutover. Script ghi `.env` và GitHub secrets/vars. Agent viết script nhưng không chạy. Secret nhập ẩn, stage nào không thể hoàn tác thì có `confirm`.
- **/implement-spec.** Chạy cả spec trên một integration branch. Ticket được xem như task graph: các ticket trên frontier chạy song song, mỗi implementer một worktree và chạy tdd, merger subagent gộp vào integration branch. Cuối cùng chạy code-review và một implementer mới sửa các finding. Subagent giao tiếp với nhau qua context pointer.

### 3.5 Productivity
- **/grill-me.** Grilling không trạng thái, dùng khi không có repo. Một phiên bình thường khoảng 46 câu trong 4 round. Nên dùng model tốt nhất và tắt plan mode. Muốn hỏi từng câu một thì thêm vào CLAUDE.md: `When grilling, ask one question at a time.`
- **/handoff.** Ghi file markdown vào thư mục temp cho một agent khác tiếp tục. Chỉ dùng trong 4 trường hợp: đổi harness, đổi thư mục hoặc repo, giao cho đồng nghiệp, hoặc fork một nhánh phụ. File tham chiếu artifact chứ không chép lại, có phần "suggested skills", và đã redact secret.
- **/to-questionnaire.** Câu trả lời nằm trong đầu người khác. Skill chỉ hỏi về người nhận và thông tin cần lấy, rồi ghi `to-questionnaire-<slug>.md`. Câu quan trọng nhất đặt trước, mỗi câu một ý.
- **/teach.** Workspace học nhiều phiên: `MISSION.md`, `RESOURCES.md`, `lessons/*.html`, `reference/`, `learning-records/`. Nguyên tắc: ưu tiên storage strength hơn fluency, dùng desirable difficulty, mọi claim có citation.
- **/wait-what.** Agent pitch lại câu trả lời bằng ASD-STE100 và glossary. Skill chỉ có 3 dòng. Chữ "wait" mô tả trạng thái của người nghe, nên hiệu quả hơn "be concise".
- **/writing-for-agents.** Tài liệu tham chiếu cho mọi văn bản agent đọc (đã nêu ở nguyên tắc 21). Có `SKILL-MECHANICS.md` giải thích model-invoked và user-invoked.

### 3.6 Reference
- **/pr.** Thân PR gồm Summary (visual nhỏ nhất đủ ý), Evidence (Before/After; screenshot là S-tier, kết quả test là A-tier) và Merge Danger (Door one-way/two-way, Blast Radius).
- **/codebase-design.** Từ vựng cho deep module. Có `DEEPENING.md` với 4 loại dependency: in-process, local-substitutable, remote-owned (ports & adapters), true external. Có `DESIGN-IT-TWICE.md`: chạy từ 3 subagent trở lên cho ra các interface khác hẳn nhau, so sánh rồi đưa khuyến nghị.
- **/domain-modeling.** Chất vấn term, làm sắc từ mơ hồ, đối chiếu với code, ghi `GLOSSARY.md` theo GLOSSARY-FORMAT. Repo nhiều context thì có thêm GLOSSARY-MAP. ADR theo ADR-FORMAT, đánh số NNNN.
- **/grilling.** Primitive phỏng vấn (nguyên tắc 2–3). Có confirmation gate trước khi hành động.
- **/tdd.** Vòng red → green, mỗi lần một slice. Refactor đã bị tách khỏi vòng từ 06/2026 và chuyển sang code-review. Chỉ mock ở system boundary, và ưu tiên interface kiểu SDK.

### 3.7 Misc
- **/git-guardrails-claude-code.** Hook PreToolUse chặn `push`, `reset --hard`, `clean -f`, `branch -D`, `checkout .`. Script exit 2 khi chặn.
- **/migrate-to-shoehorn.** Thay `as` trong test bằng `fromPartial` hoặc `fromAny`.
- **/scaffold-exercises.** Dựng thư mục bài tập cho khoá học, dùng lint làm feedback loop.
- **/setup-pre-commit.** Cài Husky và lint-staged (Prettier), kèm typecheck và test.

### 3.8 In-progress
- **/claude-handoff.** Handoff rồi khởi chạy `claude --bg --name`.
- **/loop-me.** Grilling cho ra `workflows/*.md`. Từ vựng: loop, trigger, checkpoint, push right, brief.
- **/setup-ts-deep-modules.** Rule dependency-cruiser kiểm soát entry point. Phải chứng minh rule hoạt động bằng vòng pass → fail → pass.
- **/writing-fragments → /writing-beats hoặc /writing-shape.** Pha explore gom fragment, sau đó pha exploit dựng bài theo beat hoặc theo lập luận. Quy tắc: chỉ dùng concept đã grounded.
- **/chief-of-staff.** Agent đóng vai DRI cho một mục tiêu dài hạn: giao việc cho subagent, duy trì wiki (ingest/query/lint), chạy retro cho khoảng 1/5 số phiên.
- **/software-factory.** Từ vựng: task, trigger, run, runner, ticket tracker/source, git host, orchestrator. Có bảng ví dụ task (Explore, Implementer, Review, Rework, Ratchet, Fix…). Nguyên tắc "buy the services, build the tasks".

### 3.9 Archived
- **/resolving-merge-conflicts.** Giải từng hunk theo ý định của mỗi bên, chạy check, không bao giờ `--abort`. Đã bị loại khỏi repo từ v1.3.0 vì agent tự làm được.

### 3.10 Quy trình mẫu (video "ship 21.000 dòng")
Theo kích thước diff: diff nhỏ thì one-shot; diff lớn thì grill (khoảng 30–50 câu, nói WHY thay vì WHAT); vượt một phiên thì chuyển sang wayfinder. Tiếp theo: thử term bằng scenario, prototype 3 biến thể, to-spec (47 user stories), to-tickets (9 ticket), compact (từ khoảng 260k xuống 10k token), implement-spec AFK, chia thành 7 stacked PR theo door kèm feature flag, rồi retro trên hơn 30 phiên, cho ra khoảng 20 issue cải tiến. Owner lưu ý các con số này chỉ là ví dụ, không phải định mức.

## 4. Sai lầm thường gặp

- **Gật "yes" với 40 câu.** Kết quả là một plan của agent mà bạn chỉ gật đầu. Phiên 200 câu nghĩa là phạm vi quá lớn, cần chia nhỏ.
- **Agent tự trả lời câu hỏi grilling, hoặc hết câu hỏi thì nhảy vào code.** Cách chữa: thêm vào AGENTS.md rằng không implement khi chưa được cho phép.
- **Skill ủy quyền không nạp đủ phụ thuộc.** Dấu hiệu: hỏi dồn tất cả cùng lúc, không có khuyến nghị, glossary không đổi. Cách chữa: hỏi agent đã nạp những skill nào.
- **GLOSSARY.md phình thành spec,** có khi 500–3000 dòng. Glossary agent viết mà không ai review sẽ thành "lore".
- **Nhãn `ready-for-agent` gắn trên spec cha.** AFK runner sẽ build cả spec trong một lượt.
- **Ticket cắt theo layer, hoặc 12 ticket cho một thay đổi 3 dòng.** Acceptance criteria không thể fail.
- **Clear hoặc compact giữa to-spec và to-tickets.** Spec bị cắt cụt.
- **Chạy song song nhiều `/implement` trong cùng một checkout.** Hậu quả: amend nhầm commit, mất stash, commit lên sai branch.
- **Review khi chưa commit, hoặc review trong chính phiên đã viết code.**
- **Tin finding của review như sự thật.** Finding chỉ là giả thuyết, phải kiểm citation. Chạy review lại liên tục không bao giờ hội tụ.
- **Subagent tự spawn đệ quy.** Đã ghi nhận ở code-review (hơn 50 agent) và research (khoảng 450k token). Cách chữa: thêm câu "if you're already a subagent, do it yourself".
- **Wayfinder viết code production.** Map 27 ticket bị stale từ ticket thứ 13 (bẫy waterfall). Nên "prototypemaxxing, not planmaxxing".
- **Lý thuyết hoá khi chưa có loop đỏ được.** Giả thuyết không kèm dự đoán chỉ là "a vibe".
- **Test tautological, mock module của chính mình, viết hết test trước.**
- **Prototype cả app, biến thể chỉ khác màu, đem code biến thể đưa thẳng lên production.**
- **Tin handoff như hợp đồng.** File có thể chứa claim chưa ai kiểm chứng. File temp bị xoá. Dấu backtick hoặc `$(...)` trong lệnh shell làm cắt mất nội dung.
- **Sửa trực tiếp SKILL.md đã cài.** Lần `npx skills update` sau sẽ ghi đè. Hành vi lâu dài nên đặt trong CLAUDE.md/AGENTS.md.
- **Trùng tên `/code-review` với lệnh có sẵn của Claude Code.**
- **Comment thừa và workaround do AI sinh.** Trong video: 18–20% số dòng mới là comment, khoảng 940 dòng thừa; 230 chỗ `useEffect`; khoảng 2000 chỗ dùng `as`. Cách chữa là ratchet lint, nhưng không áp rule "cấm comment/as/useEffect" cho mọi repo. *(video, trang chính)*
- **Coi 150k token, 30 phiên, 7 PR hay 47 stories là luật.** Đó chỉ là ví dụ.
- **Coi test pass là đã nghiệm thu,** hoặc coi feature flag là cách rollback được cả schema.

## 5. Thuật ngữ

- **Frontier.** Với grilling: các câu hỏi đã đủ tiền đề. Với ticket/wayfinder: các ticket mở, không còn blocker và chưa ai claim.
- **Design tree.** Cây quyết định mà grilling đi qua từng nhánh.
- **Confirmation gate.** Agent dừng lại xác nhận đã hiểu chung với người trước khi hành động.
- **Ubiquitous language.** Ngôn ngữ chung giữa code, developer và domain expert (từ DDD).
- **ADR.** Architecture Decision Record, chỉ viết khi qua đủ ba cửa.
- **GLOSSARY-MAP.** Bản đồ cho repo nhiều bounded context.
- **Tracer bullet / vertical slice.** Một đường hẹp nhưng xuyên mọi layer, demo được.
- **Blocking edge.** Quan hệ "blocked by" giữa các ticket.
- **Prefactoring.** Làm cho thay đổi trở nên dễ trước khi thực hiện nó.
- **Expand–contract.** Refactor diện rộng theo ba bước: expand, migrate, contract.
- **Seam.** Chỗ có thể đổi hành vi mà không sửa tại chỗ đó; nơi interface nằm.
- **Module, Interface, Implementation, Depth, Adapter, Port, Leverage, Locality, Pass-through, Deletion test.** Từ vựng deep module (xem 3.6, /codebase-design).
- **Smart zone / dumb zone.** Dưới khoảng 120–150k token chất lượng còn tốt; vượt quá thì attention suy giảm.
- **Phase boundary.** Điểm giữa hai pha, nơi chọn Continue, `/clear`, `/handoff`, subagent hoặc `/compact`.
- **Primary / secondary source.** Hội thoại gốc so với bản tóm tắt (có mất mát).
- **HITL / AFK.** Có người trong vòng / agent chạy một mình.
- **Integration branch.** Branch gộp các ticket của một spec.
- **Task graph.** Tập ticket nhìn như một đồ thị theo dependency.
- **Context pointer.** Tham chiếu tới tài liệu sẵn có thay vì chép lại nội dung.
- **Context load / cognitive load.** Chi phí context của model so với chi phí đặt lên người.
- **Progressive disclosure.** Inline phần mọi nhánh cần, đặt sau pointer phần chỉ một số nhánh dùng.
- **Leading word.** Từ ngắn gọn gợi cả một khái niệm, như *tracer bullets* hay *fog of war*.
- **No-op.** Câu không làm đổi hành vi. **Sediment.** Nội dung cũ tích tụ lại.
- **Premature completion.** Agent kết thúc sớm vì thấy các bước phía sau.
- **Fixed point.** Commit, branch hoặc tag làm mốc để diff khi review.
- **Hard violation / judgement call.** Vi phạm rõ ràng so với điều cần phán đoán.
- **Ratchet.** Siết dần: khoá rule với code mới, giảm vi phạm cũ theo lộ trình.
- **One-way / two-way door.** Quyết định không thể / có thể quay lại.
- **Blast radius.** Phạm vi ảnh hưởng của một thay đổi.
- **Fog of war.** Quyết định thấy trước được nhưng chưa phát biểu sắc được.
- **Destination.** Trạng thái khi đi hết map.
- **Decision ticket.** Ticket mà câu trả lời là một quyết định.
- **Ungrillable.** Câu hỏi cần có thứ để phản ứng (prototype).
- **Storage strength / fluency, desirable difficulty.** Thuật ngữ học tập dùng trong /teach.
- **DRI.** Người chịu trách nhiệm trực tiếp cho một mục tiêu.
- **Pit of success.** Môi trường khiến làm đúng là dễ.
- **Task / Trigger / Run / Runner / Orchestrator.** Từ vựng software factory: run không bao giờ chờ người, runner dùng xong bỏ.
- **Slop cannon.** Trigger không có phanh.
- **Loop / workflow / checkpoint / push right / brief.** Từ vựng của /loop-me.
- **Beat / grounded / prerequisite / fragment / pile.** Từ vựng của bộ skill writing.

## 6. Danh sách nguồn

Nguồn công khai:
- https://github.com/mattpocock/skills : README, `skills/*/SKILL.md`, GLOSSARY.md, CHANGELOG.md.
- https://www.aihero.dev/skills-changelog-v13-implement-spec-pr-retro-and-glossary-md
- https://www.aihero.dev/watch-me-ship-a-21-000-line-feature-with-mattpocock-skills~ez95n
- https://www.aihero.dev/grill-with-docs
- https://www.aihero.dev/things-people-get-wrong-with-grill-me-and-grill-with-docs
- https://www.aihero.dev/tracer-bullets
- https://www.aihero.dev/how-to-make-codebases-ai-agents-love
- https://www.aihero.dev/ai-coding-dictionary/smart-zone

Lưu ý về độ tin cậy:
- Repo thay đổi thường xuyên; tên skill và hành vi có thể đã đổi, hãy đọc lại SKILL.md trước khi dựa vào.
- Một FAQ của skill triage có thể mâu thuẫn với SKILL.md về việc tạo label; SKILL.md thắng.
- Các nguồn video có thể mâu thuẫn nhau về ngưỡng 120k hay 150k token và về tên model; ghi "chưa chốt".
- Các con số trong video demo (47 user story, 9 ticket, 7 PR, 30 phiên) chỉ là ví dụ, không phải định mức.
