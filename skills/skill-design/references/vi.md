# Thiết kế skill (bản tiếng Việt)

Bản tiếng Việt của `SKILL.md`. Biến một quy trình (workflow), SOP hoặc một khối kiến thức thành skill theo chuẩn Agent Skills, rồi kiểm thử và xuất bản. Vòng làm việc (work loop): làm rõ, nghiên cứu, lập kế hoạch, xây dựng, kiểm chứng. Trả lời bằng ngôn ngữ của người dùng; người dùng Việt nhận kết quả bằng tiếng Việt.

**Cổng (gate)** là điểm dừng để người dùng duyệt trước khi làm tiếp. Các cổng trong skill này: trước khi cài bất cứ thứ gì tìm được trên mạng, trước khi ghi đè một skill đang có, trước khi xuất bản.

## Skill là gì

**Agent Skill** là một thư mục có tệp `SKILL.md` (frontmatter YAML gồm `name` và `description`, rồi các bước bằng Markdown) và tùy chọn `scripts/`, `references/`, `assets/`. Agent nạp skill theo **progressive disclosure** (nạp dần theo nhu cầu): `description` luôn nằm trong ngữ cảnh, thân `SKILL.md` chỉ nạp khi prompt khớp, các tệp khác chỉ nạp khi agent đọc hoặc chạy chúng.

Nền tảng chạy được skill (đã đối chiếu tài liệu chính thức và máy này ngày 2026-11-18):

| Nền tảng | Skill nằm ở đâu hoặc nhập vào bằng cách nào |
|---|---|
| Claude Code | Thư mục `~/.claude/skills/<name>/SKILL.md` (cá nhân), `.claude/skills/<name>/SKILL.md` (dự án) hoặc plugin. Không cần tải lên. |
| Claude.ai | Tải lên tệp zip trong phần cài đặt. Skill tùy biến cần gói Pro, Max, Ultra, Team hoặc Enterprise và bật code execution. |
| Claude API | Tải lên qua `/v1/skills`, rồi liệt kê `skill_ids` trong tham số `container` cùng công cụ code execution. Dùng chung cả workspace; container không có mạng. |
| Agent SDK | Tệp trên đĩa trong `.claude/skills/`, được tìm qua `settingSources` và tùy chọn `skills`. Không có API đăng ký skill bằng code. |
| OpenMausBot | Thư mục `workspaces/<botId>/skills/<name>/SKILL.md` trong thư mục dữ liệu, thuộc về một bot (thấy trên máy này). Giao diện nhập skill và việc nhập giữ những tệp nào: chưa kiểm chứng; một lần nhập ở đây chỉ giữ SKILL.md. |

Skill tùy biến không đồng bộ giữa các nền tảng Claude: tải lên hoặc sao chép riêng cho từng nơi.

| Thứ | Là gì | Khi nào được nạp | Dùng khi |
|---|---|---|---|
| Prompt | Một tin nhắn chỉ dẫn | Chỉ lượt đó | Việc làm một lần |
| Soul (chỉ dẫn thường trực) | Vai trò, giọng và các cổng cố định của bot | Mọi lượt, xếp trên skill | Bot là ai và không bao giờ làm gì |
| AGENTS.md / CLAUDE.md | Quy tắc luôn bật của dự án | Mọi phiên | Sự kiện và quy tắc ngắn |
| Skill | Quy trình tái dùng có bước và tiêu chí kiểm | Description luôn nạp, thân nạp khi khớp | Quy trình lặp lại, mỗi lần chạy giống nhau |
| Bot | Một agent có soul, model, thư mục và mức phê duyệt | Chạy khi được gọi | Người làm việc mang các skill |

## Bước 1. Tiếp nhận (làm rõ)

Hỏi gộp một lần tất cả trường còn thiếu. Trường nào chưa có thì điền mặc định và nói rõ.

