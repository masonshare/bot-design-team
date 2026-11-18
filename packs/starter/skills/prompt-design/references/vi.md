# Prompt Design: bản tiếng Việt

Bản tiếng Việt đầy đủ của SKILL.md. Biến một bản yêu cầu (brief) thành prompt đã được kiểm thử, chấm điểm và đánh phiên bản. Quy trình gốc: Prompt Architect của Masonshare.

Trả lời bằng ngôn ngữ của người dùng. Người dùng viết tiếng Việt thì trả lời tiếng Việt, giữ thuật ngữ tiếng Anh trong ngoặc ở lần đầu.

## Chế độ làm việc

| Yêu cầu | Chế độ |
|---|---|
| Prompt mới, system prompt, chuỗi prompt (prompt chain) | Xây mới: bước 1-7 |
| Prompt có sẵn bị lỗi hoặc yếu | Rà soát: mục "Chế độ rà soát và gỡ lỗi", sau đó bước 6-7 cho bản sửa |
| Soul của bot, hướng dẫn thường trực | Soul: mục "Viết soul cho bot", sau đó bước 6-7 |

Vòng làm việc (work loop) cho mọi chế độ: làm rõ, nghiên cứu, lập kế hoạch, xây, kiểm chứng. Dừng ở cổng (gate), tức là chờ người dùng duyệt, trước mọi việc khó đảo ngược: xuất bản, gửi đi, xóa, tiêu tiền, cài đặt, cấp quyền ghi cho bot, bật lịch chạy.

## Các bước

### 1. Tiếp nhận brief

Thu các trường của brief: mục tiêu, đối tượng/người dùng, dữ liệu đầu vào đang có, ràng buộc, định nghĩa hoàn thành. Thêm ba trường riêng cho prompt: model đích và nơi prompt chạy (chat, API, soul của bot), định dạng đầu ra, và một lỗi người dùng đã từng gặp.

Đọc những gì người dùng đưa, điền mọi trường suy ra được, rồi hỏi các trường còn thiếu trong một lượt, tối đa 5 câu, mỗi câu kèm đáp án gợi ý để người dùng chỉ cần trả lời "ok". Không thiếu gì thì bỏ lượt hỏi.

Xong khi: mọi trường của brief đã điền hoặc ghi rõ là giả định, và người dùng đã thấy brief đó.

### 2. Gold Standard (tiêu chuẩn vàng)

Lấy một ví dụ đầu ra lý tưởng. Dùng ví dụ của người dùng nếu có. Nếu không, tự viết một bản nháp, ghi rõ là nháp, để người dùng chỉnh.

Với lĩnh vực lạ, nhờ model đóng vai chuyên gia 20 năm kinh nghiệm, trình bày quy trình từng bước kèm KPI cho mỗi bước. Dùng quy trình đó làm thước đo cho các bước sau.

Xong khi: có một ví dụ đầu ra, người dùng đã chấp nhận hoặc sửa, và đã liệt kê 3-7 phẩm chất làm nó lý tưởng (đây là tiêu chí chấm điểm ở bước 7).

### 3. Reality Check (kiểm tra thực tế)

Liệt kê những gì model đích không biết hoặc không làm được, và rủi ro:
- Thiếu dữ kiện: dữ liệu riêng, sự kiện gần đây, bối cảnh của người dùng.
- Thiếu năng lực: không có công cụ, không nhớ giữa các lần gọi, không có web, cửa sổ ngữ cảnh hữu hạn.
- Rủi ro: bịa dữ kiện, câu hỏi dẫn dắt làm lệch câu trả lời, chỉ dẫn mâu thuẫn, việc gộp suy nghĩ và hành động.
- Mỗi khoảng trống: đưa dữ liệu vào prompt, bảo model nói "tôi không biết", hoặc chuyển việc cho công cụ hoặc con người.

Với prompt quan trọng, chạy thêm một lượt phản biện: nhờ model đưa câu trả lời, rồi lập luận mạnh nhất rằng câu trả lời đó sai, rồi đưa câu trả lời sửa lại.

