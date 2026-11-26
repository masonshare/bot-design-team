# Ví dụ giả định: bộ tổng hợp phản hồi khách cho tiệm "Bánh Lá Dứa"

Tất cả tên, số liệu bên dưới là bịa để minh họa. Tiệm bánh nhỏ có hai cửa hàng, thu phản hồi qua một bảng tính xuất ra tệp CSV mỗi tuần.

## Bước 1. Làm rõ (dừng)

Yêu cầu gốc: "Làm giúp mình cái báo cáo phản hồi khách hàng."

Agent hỏi một lượt, mỗi câu có mặc định:
1. Ai đọc báo cáo? (mặc định: chủ tiệm, đọc trên điện thoại)
2. Gồm cả hai cửa hàng hay một? (mặc định: cả hai, tách riêng)
3. Chạy một lần hay mỗi tuần? (mặc định: mỗi tuần)
4. Xong nghĩa là gì? (mặc định: một trang, có ba việc nên làm)

Người dùng gật hai câu đầu, đổi câu 3 thành "mỗi tuần, từ tệp CSV". Khối chốt:

```
Công việc: biến tệp phản hồi CSV hằng tuần thành báo cáo một trang cho chủ tiệm
Kết quả mục tiêu: điểm trung bình mỗi cửa hàng; ba chủ đề than phiền nhiều nhất; ba việc nên làm tuần tới
Xong nghĩa là: báo cáo một trang, có số liệu đối chiếu được với tệp gốc
Giả định: tệp có cột điểm 1 đến 5 và cột nhận xét tự do
```

## Bước 2. Nghiên cứu (tự chạy)

- Kiểm kê: có kết nối bảng tính và công cụ chạy Python; chưa có skill báo cáo nào cho tiệm; sẽ tự viết phần đếm chủ đề.
- Câu hỏi: nhận xét tự do nên chia chủ đề bằng từ khóa hay bằng mô hình ngôn ngữ? Có cần tìm web không? Không, việc nằm trọn trong dữ liệu người dùng đưa.
- Nguồn: kiến thức sẵn có và đọc tệp người dùng; không đi đường nghiên cứu sâu vì không đạt dấu hiệu nào.
- Hai cách: (A) đếm từ khóa, dễ và lặp lại được nhưng bỏ sót; (B) agent đọc từng nhận xét rồi gắn chủ đề, chính xác hơn nhưng chậm khi hàng trăm dòng. Chọn A cho phần đếm, B chỉ cho các nhận xét không khớp từ khóa nào. Rủi ro chính: từ khóa thiếu.

## Bước 3. Lập kế hoạch (dừng)

Kế hoạch bốn bước, rồi sau khi duyệt được ghi ra file kế hoạch:

```
- [ ] Bước 1: Đọc CSV, kiểm tra cột, báo dòng lỗi
- [ ] Bước 2: Tính điểm trung bình theo cửa hàng
- [ ] Bước 3: Gắn chủ đề cho nhận xét (từ khóa, rồi đọc phần còn lại)
- [ ] Bước 4: Viết báo cáo một trang và ba việc nên làm
```

## Bước 4. Thực thi (tự chạy)

Tick từng bước ngay khi xong. Giữa chừng ngữ cảnh bị nén gọn: agent đọc lại file kế hoạch, chạy script in mục chưa tick, thấy còn bước 3 và 4, tiếp tục đúng chỗ. Ở bước 3 agent định ghi một file từ điển từ khóa không có trong kế hoạch: dừng xin phép, người dùng đồng ý, rồi mới ghi.

## Bước 5a. Kiểm chứng (dừng)

- Điểm trung bình: chạy lại phép tính trên tệp gốc, khớp với báo cáo. Đạt, kèm kết quả lệnh.
- Ba chủ đề: đếm tay 20 dòng ngẫu nhiên, 18 dòng gắn đúng. Đạt một phần: nêu 2 dòng sai. Tự sửa từ khóa, đếm lại, đạt.
- Một trang: đạt.

Hỏi: tinh chỉnh thêm hay xác nhận? Người dùng xác nhận.

## Bước 5b. Quyết định đóng gói (dừng)

Agent tìm nhanh skill báo cáo phản hồi, không thấy skill tương tự, rồi hỏi: làm một lần hay đóng gói? Người dùng nói tuần nào cũng cần, chọn đóng gói.

## Bước 6. Đóng gói

Dừng chốt tên: `weekly-feedback-digest`, dùng riêng cho dự án này, thân bằng tiếng Việt. Được xác nhận. Skill gồm: mục tiêu, kế hoạch bốn bước làm quy trình, một ví dụ đầu vào đầu ra, và script đếm từ khóa dùng lại được. Kiểm tra cuối: thư mục có `SKILL.md` hợp lệ, tên khớp. Bước tiếp theo đề xuất: chạy thử trên tệp tuần sau.