| Trường | Câu hỏi | Mặc định |
|---|---|---|
| chủ đề (topic) | Quy trình, SOP hay kiến thức nào sẽ thành skill? | bắt buộc |
| người dùng đích (target user) | Ai chạy skill, trong agent nào? | bắt buộc |
| đầu vào sẵn có (inputs) | Tài liệu, bản ghi, ví dụ, một lần chạy thật? | không có |
| mức chi tiết | cao, vừa hay thấp | vừa |
| ngôn ngữ | Ngôn ngữ của thân skill | tiếng Anh, kèm bản tiếng Việt cho người dùng Việt |
| chế độ chạy (execution mode) | `coach` (hỏi từng bước), `auto` (chạy trọn vẹn, chỉ dừng ở cổng) hoặc `hybrid` | hybrid |
| nơi triển khai | cài toàn cục, thư mục dự án, hay repo công khai | thư mục dự án |
| tiêu chí hoàn thành | Một lần chạy đúng trông như thế nào | một tác vụ mẫu |

Xong khi: mọi trường đã có câu trả lời hoặc mặc định được nêu rõ, và người dùng xác nhận bản tóm tắt.

## Bước 2. Tìm skill đã có

1. Chạy `npx skills find <nhu cầu trong 2-4 từ>` và tìm trên https://skills.sh với cùng từ khóa. Thử thêm một truy vấn theo lĩnh vực của vấn đề.
2. Mở SKILL.md của từng ứng viên và đọc nội dung thật. Đánh giá theo bốn điểm: có bao phủ tác vụ của người dùng, có chạy được trong agent của họ, có hỏi trước khi hành động ra bên ngoài, không gọi mạng ngầm.
3. Trình bày bảng ngắn: skill, nguồn, phần bao phủ, phần thiếu. Hỏi người dùng: dùng nguyên bản, tùy biến, hay làm mới. Hiển thị đúng lệnh cài và chỉ cài khi người dùng đồng ý (cổng).
4. Khi tùy biến, coi skill tìm được là tài liệu tham khảo và xây từ quy trình của chính người dùng.

Xong khi: người dùng đã chọn dùng, tùy biến hay làm mới, kèm danh sách ứng viên (hoặc "không tìm thấy").

## Bước 3. Nên hay không nên làm skill (go/no-go)

Skill đáng làm khi cả bốn câu trả lời là có:

1. Tác vụ lặp lại, hoặc sẽ lặp lại, với cùng một hình dạng.
2. Không có hướng dẫn viết sẵn thì agent làm sai hoặc thiếu nhất quán (chạy thử một prompt nền để thấy).
3. Các bước viết ra được và kiểm tra được thành công.
4. Kiến thức còn đúng lâu hơn một tuần.

Tác vụ làm một lần, tra cứu dữ kiện thuần túy, hoặc quy tắc vừa trong một dòng của AGENTS.md hay CLAUDE.md thì không cần skill: hãy nói thẳng và chỉ ra nơi phù hợp hơn.

Xong khi: có kết luận (làm hoặc không) kèm một lý do cho mỗi câu hỏi.

## Bước 4. Chọn cỡ skill (tier)

| Cỡ | Dùng khi | Cấu trúc |
|---|---|---|
| đơn giản (simple) | một ý, khoảng 200 dòng trở xuống | chỉ `SKILL.md` |
| mở rộng (expanded) | nhiều chủ đề nhỏ, mẫu biểu, ví dụ dài | `SKILL.md` cộng `references/` |
| nền tảng (platform) | một sản phẩm hoặc lĩnh vực có nhiều mảng riêng | `SKILL.md` làm bộ định tuyến, mỗi mảng một `references/<mảng>.md`, `scripts/` cho việc tất định |

Bắt đầu từ cỡ nhỏ nhất đủ chứa quy trình. Đồng thời xác định loại skill, vì loại quyết định kiểu kiểm thử: kỹ thuật (how-to), tham chiếu (tra cứu), kỷ luật (quy tắc phải giữ dưới áp lực), mẫu tư duy (pattern).

