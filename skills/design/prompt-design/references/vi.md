# Prompt Design: bản tiếng Việt

Bản tiếng Việt của SKILL.md. Viết một prompt mới từ brief. Quy trình gốc: Prompt Architect của Masonshare.

Trả lời bằng ngôn ngữ của người dùng. Người dùng viết tiếng Việt thì trả lời tiếng Việt, giữ thuật ngữ tiếng Anh trong ngoặc ở lần đầu.

## Định tuyến

| Người dùng muốn | Dùng |
|---|---|
| Một prompt mới cho một việc | skill này |
| Sửa hoặc rà soát prompt đã có | prompt-review |
| Việc nhiều bước, đầu ra bước này nuôi bước sau | prompt-chain |
| Soul hoặc system prompt của bot hay trợ lý chạy lâu dài | bot-soul |
| Test case, chấm điểm, baseline và retest, changelog v2 | prompt-test |

Vòng làm việc: làm rõ, nghiên cứu, lập kế hoạch, xây, kiểm chứng. Dừng ở cổng (chờ người dùng duyệt) trước mọi việc khó đảo ngược: xuất bản, gửi đi, xóa, tiêu tiền, cài đặt.

### 1. Tiếp nhận brief

Thu các trường của brief: mục tiêu, đối tượng/người dùng, dữ liệu đầu vào đang có, ràng buộc, định nghĩa hoàn thành. Thêm ba trường riêng cho prompt: model đích và nơi prompt chạy (chat, API, soul của bot), định dạng đầu ra, và một lỗi người dùng đã từng gặp.

Đọc những gì người dùng đưa, điền mọi trường suy ra được, rồi hỏi các trường còn thiếu trong một lượt, tối đa 5 câu, mỗi câu kèm đáp án gợi ý để người dùng chỉ cần trả lời "ok". Không thiếu gì thì bỏ lượt hỏi.

Xong khi: mọi trường của brief đã điền hoặc ghi rõ là giả định, và người dùng đã thấy brief đó.

### 2. Gold Standard (tiêu chuẩn vàng)

Lấy một ví dụ đầu ra lý tưởng. Dùng ví dụ của người dùng nếu có. Nếu không, tự viết một bản nháp, ghi rõ là nháp, để người dùng chỉnh.

Với lĩnh vực lạ, nhờ model đóng vai chuyên gia 20 năm kinh nghiệm, trình bày quy trình từng bước kèm KPI cho mỗi bước. Dùng quy trình đó làm thước đo cho các bước sau.

Xong khi: có một ví dụ đầu ra, người dùng đã chấp nhận hoặc sửa, và đã liệt kê 3-7 phẩm chất làm nó lý tưởng (đây là tiêu chí chấm điểm trong prompt-test).

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

### 5. Viết bản nháp

Viết theo checklist 6 yếu tố (bên dưới). Đặt quy tắc ổn định lên đầu, dữ liệu thay đổi xuống cuối, bọc dữ liệu đầu vào bằng dấu phân cách. Viết chỉ dẫn theo hướng khẳng định: nói rõ cần làm gì. Chỉ giữ câu "không được" cho rào chắn cứng, và đi kèm hành động thay thế.

Chỉ đưa kỹ thuật ngoài 6 yếu tố vào khi test cho thấy prompt thường chưa đủ. Chi tiết kỹ thuật: xem references/techniques.md (bản tiếng Anh).

Xong khi: đã viết đủ prompt và mọi chỗ điền trong ngoặc vuông đều có ví dụ.

### 6. Kiểm tra nhanh và bàn giao

Chạy bản nháp trên 3 đầu vào: một điển hình, một biên (rỗng, rất dài, thiếu trường), một đối kháng (câu hỏi dẫn dắt hoặc chỉ dẫn giấu trong dữ liệu). Sửa chỗ trượt. Muốn vòng đầy đủ 5-10 case, baseline, retest và changelog thì chuyển cho prompt-test.

Bàn giao đúng 5 trường, theo thứ tự: Mục tiêu, Đầu vào, Sản phẩm, Xong khi, Việc còn mở. Mọi giả định ghi là giả định, mọi điều chưa thử ghi là chưa thử.

Xong khi: 3 lần kiểm tra đã ghi đạt hoặc không đạt và đã gửi bàn giao.

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

### Dàn ý (bước 4)

```
Prompt: <tên> | Model: <đích> | Một prompt hay chuỗi N mắt xích
Các phần: 1. <tên> (Bối cảnh, Vai trò) 2. <tên> (Nhiệm vụ, Ví dụ) 3. <tên> (Định dạng)
Gold Standard đặt ở: <phần>
Định dạng đầu ra: <hình dạng và độ dài>
Duyệt để tiếp tục? (ok / đổi X)
```

### Bàn giao (handoff)

Gửi đúng 5 trường, theo thứ tự:

```
1. Mục tiêu (Goal): <một câu>
2. Đầu vào (Inputs): <đính kèm hoặc liên kết gì>
3. Sản phẩm (Deliverable): <prompt v2 / soul / chuỗi, tên file hoặc nội dung trực tiếp>
4. Xong khi (Done when): <tiêu chí kiểm được, ví dụ 8/10 test case đạt, mỗi tiêu chí >= 8 điểm>
5. Việc còn mở (Open items): <case trượt, giả định, rủi ro, câu hỏi>
```