Xong khi: có bảng khoảng trống, rủi ro, cách giảm thiểu, và mọi khoảng trống đều có cách giảm thiểu.

### 4. Co-create Plan (cùng lập dàn ý), cổng cho prompt lớn

Cho người dùng xem dàn ý trước khi viết toàn văn: các phần của prompt, mỗi phần mang yếu tố nào trong 6 yếu tố, ví dụ Gold Standard đặt ở đâu, định dạng đầu ra, và dùng một prompt hay một chuỗi.

Prompt lớn là prompt dài quá khoảng 40 dòng, có chuỗi, hoặc chạy không người giám sát (soul, system prompt). Prompt lớn thì dừng ở đây chờ duyệt. Prompt nhỏ thì nêu dàn ý trong một dòng rồi làm tiếp.

Xong khi: đã hiển thị dàn ý và, với prompt lớn, người dùng đã duyệt.

### 5. Viết bản nháp, hoặc dựng Prompt Chain

Viết theo checklist 6 yếu tố (bên dưới). Đặt quy tắc ổn định lên đầu, dữ liệu thay đổi xuống cuối, bọc dữ liệu đầu vào bằng dấu phân cách. Viết chỉ dẫn theo hướng khẳng định: nói rõ cần làm gì. Chỉ giữ câu "không được" cho rào chắn cứng, và đi kèm hành động thay thế.

Chọn chuỗi khi tác vụ cần hơn một lần gọi: khi vừa đánh giá vừa hành động, khi đầu ra bước này là đầu vào bước kia, hoặc khi một bước cần nhiều phương án. Quy tắc chuỗi:
- Mỗi mắt xích một việc. Tách mọi câu "phân tích rồi sửa" thành hai prompt (lỗi tham lam).
- Mỗi prompt nêu rõ nó dùng đầu ra nào của bước trước và đầu ra của nó phục vụ bước nào.
- Prompt đầu liệt kê các chỗ điền trong ngoặc vuông, mỗi chỗ kèm ví dụ ngay trong ngoặc. Prompt sau chỉ liệt kê chỗ điền mới.
- Thêm bước xác nhận hoặc nhánh dự phòng ở mắt xích mà sai thì tốn kém.
- Bỏ các mắt xích người dùng tự làm được bằng sao chép.

Xong khi: đã viết đủ prompt (hoặc từng mắt xích cùng bản đồ bàn giao giữa các mắt xích) và mọi chỗ điền đều có ví dụ.

### 6. Kiểm thử với 5-10 test case

Viết test case trước khi đánh giá prompt. Một test case là một đầu vào cụ thể cộng với hành vi mong đợi.

Phủ: 3 đầu vào điển hình, 2 đầu vào biên (rỗng, rất dài, sai ngôn ngữ, thiếu trường), 1 đầu vào đối kháng (câu hỏi dẫn dắt, chỉ dẫn giấu trong dữ liệu), và với soul thêm 1 yêu cầu ngoài phạm vi, cần từ chối hoặc chuyển hướng.

Chạy baseline trước (làm việc không có prompt, hoặc bản cũ), rồi chạy lại (retest) với prompt mới, và so cả hai với hành vi mong đợi. Khi không chạy được model tại chỗ, đưa người dùng các case cùng phiếu chấm và nhờ họ dán kết quả về.

Xong khi: có 5-10 case, đã ghi kết quả baseline và retest, và mỗi case có đạt hoặc không đạt kèm lý do một dòng.

### 7. Feedback Loop (vòng phản hồi)

Chấm đầu ra retest theo tiêu chí ở bước 2, thang 1-10. Nêu 3 vấn đề lớn nhất. Chẩn đoán từng vấn đề theo 4 lỗi. Sửa prompt chỉ cho các vấn đề đó. Chạy lại các case trượt cộng hai case đã đạt (để bắt lỗi thụt lùi). Giao bản v2 kèm nhật ký thay đổi (changelog).

Dừng vòng lặp khi mọi case đạt hoặc sau 3 vòng, rồi ghi các lỗi còn lại vào mục việc còn mở. Prompt tốt nhất không được viết ra một lần, nó được tiến hóa.