Xong khi: đã ghi lại cỡ và loại.

## Bước 5. Viết mô tả (description) trước

Mô tả là đoạn văn duy nhất của skill luôn được nạp vào ngữ cảnh, nên chỉ nó quyết định skill có kích hoạt hay không. Soạn nó trước phần thân.

- Một dòng, tối đa 1024 ký tự, không có dấu nháy kép, không có chuỗi `: ` (làm hỏng YAML thường).
- Mở đầu bằng skill làm gì (động từ trước), rồi `Use when` kèm 3-6 tình huống khác nhau của người dùng, với những từ khóa người dùng thực sự gõ, kể cả khi họ không nêu tên lĩnh vực.
- Nêu kết quả và tình huống kích hoạt. Để danh sách bước trong phần thân: agent đọc tóm tắt bước ở mô tả thường làm theo đó mà bỏ qua phần thân.
- Kết thúc bằng 4-8 từ khóa kích hoạt bằng ngôn ngữ người dùng (tiếng Việt có dấu).
- Bỏ các từ quá chung ("giúp", "việc"): chúng kích hoạt nhầm mọi thứ.

Xong khi: mô tả qua kiểm tra ở Bước 8 và người chưa đọc phần thân vẫn hiểu đúng.

## Bước 6. Viết phần thân (body)

1. **Bước đi trước.** Đánh số, mỗi bước kết thúc bằng một dòng "Xong khi" kiểm tra được. Phần tham chiếu (bảng, quy tắc, định nghĩa) đặt sau các bước.
2. **Chỉ thêm điều agent còn thiếu.** Với mỗi dòng hãy hỏi: không có dòng này agent có làm sai không? Nếu không thì cắt. Bẫy thường gặp và quy ước bất thành văn đặt trong SKILL.md.
3. **Một mặc định**, kèm lối thoát ngắn, thay cho một thực đơn lựa chọn.
4. **Câu lệnh khẳng định.** Nêu hành vi mong muốn. Chỉ giữ điều cấm như lan can cứng, đi kèm việc cần làm thay thế. Nêu lý do cho các bước dễ hỏng.
5. **SKILL.md tự đủ.** Một số nền tảng chỉ nhập SKILL.md, không nhập `references/` hay `scripts/`. Mọi bước cần cho một lần chạy nằm trong SKILL.md; `references/` chỉ chứa phần chiều sâu tùy chọn, mỗi tệp ghi rõ điều kiện để đọc.
6. **Chỉ sâu một tầng.** SKILL.md liên kết tới tệp; các tệp đó không liên kết tiếp. Dùng đường dẫn tương đối từ gốc skill.
7. **Script chỉ cho việc tất định** (kiểm tra, phân tích cú pháp, chuyển đổi). Chỉ thư viện chuẩn, không hỏi tương tác, có `--help`, báo lỗi rõ, thoát mã khác 0 khi thất bại. Skill vẫn chạy được khi nền tảng bỏ qua script.
8. **Không bao giờ để thông tin xác thực trong thư mục skill.** Khóa API, token, URL webhook, mật khẩu và ghi chú đăng nhập thuộc về kho bí mật hoặc kết nối của nền tảng. Skill chỉ gọi tên kết nối ("dùng kết nối đã lưu tên X") và không lưu gì thêm.
9. Markdown thuần. Nhắm dưới 300 dòng cho SKILL.md; tuyệt đối dưới 500.

Xong khi: mỗi bước có tiêu chí hoàn thành, mọi liên kết trỏ đúng, và người đọc chạy được skill chỉ từ SKILL.md.

## Bước 7. Kiểm thử

Viết bài kiểm thử trước khi tuyên bố skill xong. Cách dựng subagent: [testing.md](testing.md). Định dạng tệp: [templates.md](templates.md).

