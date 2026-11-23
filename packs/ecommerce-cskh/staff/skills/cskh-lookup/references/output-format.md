# Output format for cskh-lookup

Example (channel Shopee, FAKE data):

```
Trả lời khách:
Dạ anh/chị vào mục Đơn hàng trên Shopee, chọn Hủy đơn nếu đơn chưa được giao đi ạ. Em hỗ trợ thêm nếu cần.

Dành cho nhân viên (không gửi khách):
- Mã kịch bản: FAKE-ORD-002 (Đã duyệt, kênh Shopee)
- Lưu ý nội bộ: Chỉ dùng trên Shopee. Không chuyển khách sang kênh ngoài sàn
```

Rules:

- The first block must be safe to copy and send as is: no codes, no status words, no internal note, no warnings.
- The second block always names the code and status. Add a warning line when the match was `Nháp`, `Hết hạn`, another channel, or contradictory.
- Never merge the two blocks.
- When nothing official matched, the rules of skill `cskh-no-script` apply instead.
