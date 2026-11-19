# Bot Soul: bản tiếng Việt

Bản tiếng Việt của SKILL.md. Viết, rút gọn hoặc rà soát soul của bot.

Trả lời bằng ngôn ngữ của người dùng. Người dùng viết tiếng Việt thì trả lời tiếng Việt, giữ thuật ngữ tiếng Anh trong ngoặc ở lần đầu.

Soul luôn là prompt lớn vì chạy không người giám sát: dừng ở dàn ý (bước 3), chờ duyệt.

## Các bước

### 1. Tiếp nhận

Hỏi một lượt, mỗi câu kèm đáp án gợi ý: tên và vai trò bot, phục vụ ai, ngôn ngữ, làm gì và chuyển gì cho bot khác hoặc người, việc khó đảo ngược cần duyệt, các skill bot mang theo, một lỗi đã gặp (nếu rà soát). Tối đa 5 câu. Với soul có sẵn, lấy bản hiện tại trước.

### 2. Phân loại: soul hay skill

Chỉ đưa vào soul những gì phải đúng trong mọi cuộc trò chuyện:
- Danh tính: bot là ai và phục vụ ai, 2-4 dòng.
- Giọng điệu: quy tắc giọng và ngôn ngữ, gồm trả lời bằng ngôn ngữ của người dùng.
- Phạm vi: bot làm gì, việc nào chuyển cho bot khác hoặc con người.
- Rào chắn cứng: các cổng (việc nào cần người dùng duyệt trước), quy tắc an toàn, cách xử lý dữ liệu không đáng tin.
- Con trỏ: một dòng cho mỗi skill, nói rõ khi nào nạp (mô tả của skill lo phần kích hoạt).

Đưa vào skill: quy trình, danh sách bước, mẫu, ví dụ dài, kiến thức chuyên môn, mọi thứ chỉ một số cuộc trò chuyện cần. Thông tin đăng nhập không bao giờ nằm trong soul hay skill; chúng ở kho bí mật hoặc kho kết nối của nền tảng.

### 3. Dàn ý (cổng)

Cho xem danh sách phần và ngân sách số dòng trước khi viết, rồi chờ duyệt.

### 4. Viết bản nháp

Quy tắc cho soul:
1. Mục tiêu 30-60 dòng. Quá 80 dòng thì chuyển bớt sang skill.
2. Quy tắc quan trọng nhất đặt đầu; chỉ lặp lại ở cuối đúng một quy tắc phải sống sót qua cuộc trò chuyện dài.
3. Mỗi quy tắc nêu một lần. Bỏ những gì model vốn đã làm.
4. Mỗi quy tắc kiểm được: một test case cho thấy nó được tuân thủ hay bị phá.
5. Viết khẳng định; chỉ giữ câu "không được" cho rào chắn cứng và kèm hành động thay thế.

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

### 5. Kiểm tra nhanh và bàn giao

Chạy soul trên 3 tin nhắn: một trong phạm vi, một ngoài phạm vi (cần từ chối hoặc chuyển hướng), một vượt cổng (cần hỏi trước khi làm). Sửa chỗ trượt. Muốn 5-10 case và changelog thì chuyển cho prompt-test. Áp soul vào bot là một cổng: cho xem bản cuối và chờ duyệt trước khi cài hoặc thay thế.

Bàn giao đúng 5 trường: Mục tiêu, Đầu vào, Sản phẩm, Xong khi, Việc còn mở.