1. **Kiểm thử kích hoạt (trigger tests).** 8-10 prompt nên kích hoạt và 8-10 prompt không nên. Prompt âm tính nên là loại gần giống, có chung từ khóa. Thay đổi cách diễn đạt, độ trang trọng, độ dài, và việc có nêu tên lĩnh vực hay không.
2. **Ca kiểm thử tác vụ (test cases).** 3-5 prompt thực tế kèm hành vi mong đợi, thêm một prompt mơ hồ và một trường hợp biên. Lưu thành `evals/evals.json`.
3. **Chạy nền (baseline).** Chạy từng ca trong ngữ cảnh mới, không có skill. Ghi lại điều sai, đúng nguyên văn lời agent.
4. **Chạy lại (retest).** Chạy cùng các ca với skill. So với baseline và hành vi mong đợi.
5. **Sửa và chạy lại.** Xử lý mỗi lỗi tại nguyên nhân (thường là thiếu một chỉ dẫn hoặc mô tả yếu). Chạy lại các ca hỏng và một mẫu các ca đã đạt. Sửa theo nguyên nhân của ca hỏng, và không dán nguyên từ của prompt hỏng vào mô tả.
6. **Ngưỡng đạt.** Ít nhất 80% prompt nên kích hoạt thì kích hoạt, nhiều nhất 10% prompt không nên kích hoạt mà vẫn kích hoạt, và mọi ca tác vụ đạt hành vi mong đợi.

Xong khi: kết quả baseline và retest nằm cạnh nhau và đạt ngưỡng, hoặc các lỗi còn lại được liệt kê ở mục việc còn mở.

## Bước 8. Kiểm tra theo đặc tả (spec)

Chạy `python scripts/validate_skill.py <thư-mục-skill>` khi có script; nếu không, kiểm tra thủ công theo các quy tắc sau (đặc tả Agent Skills):

- `SKILL.md` tồn tại và có frontmatter YAML.
- `name`: bắt buộc, 1-64 ký tự, chữ thường `a-z`, số `0-9` và dấu gạch ngang, không bắt đầu, kết thúc hoặc đặt hai gạch ngang liền nhau, trùng tên thư mục.
- `description`: bắt buộc, không rỗng, tối đa 1024 ký tự, một dòng.
- Trường tùy chọn: `license` (tên ngắn), `compatibility` (tối đa 500 ký tự, chỉ khi có yêu cầu môi trường thật), `metadata` (ánh xạ chuỗi sang chuỗi cho tác giả, phiên bản, ngôn ngữ), `allowed-tools` (thử nghiệm, cách nhau bằng dấu cách).
- Bộ kiểm tra chặt theo đặc tả từ chối các khóa cấp cao khác, nên khóa tùy ý đặt dưới `metadata`.
- SKILL.md dưới 500 dòng; phần thân khoảng dưới 5000 token.
- Mọi liên kết tương đối trỏ đúng; không có đường dẫn cục bộ tuyệt đối (ký tự ổ đĩa, thư mục người dùng).
- `scripts/`, `references/`, `assets/` là quy ước; `evals/` chứa bài kiểm thử.

Xong khi: mọi kiểm tra đạt.

## Bước 9. Đóng gói và xuất bản

1. Cấu trúc trong repo: `skills/<tên>/SKILL.md`, kèm `references/`, `scripts/`, `evals/`. Trình cài tự tìm thấy `skills/<tên>/SKILL.md`. Xem trước bằng `npx skills add <chủ-sở-hữu>/<repo> --list`.
2. Rà thư mục để loại thông tin xác thực, đường dẫn cá nhân, tên riêng tư và văn bản chép từ bên thứ ba. Ghi từng nguồn dưới mục Sources ở cuối tệp dùng nguồn đó.
3. Chọn phiên bản và viết mục changelog theo [templates.md](templates.md). PATCH: sửa chữ hoặc lỗi chính tả, hành vi không đổi. MINOR: thêm phần, script hoặc tham chiếu; cách dùng cũ vẫn chạy. MAJOR: đổi tên bước, đổi định dạng đầu ra, xóa trường. Phân vân giữa hai mức thì chọn mức cao hơn.
4. Cổng: cho người dùng xem danh sách tệp, phiên bản và lệnh cài. Chỉ xuất bản sau khi được duyệt.
5. Người dùng cài bằng `npx skills add <chủ-sở-hữu>/<repo>` (`--skill <tên>` cho một skill, `-g` để cài toàn cục).

