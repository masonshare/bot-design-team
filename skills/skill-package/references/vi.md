# Đóng gói skill (bản tiếng Việt)

Bản tiếng Việt của `SKILL.md`. Làm cho một skill đã xong trở nên hợp lệ và chia sẻ được. Nhận một thư mục skill đã qua skill-test. Giao ra thư mục đạt chuẩn, phiên bản, mục changelog và lệnh cài, sau khi người dùng duyệt.

**Cổng (gate)** là điểm dừng để người dùng duyệt trước khi làm tiếp. Các cổng ở đây: trước khi ghi đè một skill đang có, trước khi xuất bản.

## Định tuyến

| Người dùng muốn | Dùng |
|---|---|
| Kiểm tra theo chuẩn, đặt phiên bản, xuất bản, chia sẻ | skill này |
| Sửa description hoặc phần thân | skill-write |
| Chạy kiểm thử | skill-test |
| Chấm, chia hoặc gộp skill | skill-review |
| Làm trọn cả quy trình | skill-design |

Khi skill tương ứng chưa được cài, nói một dòng rằng nó chưa có, rồi làm xong phần việc có thể làm ở đây.

## Các bước

### 1. Kiểm tra theo chuẩn

Chạy `python scripts/validate_skill.py <thư-mục-skill>` (đường dẫn tính từ gốc skill này; script chỉ cần thư viện chuẩn của Python và thoát mã 1 khi có lỗi). Khi thiếu script, kiểm tay theo các quy tắc sau (đặc tả Agent Skills):

- `SKILL.md` tồn tại và có frontmatter YAML.
- `name`: bắt buộc, 1-64 ký tự, chữ thường `a-z`, số `0-9` và dấu gạch ngang, không bắt đầu, kết thúc hoặc đặt hai gạch ngang liền nhau, trùng tên thư mục.
- `description`: bắt buộc, không rỗng, tối đa 1024 ký tự, một dòng, không có dấu nháy kép và không có chuỗi `: `.
- Trường tùy chọn: `license`, `compatibility` (tối đa 500 ký tự), `metadata` (ánh xạ chuỗi sang chuỗi cho tác giả, phiên bản, ngôn ngữ), `allowed-tools` (thử nghiệm). Bộ kiểm tra chặt theo đặc tả từ chối các khóa cấp cao khác, nên khóa tùy ý đặt dưới `metadata`.
- SKILL.md dưới 500 dòng; phần thân khoảng dưới 5000 token.
- Mọi liên kết tương đối trỏ đúng; không có đường dẫn cục bộ tuyệt đối (ký tự ổ đĩa, thư mục người dùng).

Sửa từng lỗi tại nguyên nhân và chạy lại đến khi sạch.

Xong khi: mọi kiểm tra đạt, và kết quả đầu ra đã được lưu cho người dùng.

### 2. Rà sạch (scrub)

Loại khỏi thư mục mọi thông tin xác thực, đường dẫn cá nhân, tên riêng tư và văn bản chép từ bên thứ ba. Khóa, token và URL webhook thuộc về kho bí mật hoặc kết nối của nền tảng, không bao giờ nằm trong thư mục skill. Ghi từng nguồn dưới mục Sources ở cuối tệp dùng nguồn đó.

Xong khi: tìm trong thư mục các khóa, token, URL chứa bí mật và đường dẫn thư mục người dùng không thấy gì.

### 3. Cấu trúc và nơi skill chạy

Cấu trúc trong repo: `skills/<tên>/SKILL.md`, kèm `references/`, `scripts/`, `evals/`. Trình cài tự tìm thấy `skills/<tên>/SKILL.md`. Xem trước bằng `npx skills add <chủ-sở-hữu>/<repo> --list`.

| Nền tảng | Skill vào bằng cách nào |
|---|---|
| Claude Code | Thư mục `~/.claude/skills/<name>/SKILL.md` (cá nhân), `.claude/skills/<name>/SKILL.md` (dự án) hoặc plugin. Không cần tải lên. |
| Claude.ai | Tải lên tệp zip trong phần cài đặt. Skill tùy biến cần gói Pro, Max, Ultra, Team hoặc Enterprise và bật code execution. |
| Claude API | Tải lên qua `/v1/skills`, rồi liệt kê `skill_ids` trong tham số `container` cùng công cụ code execution. Dùng chung cả workspace; container không có mạng. |
| Agent SDK | Tệp trên đĩa trong `.claude/skills/`, được tìm qua `settingSources` và tùy chọn `skills`. |
| OpenMausBot | Thư mục `workspaces/<botId>/skills/<name>/SKILL.md`, thuộc về một bot. |

