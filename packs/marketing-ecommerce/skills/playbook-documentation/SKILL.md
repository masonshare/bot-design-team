---
name: playbook-documentation
description: Đóng gói quy trình vận hành và kinh nghiệm thành sổ tay (playbook) mà người mới làm theo được, kèm mẫu quy trình từng bước (SOP), danh sách kiểm tra, và cách nhân bản sang dự án kinh doanh kế tiếp. Dùng khi hỏi "viết SOP thế nào", "làm sao để người khác chạy được thay tôi", "tài liệu hóa công ty", "đóng gói quy trình". English - turn operating know-how into a playbook someone new can follow - SOP template, document types, build/test/maintain checklist, and a launch playbook for repeating a business.
---

# Viết sổ tay quy trình (playbook)

Không có sổ tay thì mỗi lần mở dự án mới là học lại từ đầu, và việc luôn nghẽn ở người duy nhất biết làm. Viết ra một lần, dùng nhiều lần.

## Sổ tay là gì, và không phải là gì

**Là:** tài liệu đủ chi tiết để người mới, không biết bối cảnh, làm đúng một quy trình và ra đúng kết quả.

**Không phải:** mô tả chung chung, lý thuyết, hay thứ "chỉ chủ mới hiểu".

**Phép thử:** đưa cho một người hoàn toàn mới. Họ làm xong mà không phải hỏi lại không?

## Năm loại tài liệu

```
Sổ tay hệ thống
  Quy trình từng bước (SOP)
  Cách xử lý tình huống cụ thể (runbook)
  Danh sách kiểm tra trước và sau mỗi việc
  Bảng chỉ số cần theo dõi
  Cây quyết định: khi nào làm gì
```

## Các bước xây sổ tay

### Bước 1. Kê quy trình đang chạy
- [ ] Liệt kê mọi quy trình, kể cả việc đang nằm trong đầu chưa viết ra.
- [ ] Xếp theo tần suất: hằng ngày, hằng tuần, hằng tháng, theo sự kiện.
- [ ] Đánh dấu việc người khác đang làm: cần quy trình viết ngay.
- [ ] Đánh dấu việc chỉ mình bạn làm được: đó là nút thắt, viết gấp.

### Bước 2. Viết quy trình theo mẫu một trang

```
# [Tên quy trình]
Mục đích: [một câu]
Ai làm: ___
Tần suất: ___
Thời gian ước tính: ___
Khi nào bắt đầu: [tình huống kích hoạt]

Các bước:
1. [Việc cụ thể, bắt đầu bằng động từ]
   Công cụ: ___
   Kết quả cần có: ___
2. [Bước kế]
   Nếu gặp tình huống A: làm ___
   Nếu gặp tình huống B: làm ___
3. ...

Biết đã xong khi: ___
Lỗi thường gặp: [lỗi] -> [cách xử lý]
Hỏi ai khi kẹt: ___
Cập nhật lần cuối: ___
```

### Bước 3. Tổ chức theo nhóm việc

Chia thư mục theo mảng việc của doanh nghiệp, ví dụ:

```
Sổ tay [Tên doanh nghiệp]
  01 Bán hàng và marketing: chạy quảng cáo, đăng bài, mở chiến dịch mới
  02 Vận hành: xử lý đơn, nhập kho, xử lý hoàn hàng
  03 Chăm sóc khách: trả lời khiếu nại, mẫu tin nhắn thường gặp
  04 Tài chính: báo cáo doanh thu tuần, đối soát cuối tháng
  05 Nhân sự: đón nhân viên mới, bảng chỉ tiêu tuần
```

Đây là ví dụ, hãy theo mảng việc thật của khách.

### Bước 4. Thử sổ tay
- [ ] Cho người chưa biết quy trình làm thử.
- [ ] Ghi chỗ họ bị kẹt, rồi làm rõ chỗ đó.
- [ ] Lặp lại với 2 đến 3 người trước khi coi là xong.

### Bước 5. Giữ cho sổ tay sống
- [ ] Mỗi quy trình có một người chịu trách nhiệm cập nhật.
- [ ] Rà lại toàn bộ mỗi quý một lần.
- [ ] Quy trình đổi thì sửa sổ tay ngay, không để cũ.

## Sổ tay để nhân bản sang dự án mới

Ngoài quy trình vận hành, người làm nhiều dự án nên có thêm "sổ tay khởi động":

```
SỔ TAY KHỞI ĐỘNG
Giai đoạn 1. Kiểm chứng (tuần 1 đến 2)
  - Danh sách kiểm chứng ý tưởng
  - Mẫu nghiên cứu đối thủ
  - Mẫu tính chi phí và lãi sơ bộ
Giai đoạn 2. Chuẩn bị (tuần 3 đến 4)
  - Việc pháp lý tối thiểu
  - Thiết lập kênh bán và công cụ
  - Mẫu mô tả công việc cho vài vị trí đầu
Giai đoạn 3. Ra mắt (tháng 2)
  - Danh sách việc cho chiến dịch đầu tiên
  - Mẫu theo dõi chỉ số tuần đầu
  - Cách xử lý tình huống hay gặp khi mới ra mắt
Giai đoạn 4. Tối ưu (tháng 3 đến 6)
  - Khung rà soát hằng tháng
  - Việc cần làm khi hiệu quả quảng cáo giảm hoặc tỷ lệ hoàn hàng tăng
  - Cây quyết định: khi nào mở rộng, khi nào đổi hướng
BÀI HỌC (bổ sung sau mỗi dự án)
  - Điều làm tốt / điều sẽ làm khác / hiểu biết thị trường quan trọng nhất
```

Các mục trên là khung gợi ý. Chỉ đưa vào những giai đoạn khách thật sự cần.

## Nơi lưu sổ tay

| Công cụ | Ưu | Hợp với |
|---|---|---|
| Google Docs và Drive | Miễn phí, quen thuộc, dễ chia sẻ | Mặc định; người làm một mình hoặc nhóm nhỏ |
| Công cụ ghi chú dạng cơ sở dữ liệu (ví dụ Notion) | Đẹp, có bảng dữ liệu | Nhóm đã dùng sẵn công cụ đó |
| Công cụ tài liệu của nhóm kỹ thuật | Mạnh cho nhóm kỹ thuật | Nhóm lớn hơn |

Mặc định lưu bằng Google Docs. Chỉ dùng công cụ khác khi khách đã dùng và yêu cầu.

## Nguyên tắc

Nếu bạn phải giải thích cùng một việc cho hai người, đó là dấu hiệu cần viết quy trình. Mỗi lần giải thích bằng miệng là một lần lãng phí.

## Cách trả lời

Luôn trả ra: mẫu quy trình đã điền cho một việc thật của khách, danh sách kiểm tra, và các bước tiếp theo. Hỏi trước nếu chưa biết đó là việc gì, ai làm, bao lâu một lần. Giao dưới dạng Google Docs mới nếu có kết nối, không thì trả ngay trong cuộc trò chuyện; mọi nội dung là bản nháp cho người dùng duyệt.