Xong khi: người dùng đã duyệt, mục changelog đã có, và bản xem trước `--list` hiện skill.

## Cập nhật một skill đang có

1. Đọc SKILL.md hiện tại và các bài kiểm thử. Xin một lỗi thật: prompt và điều agent đã làm.
2. Tái hiện lỗi thành một ca kiểm thử kích hoạt hoặc tác vụ, chạy khi chưa sửa để xác nhận nó hỏng.
3. Sửa phần nhỏ nhất giải thích được lỗi: mô tả nếu trượt kích hoạt, bước hoặc tiêu chí hoàn thành của nó nếu hành vi sai.
4. Chạy lại toàn bộ bộ kiểm thử và trình kiểm tra; xác nhận không ca cũ nào thụt lùi.
5. Tăng phiên bản, thêm mục changelog (nguyên nhân, thay đổi, di chuyển, quay lui), và đi qua cổng ở Bước 9.

Xong khi: ca hỏng đã đạt, không ca cũ nào thụt lùi, và changelog nêu rõ nguyên nhân.

## 4 tiêu chí đóng gói

Skill sẵn sàng phát hành khi nó:

1. **Tối giản (minimal)**: một công việc mạch lạc; mỗi dòng đều làm thay đổi hành vi.
2. **Chính xác (accurate)**: các bước khớp với cách việc diễn ra thật, đã đối chiếu với một lần chạy thật.
3. **Mô-đun (modular)**: chiều sâu ở `references/`, việc tất định ở `scripts/`, mỗi dữ kiện có một nguồn duy nhất.
4. **Đầu vào và đầu ra rõ ràng**: nêu skill nhận gì và giao ra gì, để skill hoặc bot khác nối vào được.

## Bàn giao (handoff)

Khi chuyển việc cho bot khác hoặc người dùng, gửi 5 trường theo thứ tự: Goal (mục tiêu, một câu), Inputs (đầu vào đính kèm hoặc liên kết), Deliverable (sản phẩm: tên tệp hoặc nội dung trực tiếp), Done when (tiêu chí hoàn thành kiểm tra được), Open items (câu hỏi, rủi ro, việc chưa làm).

## Đọc thêm khi cần

- [templates.md](templates.md): khi soạn bản nháp quy trình, mục changelog hoặc `evals/evals.json`.
- [testing.md](testing.md): khi chạy baseline và retest bằng subagent, hoặc khi skill liên tục hỏng.
- `scripts/validate_skill.py`: trình kiểm tra ở Bước 8.

## Nguồn

- Anthropic, "Skill authoring best practices": https://docs.claude.com/en/docs/agents-and-tools/agent-skills/best-practices
- Đặc tả Agent Skills: https://agentskills.io/specification
- Anthropic, "Agent Skills overview" (nền tảng, các mức nạp, phạm vi chia sẻ): https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
- Claude Code, "Extend Claude with skills" (vị trí skill, so với CLAUDE.md): https://code.claude.com/docs/en/skills
- Claude Agent SDK, "Extend agents with skills": https://code.claude.com/docs/en/agent-sdk/skills
- obra/superpowers, "writing-skills" (ý tưởng kiểm thử trước cho skill): https://github.com/obra/superpowers
- vercel-labs/skills (`npx skills`, find-skills): https://github.com/vercel-labs/skills
- Thư mục skill: https://skills.sh
