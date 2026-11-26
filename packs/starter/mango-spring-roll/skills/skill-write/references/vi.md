# Viết skill (bản tiếng Việt)

Bản tiếng Việt của `SKILL.md`. Soạn một thư mục skill: viết mô tả (description) trước, rồi đến phần thân. Nhận bản tóm tắt tiếp nhận và kết luận "làm" (xem skill-search). Giao ra một thư mục sẵn sàng cho skill-test.

Trả lời theo ngôn ngữ của người dùng. Người dùng Việt nhận đầu ra tiếng Việt, kèm thuật ngữ tiếng Anh trong ngoặc ở lần dùng đầu.

**Cổng (gate)** là điểm dừng để người dùng duyệt trước khi làm tiếp. Cổng ở đây: trước khi ghi đè một thư mục skill đang có.

## Định tuyến

| Người dùng muốn | Dùng |
|---|---|
| Viết hoặc cấu trúc lại description, SKILL.md | skill này |
| Làm skill từ một chủ đề, chưa có quy trình hay ghi chú | skill này, [references/from-topic.md](from-topic.md) (bản tiếng Anh) |
| Biết trước đã có skill chưa hoặc có đáng làm không | skill-search |
| Kiểm thử, nền so với chạy lại | skill-test |
| Chấm, chia hoặc gộp skill có sẵn | skill-review |
| Kiểm tra theo chuẩn, phiên bản, xuất bản | skill-package |

Khi skill tương ứng chưa được cài, nói một dòng rằng nó chưa có, rồi làm xong phần việc có thể làm ở đây.

## Các bước

### 1. Cỡ skill và loại

| Cỡ | Dùng khi | Cấu trúc |
|---|---|---|
| đơn giản (simple) | một ý, khoảng 200 dòng trở xuống | chỉ `SKILL.md` |
| mở rộng (expanded) | nhiều chủ đề nhỏ, mẫu biểu, ví dụ dài | `SKILL.md` cộng `references/` |
| nền tảng (platform) | một lĩnh vực có nhiều mảng riêng | `SKILL.md` làm bộ định tuyến, mỗi mảng một `references/<mảng>.md`, `scripts/` cho việc tất định |

Bắt đầu từ cỡ nhỏ nhất đủ chứa quy trình. Đồng thời xác định loại skill, vì loại quyết định kiểu kiểm thử: kỹ thuật (how-to), tham chiếu (tra cứu), kỷ luật (quy tắc phải giữ dưới áp lực), mẫu tư duy (pattern).

Một skill chỉ làm một việc mà người dùng thật sự gõ ra. Khi bản nháp chứa hai việc có câu kích hoạt khác nhau, hãy viết thành hai skill (xem skill-review).

Xong khi: đã ghi lại cỡ, loại và một việc duy nhất của skill.

### 2. Viết description trước

Description là đoạn văn duy nhất của skill luôn được nạp vào ngữ cảnh, nên chỉ nó quyết định skill có kích hoạt hay không. Soạn nó trước phần thân.

- Một dòng, tối đa 1024 ký tự, không có dấu nháy kép, không có chuỗi `: ` (làm hỏng YAML thường).
- Mở đầu bằng skill làm gì (động từ trước), rồi `Use when` kèm 3-6 tình huống khác nhau của người dùng, với những từ khóa người dùng thực sự gõ, kể cả khi họ không nêu tên lĩnh vực.
- Nêu kết quả và tình huống kích hoạt. Để danh sách bước trong phần thân: agent đọc tóm tắt bước ở description thường làm theo đó mà bỏ qua phần thân.
- Khi có skill anh em gần giống, thêm một mệnh đề ngắn `Not for` nêu việc nào thuộc về skill kia. Hai description không bao giờ được cùng nhận một câu.
- Kết thúc bằng 4-8 từ khóa kích hoạt bằng ngôn ngữ người dùng (tiếng Việt có dấu).
- Bỏ các từ quá chung ("giúp", "việc"): chúng kích hoạt nhầm mọi thứ.

Xong khi: người chưa đọc phần thân vẫn hiểu đúng description, và skill-test chạy được trên nó.

### 3. Bản nháp quy trình (khi bắt đầu từ SOP hoặc ghi chú)

