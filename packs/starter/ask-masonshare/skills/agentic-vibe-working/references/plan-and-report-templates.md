# Mẫu dùng trong khung sáu bước

Bốn mẫu ngắn để dán vào. Điền bằng nội dung thật của việc đang làm; ô nào chưa biết thì ghi "giả định:" thay vì bỏ trống.

## 1. Khối chốt mục tiêu (cuối bước 1)

```
Công việc: <1-2 câu, nói được bằng lời thường>
Kết quả mục tiêu:
- <ý 1, đo được>
- <ý 2, đo được>
- <ý 3, đo được>
Ràng buộc: <thời hạn, công cụ, định dạng, ngôn ngữ, ngân sách>
Ngoài phạm vi: <những gì cố ý không làm>
Xong nghĩa là: <điều kiện kết thúc, một câu>
Giả định của tôi: <từng giả định, mỗi cái một dòng>
```

Câu hỏi gợi ý cho lượt hỏi đầu (chọn 3 đến 5, mỗi câu kèm mặc định):
- Kết quả dùng để làm gì, ai đọc hoặc ai chạy nó?
- Phần nào chắc chắn nằm trong phạm vi, phần nào chắc chắn nằm ngoài?
- Có định dạng, độ dài hay giọng văn bắt buộc không?
- Có hạn chót hoặc công cụ nào phải dùng, hoặc phải tránh?
- Điều gì làm bạn thất vọng nhất nếu kết quả thiếu?

## 2. File kế hoạch dạng checkbox (sau khi duyệt ở bước 3)

Một dòng checkbox cho mỗi bước; chi tiết thụt vào dưới. Cú pháp phải đúng `- [ ]` và `- [x]` để script đọc được.

```
# Kế hoạch: <tên việc>
Mục tiêu: <một câu>
Ngày duyệt: <ngày>

- [ ] Bước 1: <tên ngắn>
  - Đầu vào: ...
  - Việc làm: ...
  - Skill/công cụ: ...
  - Đầu ra: ...
- [ ] Bước 2: <tên ngắn>
  - Đầu vào: <thường là đầu ra bước 1>
  - Việc làm: ...
  - Đầu ra: ...

Nhật ký thay đổi:
- <ngày> đổi <gì> vì <lý do>
```

Cách dùng: tick `[x]` ngay khi một bước xong; đầu phiên mới hoặc sau khi ngữ cảnh bị nén gọn thì đọc lại file, hoặc chạy `python scripts/context-recovery.py <file>` để in các mục còn mở. Phần "Nhật ký thay đổi" ghi mọi lần đổi hướng đã được người dùng đồng ý.

## 3. Báo cáo kiểm chứng (bước 5a)

```
Tiêu chí 1: <tên> | Đạt | Bằng chứng: <đường dẫn, kết quả lệnh, liên kết>
Tiêu chí 2: <tên> | Đạt một phần | Còn thiếu: <cụ thể>
Tiêu chí 3: <tên> | Chưa đạt | Nguyên nhân gốc: <...>

Lệnh đã chạy: <lệnh> -> <kết quả, các số chính>
Ghi chú rà soát: <phát hiện, hoặc "không có vấn đề nghiêm trọng">
Giả định còn lại: <...>

Kết luận: <đạt hết / còn việc>
Câu hỏi: tinh chỉnh thêm, hay xác nhận hoàn thành?
```

## 4. Bản tóm tắt đóng gói (bước 6)

```
Tên skill: <chữ-thường-gạch-nối>
Nơi đặt: <dùng chung mọi dự án | riêng dự án này>
Ngôn ngữ phần thân: <vi | en | song ngữ>
Mục tiêu cốt lõi: <từ bước 1>
Cách làm đã chốt: <từ bước 2>
Kế hoạch chuẩn: <từ bước 3, rút gọn thành các bước dùng lại được>
Ví dụ: <một đầu vào và đầu ra thật từ bước 4>
Tài nguyên đi kèm: <script, mẫu, hoặc "không có">
Câu hỏi cho người dùng: giữ tên và nơi đặt này chứ?
```
