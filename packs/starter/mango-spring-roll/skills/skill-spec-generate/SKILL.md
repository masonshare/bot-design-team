---
name: skill-spec-generate
description: Viết tệp ghi chú thiết kế cho một skill vừa tạo (vì sao tồn tại, các quyết định kiến trúc, ngưỡng số, đánh đổi, khi nào xem lại), tách khỏi thư mục skill để không tốn ngữ cảnh khi skill chạy. Dùng khi vừa làm xong một skill, hoặc khi hỏi "ghi lại lý do thiết kế skill này", "viết ghi chú thiết kế cho skill X", "bổ sung spec cho skill cũ". English - write a design-notes file for a finished skill (why it exists, architecture decisions, thresholds, tradeoffs, when to revisit), kept outside the skill folder so it never loads at runtime.
---

# Ghi chú thiết kế cho skill

`SKILL.md` là phần cho AI đọc khi chạy: làm gì, làm thế nào. Ghi chú thiết kế là phần cho **người** đọc: vì sao làm vậy, đã đánh đổi gì. Hai thứ phải tách ra. Ghi chú này **không nằm trong thư mục skill** và không được nạp vào ngữ cảnh khi skill chạy; người ta chỉ mở nó khi gỡ lỗi, rà soát, chỉnh ngưỡng, hoặc bàn giao.

## Đầu vào

Cần đường dẫn đến thư mục skill. Không có thì hỏi. Hỏi luôn nơi lưu ghi chú; mặc định là một tệp `<tên-skill>.notes.md` nằm cạnh thư mục skill, không nằm trong đó. Nếu dự án có trang tài liệu riêng cho từng skill thì đề nghị đặt ghi chú vào đó.

## Quy trình

### Bước 1. Tự điền phần suy ra được

Đọc `SKILL.md` (tên, mô tả), cây thư mục (tệp tham chiếu, tập lệnh, mẫu), và phần hội thoại gần đây (bài toán, chỗ cân nhắc, lý do chọn ngưỡng). Rồi điền ba mục:

1. **Vì sao skill tồn tại**: 3 đến 5 câu. Lấy từ bài toán trong hội thoại. Không có thì viết: "Skill này làm [mục đích rút từ mô tả]. Từ khóa kích hoạt chính: [ba từ khóa đầu]." và ghi rõ đó là suy ra.
2. **Các quyết định kiến trúc**: 3 đến 7 gạch đầu dòng, mỗi dòng dạng "Quyết định: X. Lý do: Y." Suy ra từ cấu trúc: có nhiều chế độ thì "định tuyến trước thay vì một dây chuyền tuyến tính"; có thư mục tham chiếu thì "chỉ nạp tài liệu khi cần"; có tập lệnh thì "việc lặp lại giao cho mã, không để AI tự làm"; có gọi skill khác thì "dùng lại thay vì lặp logic" và ghi đó là gợi ý mềm hay bắt buộc.
3. **Giá trị ngưỡng** (nếu có): tìm trong tệp skill các con số, giới hạn, mặc định. Lập bảng tham số, giá trị, lý do. Bỏ mục này nếu skill không có số nào.

### Bước 2. Hỏi người dùng hai mục không đoán được

Hai mục này là phán đoán của người, đừng tự điền. Hỏi một lượt, kèm ví dụ:

- **Đánh đổi đã chấp nhận**: chọn thiết kế này thì bỏ qua điều gì? (Ví dụ: "Cảnh báo ở ngưỡng lớn để khỏi làm phiền, chấp nhận bỏ sót trường hợp nhỏ.")
- **Khi nào xem lại**: điều kiện nào thì phải mở lại ghi chú? (Ví dụ: "Khi nền tảng đổi giới hạn ngữ cảnh thì tính lại ngưỡng.")

Người dùng bỏ qua thì ghi `Chưa điền`. Không tự bịa.

### Bước 3. Viết tệp

Điền mẫu trong `templates/design-notes-template.md`: tên skill, ngày hôm nay, và năm mục ở trên, cộng mục **Skill liên quan** (lấy từ các skill được nhắc trong SKILL.md, đánh dấu cái nào là gợi ý mềm) và mục **Nguồn tham khảo cho tài liệu ghi công** (xem dưới). Ghi ra nơi đã thỏa thuận.

Nếu tệp đích đã có, **không ghi đè**. Đề xuất bản gộp và hỏi.

### Bước 4. Báo lại

Nêu đường dẫn tệp và tình trạng từng mục (tự điền, có đầu vào của người dùng, bỏ trống, hoặc bỏ qua vì không áp dụng). Gợi ý: lần sau sửa skill thì đọc ghi chú này trước để hiểu lý do ban đầu.

## Mục nguồn tham khảo

Nếu skill dựa trên tài liệu, bài viết, sách hay khóa học nào, liệt kê ở mục riêng của ghi chú. Chỉ ghi nguồn đã thật sự dùng, và viết theo dạng "ý lấy từ đâu, dùng vào phần nào". Không ghi tên tác giả vào chính SKILL.md.

## Quy cách

Tối đa khoảng 150 dòng, đúng sáu mục (vì sao tồn tại, quyết định kiến trúc, giá trị ngưỡng, đánh đổi, khi nào xem lại, skill liên quan) cộng mục nguồn. Không thêm mục khác.

## Tránh

- Chép nội dung SKILL.md sang ghi chú: ghi chú là lý do, không phải bản sao.
- Tự điền "đánh đổi" hay "khi nào xem lại".
- Đặt ghi chú trong thư mục skill hoặc nạp nó vào ngữ cảnh khi skill chạy.
- Ghi đè tệp có sẵn mà không hỏi.
- Đưa thông tin riêng (đường dẫn máy, tên khách, khóa truy cập) vào ghi chú.

## Dùng cùng skill khác

Làm xong skill bằng công cụ tạo skill nào, gọi skill này ở bước cuối. Nó cũng dùng được độc lập để bổ sung ghi chú cho skill cũ. Nó khác việc rà soát tệp hướng dẫn dự án (CLAUDE.md hay AGENTS.md): đó là một tầng khác.