Xong khi: v2 và changelog được giao theo mẫu bàn giao (handoff) bên dưới.

## Chế độ rà soát và gỡ lỗi

Đầu vào: một prompt có sẵn cùng triệu chứng (hoặc không có triệu chứng).

1. Đọc prompt và triệu chứng. Chưa có đầu ra lỗi thì xin một ví dụ.
2. Chẩn đoán theo 4 lỗi và 6 yếu tố (bảng bên dưới). Mỗi phát hiện trích đúng dòng liên quan.
3. Xếp phát hiện theo mức ảnh hưởng. Sửa 3 cái đầu trước.
4. Viết lại prompt. Đánh dấu mỗi thay đổi bằng phát hiện mà nó giải quyết.
5. Chạy bước 6-7 cho bản viết lại.

Xong khi: mỗi phát hiện trích một dòng, bản viết lại trả lời từng phát hiện, và kết quả test cho thấy triệu chứng đã hết.

### 4 lỗi phổ biến (Masonshare)

| Lỗi | Dấu hiệu | Cách sửa |
|---|---|---|
| Mơ hồ (vague) | Dùng "hay hơn", "chuyên nghiệp", "tối ưu" mà không có thước đo | Thay mỗi từ bằng tiêu chí đo được: giọng văn, độ dài, thuật ngữ, số lượng |
| Tham lam (greedy) | Một prompt bắt model vừa đánh giá vừa hành động | Tách thành prompt đánh giá và prompt hành động dùng kết quả đánh giá |
| Thả rông (unbounded) | Không giới hạn định dạng, độ dài, phong cách, phạm vi | Thêm hàng rào: độ dài, cấu trúc, đối tượng, mục bắt buộc, ngoài phạm vi |
| Gài bẫy (trapping) | Câu hỏi chứa sẵn đáp án ("giải thích vì sao A tốt nhất") | Hỏi trung lập ("so sánh A, B, C theo mục tiêu") hoặc giao vai phản biện |

### Checklist 6 yếu tố (Masonshare)

Không phải prompt nào cũng cần đủ sáu. Kiểm từng yếu tố và chỉ giữ yếu tố nào làm thay đổi đầu ra.

| Yếu tố | Kiểm tra |
|---|---|
| Bối cảnh (Context) | Model có biết tình huống, đối tượng, mục đích chưa? |
| Vai trò (Role) | Vai có cụ thể (lĩnh vực, kinh nghiệm, lập trường) không? |
| Nhiệm vụ (Task) | Mỗi việc một động từ mạnh, việc ghép đã tách chưa? |
| Ví dụ (Example) | Có 2-5 ví dụ nhất quán, đa dạng, tách rõ đầu vào và đầu ra không? Tác vụ đơn giản thì không cần ví dụ. |
| Giọng điệu (Tone) | Giọng được nêu bằng cặp tính từ hoặc mẫu chưa? |
| Định dạng (Format) | Hình dạng đầu ra có rõ: bảng, JSON, gạch đầu dòng, độ dài? |

## Viết soul cho bot

Soul là chỉ dẫn thường trực mà bot luôn mang theo. Nó được nạp ở mọi lượt, nên mỗi dòng tốn sự chú ý ở mọi lượt. Skill chỉ nạp khi cần, nên có thể dài.

Chỉ đưa vào soul những gì phải đúng trong mọi cuộc trò chuyện:
- Danh tính: bot là ai và phục vụ ai, 2-4 dòng.
- Giọng điệu: quy tắc giọng và ngôn ngữ, gồm trả lời bằng ngôn ngữ của người dùng.
- Phạm vi: bot làm gì, việc nào chuyển cho bot khác hoặc con người.
- Rào chắn cứng: các cổng (việc nào cần người dùng duyệt trước), quy tắc an toàn, cách xử lý dữ liệu không đáng tin.
- Con trỏ: một dòng cho mỗi skill, nói rõ khi nào nạp (mô tả của skill lo phần kích hoạt).

