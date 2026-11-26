# Mermaid cookbook

Các khối Mermaid hay dùng cho sơ đồ tư duy. Mọi ví dụ dùng thương hiệu và số liệu bịa (cửa hàng trà "Lá Mơ", app "Gọn Việc", ...). Chép khối, thay nội dung bằng dữ liệu thật của người dùng, đặt trong khối mã đánh dấu `mermaid`.

Nếu không chắc nơi xem có vẽ được Mermaid, đưa kèm bảng chữ cùng nội dung, hoặc chuyển sang trang HTML (xem `html-chart-canvas.md`).

## 1. Journey map (`journey`)

Số 1 đến 5 là mức hài lòng tại điểm chạm. Điểm 1 và 2 là chỗ cần sửa trước.

```mermaid
journey
    title Hành trình mua hộp trà quà tặng Lá Mơ
    section Phát hiện
      Xem video ngắn về cách ủ trà: 4: Khách
      Đọc câu chuyện vùng trà: 5: Khách
    section Cân nhắc
      Xem đánh giá trên sàn: 3: Khách
      So giá với hộp quà khác: 2: Khách
    section Mua
      Chọn hương vị cho hộp: 5: Khách
      Thanh toán: 3: Khách
    section Sau mua
      Nhận hộp đóng gói đẹp: 5: Khách
      Mua lại dịp lễ: 4: Khách
```

## 2. Ma trận 2x2 và bản đồ định vị (`quadrantChart`)

Tọa độ điểm từ 0 đến 1. Đặt tên góc bằng hành động. Quy ước: góc 1 là trên phải, 2 trên trái, 3 dưới trái, 4 dưới phải.

```mermaid
quadrantChart
    title Ưu tiên ý tưởng tính năng (số liệu bịa)
    x-axis Tốn nhiều công --> Làm nhanh được
    y-axis Tác động thấp --> Tác động cao
    quadrant-1 Làm ngay
    quadrant-2 Lên kế hoạch
    quadrant-3 Bỏ
    quadrant-4 Thử nhanh
    Nhắc việc theo giờ: [0.8, 0.6]
    Bảng thống kê tuần: [0.7, 0.4]
    Đồng bộ lịch: [0.3, 0.8]
    Giao diện tối: [0.85, 0.2]
```

Bản đồ định vị dùng cùng khối: hai trục là hai tiêu chí khách quan tâm (ví dụ "giá" và "mức cá nhân hóa"), mỗi điểm là một thương hiệu; vùng trống là cơ hội cần kiểm chứng.

## 3. Phễu và quy trình (`flowchart`)

Ghi số và tỷ lệ giữ lại trên mũi tên. Số dưới đây là bịa.

```mermaid
flowchart TD
    A[Khách vào trang: 10.000] -->|30%| B[Xem sản phẩm: 3.000]
    B -->|10%| C[Thêm vào giỏ: 300]
    C -->|50%| D[Thanh toán: 150]
    D -->|40%| E[Mua lại trong 60 ngày: 60]
    B -. rơi nhiều nhất .-> X[Rời trang]
```

## 4. Vòng phản hồi (`flowchart`)

Dấu cộng nghĩa là hai biến cùng chiều, dấu trừ là ngược chiều. Gắn nhãn vòng R (tăng cường) hoặc B (cân bằng) và ghi chỗ có độ trễ.

```mermaid
flowchart LR
    N[Nội dung hữu ích] -->|+| T[Lượt tiếp cận]
    T -->|+| F[Người theo dõi]
    F -->|+| D[Đơn hàng]
    D -->|+ có độ trễ vài tuần| N
    D -->|+| Q[Tải việc chăm sóc khách]
    Q -->|- B| N
```

Đọc: vòng ngoài là R (nội dung sinh đơn, đơn nuôi lại nội dung); nhánh qua tải chăm sóc là B (kìm lại khi nhóm quá tải). Đòn bẩy thường nằm ở nhánh B.

## 5. Mindmap một framework (`mindmap`)

```mermaid
mindmap
  root((Định giá theo giá trị))
    Khi dùng
      Sản phẩm khó so sánh
      Khách trả vì kết quả
    Các bước
      Xác định kết quả khách muốn
      Ước lượng giá trị kết quả
      Chọn mức giá bằng một phần giá trị đó
    Bẫy
      Ước lượng giá trị quá lạc quan
      Quên đối thủ thay thế
```

## 6. Strategy canvas (`xychart-beta`)

`xychart-beta` còn thử nghiệm, đường có thể thô và không phải nơi nào cũng hỗ trợ. Cần bản đẹp hoặc nhãn trực tiếp trên đường thì dùng trang HTML. Mỗi `line` là một đường, theo thứ tự đã nêu trong chú thích.

```mermaid
xychart-beta
    title "Strategy canvas: Gọn Việc và app việc phổ thông (số liệu bịa)"
    x-axis ["Giá rẻ", "Nhiều tính năng", "Dễ dùng", "Nhắc việc thông minh", "Làm việc nhóm nhỏ"]
    y-axis "Mức đầu tư" 0 --> 10
    line [8, 9, 5, 2, 3]
    line [6, 3, 9, 9, 8]
```

Đường 1 là app phổ thông, đường 2 là Gọn Việc. Hai đường tách xa ở "nhắc việc thông minh" và "làm việc nhóm nhỏ": đó là vùng khác biệt cần kiểm chứng với khách thật.

## 7. Timeline (`timeline`)

```mermaid
timeline
    title Lộ trình ra mắt 90 ngày (bịa)
    Tháng 1 : Khảo sát 20 khách : Bản thử nội bộ
    Tháng 2 : Mở cho 100 người dùng đầu : Sửa ba điểm gãy lớn nhất
    Tháng 3 : Mở rộng kênh : Đo mức giữ chân sau 30 ngày
```

## Mẹo cú pháp

- Dòng đầu là loại sơ đồ (`journey`, `quadrantChart`, `flowchart LR`, ...). Thiếu dòng này thì không vẽ.
- Nhãn có dấu tiếng Việt thường vẽ được. Khối nào vỡ: bọc nhãn trong dấu ngoặc kép, hoặc bỏ ký tự đặc biệt như dấu hai chấm, ngoặc, dấu chấm phẩy trong nhãn.
- Trong `flowchart`, nhãn có dấu cách và ký tự đặc biệt nên đặt trong ngoặc vuông; mã nút (A, B, ...) viết liền, không dấu.
- Giữ dưới khoảng 12 nút mỗi sơ đồ; nhiều hơn thì tách.