Skill tùy biến không đồng bộ giữa các nền tảng Claude: tải lên hoặc sao chép riêng cho từng nơi. Đã đối chiếu tài liệu chính thức ngày 2026-11-18.

Việc nhập mang theo những gì (chưa kiểm chứng, theo kinh nghiệm của chủ sở hữu): nhập qua tệp nhóm `team.md` chỉ mang SKILL.md; nhập từ GitHub mang cả `references/` và `scripts/`. Coi cả hai là chưa được chứng minh cho đến khi kiểm một lần nhập thật. Vì trường hợp đầu, mọi SKILL.md phải chạy được một mình; nói cho người dùng biết tệp nào sẽ mất nếu chỉ SKILL.md đi theo.

Xong khi: cấu trúc đã liệt kê và đường đi của nền tảng đích được nêu kèm giới hạn.

### 4. Phiên bản và changelog

PATCH: sửa chữ hoặc lỗi chính tả, hành vi không đổi. MINOR: thêm phần, script hoặc tham chiếu; cách dùng cũ vẫn chạy. MAJOR: đổi tên bước, đổi định dạng đầu ra, xóa trường, hoặc chia một skill thành nhiều skill. Phân vân giữa hai mức thì chọn mức cao hơn. Mỗi lần tăng phiên bản viết một mục:

```markdown
## v<X.Y.Z> - <YYYY-MM-DD>

**Bump:** PATCH | MINOR | MAJOR
**Backward compatible:** yes | no
**Driver:** <một dòng: lỗi hoặc yêu cầu gây ra thay đổi>

### Changes
- Added / Changed / Removed / Fixed: <nội dung>

### Migration
<"none" cho PATCH và MINOR; với MAJOR, hướng dẫn chính xác>

### Rollback
<tag hoặc commit để quay lại>
```

Giữ lịch sử trong `CHANGELOG.md` ở gốc repo hoặc trong ghi chú phát hành. SKILL.md chỉ mang `metadata.version` hiện tại. Mẫu dài: [changelog-template.md](changelog-template.md).

Xong khi: phiên bản đã đặt trong `metadata.version` và mục changelog đã có.

### 5. Cổng và xuất bản

Cho người dùng xem danh sách tệp, phiên bản, kết quả của bộ kiểm tra và lệnh cài. Chỉ xuất bản sau khi được duyệt; cài hộ người dùng là một lần đồng ý riêng. Người dùng cài bằng `npx skills add <chủ-sở-hữu>/<repo>` (`--skill <tên>` cho một skill, `-g` để cài toàn cục).

Xong khi: người dùng đã duyệt, và bản xem trước `--list` hiện skill.

## Bàn giao (handoff)

Khi chuyển việc cho bot khác hoặc người dùng, gửi 5 trường theo thứ tự: Goal (mục tiêu, một câu), Inputs (đầu vào đính kèm hoặc liên kết), Deliverable (sản phẩm: tên tệp hoặc nội dung trực tiếp), Done when (tiêu chí hoàn thành kiểm tra được), Open items (câu hỏi, rủi ro, việc chưa làm).

## Đọc thêm khi cần

- [changelog-template.md](changelog-template.md): mẫu changelog đầy đủ kèm một mục ví dụ. Đọc khi viết mục MAJOR.
- `scripts/validate_skill.py`: trình kiểm tra ở bước 1. Các quy tắc kiểm tay ở trên thay thế nó khi thiếu script.

## Nguồn

- Đặc tả Agent Skills: https://agentskills.io/specification
- Anthropic, "Agent Skills overview" (nền tảng, phạm vi chia sẻ): https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
- Claude Code, "Extend Claude with skills": https://code.claude.com/docs/en/skills
- Claude Agent SDK, "Extend agents with skills": https://code.claude.com/docs/en/agent-sdk/skills
- vercel-labs/skills (`npx skills`): https://github.com/vercel-labs/skills