Soạn các bước trước khi viết SKILL.md. Mỗi bước có Input (đầu vào), Action (hành động), Output (kết quả kiểm tra được) và Gate (cổng): `auto` (rủi ro thấp, dễ hoàn tác), `confirm` (lựa chọn ảnh hưởng các bước sau), `stop` (khó đảo ngược: xuất bản, gửi, xóa, chi tiền, cài đặt). Mặc định là auto. Nhắm 5-10 bước; nhiều hơn nghĩa là nên tách hai skill hoặc đưa vào tệp tham chiếu. Thêm một trường hợp biên và một ví dụ minh họa. Mẫu đầy đủ và danh mục kiểm chất lượng: [workflow-template.md](workflow-template.md); đọc khi bước 3 bắt đầu từ ghi chú thô.

Xong khi: mỗi bước có Input, một Action nêu công cụ hay phương pháp cụ thể, và một Output kiểm tra được.

### 4. Phần thân

1. **Bước đi trước.** Đánh số, mỗi bước kết thúc bằng một dòng "Xong khi" kiểm tra được. Phần tham chiếu (bảng, quy tắc) đặt sau các bước.
2. **Chỉ thêm điều agent còn thiếu.** Với mỗi dòng hãy hỏi: không có dòng này agent có làm sai không? Nếu không thì cắt. Bẫy thường gặp và quy ước bất thành văn đặt trong SKILL.md.
3. **Một mặc định**, kèm lối thoát ngắn, thay cho một thực đơn lựa chọn.
4. **Câu lệnh khẳng định.** Nêu hành vi mong muốn. Chỉ giữ điều cấm như lan can cứng, đi kèm việc cần làm thay thế. Nêu lý do cho các bước dễ hỏng.
5. **SKILL.md tự đủ.** Một số nền tảng chỉ nhập SKILL.md, không nhập `references/` hay `scripts/`. Mọi bước cần cho một lần chạy nằm trong SKILL.md; `references/` chỉ chứa phần chiều sâu tùy chọn, mỗi tệp ghi rõ điều kiện để đọc, và SKILL.md giữ một bản tóm tắt ngắn vẫn dùng được khi thiếu tệp đó.
6. **Chỉ sâu một tầng.** SKILL.md liên kết tới tệp; các tệp đó không liên kết tiếp. Dùng đường dẫn tương đối từ gốc skill.
7. **Script chỉ cho việc tất định** (kiểm tra, phân tích cú pháp, chuyển đổi). Chỉ thư viện chuẩn, không hỏi tương tác, có `--help`, báo lỗi rõ, thoát mã khác 0 khi thất bại. Skill nêu cách làm tay khi thiếu script.
8. **Không bao giờ để thông tin xác thực trong thư mục skill.** Khóa API, token, URL webhook, mật khẩu và ghi chú đăng nhập thuộc về kho bí mật hoặc kết nối của nền tảng. Skill chỉ gọi tên kết nối ("dùng kết nối đã lưu tên X") và không lưu gì thêm.
9. **Dòng định tuyến và bàn giao.** Khi skill có anh em, thêm một bảng định tuyến ngắn nói rõ phải làm gì khi thiếu skill anh em. Kết thúc bằng mẫu bàn giao 5 trường (bên dưới).
10. Markdown thuần. Nhắm dưới 300 dòng cho SKILL.md; không vượt quá 500.

Xong khi: mỗi bước có tiêu chí hoàn thành, mọi liên kết trỏ đúng, và người đọc chạy được skill chỉ từ SKILL.md.

### 5. Tự kiểm, rồi chuyển tiếp

Kiểm tay: `name` viết thường, gạch ngang đơn và trùng tên thư mục; description một dòng, không rỗng, tối đa 1024 ký tự; SKILL.md dưới 500 dòng; liên kết trỏ đúng; không có đường dẫn cục bộ tuyệt đối. Sau đó chuyển cho skill-test, và cho skill-package để chạy bộ kiểm tra đầy đủ.

Xong khi: thư mục đã có, tự kiểm đạt và bàn giao đã gửi.

## Bàn giao (handoff)

Khi chuyển việc cho bot khác hoặc người dùng, gửi 5 trường theo thứ tự: Goal (mục tiêu, một câu), Inputs (đầu vào đính kèm hoặc liên kết), Deliverable (sản phẩm: tên tệp hoặc nội dung trực tiếp), Done when (tiêu chí hoàn thành kiểm tra được), Open items (câu hỏi, rủi ro, việc chưa làm).

## Nguồn

- Anthropic, "Skill authoring best practices": https://docs.claude.com/en/docs/agents-and-tools/agent-skills/best-practices
- Đặc tả Agent Skills: https://agentskills.io/specification
- Chỉnh từ các mẫu distill-to-skill của Masonshare.