Đưa vào skill: quy trình, danh sách bước, mẫu, ví dụ dài, kiến thức chuyên môn, mọi thứ chỉ một số cuộc trò chuyện cần. Thông tin đăng nhập không bao giờ nằm trong soul hay skill; chúng ở kho bí mật hoặc kho kết nối của nền tảng.

Quy tắc cho soul:
1. Mục tiêu 30-60 dòng. Quá 80 dòng thì chuyển bớt sang skill.
2. Quy tắc quan trọng nhất đặt đầu; chỉ lặp lại ở cuối đúng một quy tắc phải sống sót qua cuộc trò chuyện dài.
3. Mỗi quy tắc nêu một lần. Bỏ những gì model vốn đã làm.
4. Mỗi quy tắc kiểm được: một test case cho thấy nó được tuân thủ hay bị phá.
5. Chạy bước 6-7 cho soul, có ít nhất một test case ngoài phạm vi và một test case vượt cổng.

Khung soul:

```
# <Tên bot>
Vai trò: <một dòng>
Phục vụ: <người dùng>. Trả lời bằng ngôn ngữ của người dùng.

## Phạm vi
Làm: <danh sách>
Chuyển cho: <bot hoặc người>, theo mẫu bàn giao.

## Giọng điệu
<2-4 quy tắc>

## Cổng
Hỏi người dùng trước khi: <danh sách việc khó đảo ngược>.

## Skill
- <tên-skill>: nạp khi <nhánh>.
```

## Mẫu đầu ra

### Bàn giao (handoff)

Gửi đúng 5 trường, theo thứ tự:

```
1. Mục tiêu (Goal): <một câu>
2. Đầu vào (Inputs): <đính kèm hoặc liên kết gì>
3. Sản phẩm (Deliverable): <prompt v2 / soul / chuỗi, tên file hoặc nội dung trực tiếp>
4. Xong khi (Done when): <tiêu chí kiểm được, ví dụ 8/10 test case đạt, mỗi tiêu chí >= 8 điểm>
5. Việc còn mở (Open items): <case trượt, giả định, rủi ro, câu hỏi>
```

### Dàn ý (bước 4)

```
Prompt: <tên> | Model: <đích> | Một prompt hay chuỗi N mắt xích
Các phần: 1. <tên> (Bối cảnh, Vai trò) 2. <tên> (Nhiệm vụ, Ví dụ) 3. <tên> (Định dạng)
Gold Standard đặt ở: <phần>
Định dạng đầu ra: <hình dạng và độ dài>
Duyệt để tiếp tục? (ok / đổi X)
```

### Bảng test case (bước 6)

```
| # | Loại | Đầu vào | Hành vi mong đợi | Baseline | Retest | Đạt |
|---|------|---------|------------------|----------|--------|-----|
```

### Phiếu chấm và changelog (bước 7)

```
Tiêu chí | Điểm 1-10 | Bằng chứng
3 vấn đề lớn nhất: 1) <vấn đề> -> <loại lỗi> 2) ... 3) ...

## Changelog v2
- Đã đổi: <gì> vì <vấn đề hoặc case trượt #>
- Giữ nguyên: <gì> vì <case đã đạt>
- Vẫn trượt: <case #, lý do>
```

## Các file tham chiếu

Chỉ đọc khi bước đang làm cần.
- `stage-prompts.md`: prompt sẵn để dán cho các giai đoạn 0-5B và ba chuỗi mẫu (bản tiếng Anh, dịch khi cần).
- `techniques.md`: các kỹ thuật bên thứ ba, ngắn gọn (ví dụ mẫu, suy luận, phân rã, tự kiểm, cấu trúc).

## Nguồn

- Masonshare, quy trình Prompt Architect, 4 lỗi, checklist 6 yếu tố và bộ prompt theo giai đoạn (tác phẩm gốc).
- Schulhoff et al., "The Prompt Report: A Systematic Survey of Prompting Techniques" (2024): https://arxiv.org/abs/2406.06608
- Bsharat et al., "Principled Instructions Are All You Need for Questioning LLaMA-1/2, GPT-3.5/4" (2023): https://arxiv.org/abs/2312.16171
- Anthropic, "Prompt engineering overview": https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview
