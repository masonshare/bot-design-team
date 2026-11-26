---
name: visual-thinking
description: Turn an analysis, strategy or framework into a diagram on demand - strategy canvas (value curve), customer journey map, 2x2 matrix, system and feedback-loop diagram, one-page business canvas, funnel, radar, positioning map. Only draws what an analysis already says (to analyse a journey or find conversion leaks, use journey-mapper first). Picks the diagram type and tool (Mermaid text, plain SVG, or an HTML page). Tiếng Việt - biến phân tích, chiến lược hay framework thành sơ đồ khi cần. Dùng khi nghe "vẽ sơ đồ", "trực quan hóa", "strategy canvas cho", "journey map", "ma trận 2x2", "vẽ vòng phản hồi", "canvas một trang", "bản đồ định vị", "vẽ phễu", "sơ đồ hóa phân tích này", hoặc ngay sau khi một phân tích xong và đáng nhìn thấy.
---

# Visual Thinking: biến phân tích thành sơ đồ

Một số kết quả phân tích đọc lâu mà nhìn một lần là hiểu: đường giá trị so với đối thủ, hành trình khách, ma trận đánh đổi, vòng phản hồi, canvas một trang. Skill này chọn đúng loại sơ đồ cho đúng framework, dựng bằng công cụ nhẹ nhất xem được ngay, và giữ dữ liệu trung thực.

Đây là sơ đồ để **tư duy và quyết định**, không phải ảnh quảng cáo hay giao diện app.

## Khi không dùng skill này

- Cần ảnh, video, bài đăng thiết kế để đăng thật: dùng công cụ thiết kế hoặc skill sản xuất nội dung nếu có.
- Cần giao diện web hay app chạy được: dùng skill thiết kế giao diện nếu có.
- Chưa có phân tích để vẽ: làm phân tích trước (ví dụ `system-thinking`, `stp-marketing-strategy`, `journey-mapper` nếu đã cài; chưa có thì làm tại chỗ rồi quay lại đây).
- Chỉ cần biểu đồ số liệu thuần (cột, đường theo thời gian từ báo cáo): vẽ bảng hoặc biểu đồ đơn giản, không cần cả quy trình dưới đây.

## Ngữ cảnh khách hàng

Nếu người dùng giữ `brand-profile.md` (tên, định vị, tệp khách, giọng điệu, màu nếu có), đọc trước và dùng tên, màu, ngôn ngữ trong đó cho sơ đồ; đừng hỏi lại. Không có thì hỏi một lần: tên thương hiệu và ngôn ngữ nhãn. Với sơ đồ chỉ để tư duy cá nhân, bỏ qua bước này.

## Quy trình

1. **Nhận đầu vào.** Một phân tích đã có, một framework cần minh họa, hoặc số liệu thô. Thiếu số liệu để vẽ thì hỏi đúng phần thiếu (mỗi câu kèm mặc định), hoặc vẽ bản minh họa và ghi rõ là giả định.
2. **Chọn loại sơ đồ** theo bảng ánh xạ bên dưới. Nếu người dùng đã nêu loại hoặc framework, dùng đúng cái đó. Nếu có hai đến ba loại hợp lý ngang nhau, đề xuất ngắn gọn và để người dùng chọn một.
3. **Chọn công cụ** theo cây quyết định bên dưới.
4. **Dựng sơ đồ.** Dữ liệu lấy từ phân tích, không bịa thêm điểm. Mỗi điểm hay mỗi đường phải truy ngược được về một dòng trong phân tích.
5. **Kèm ba dòng đọc sơ đồ:** nó cho thấy gì, điểm đáng chú ý nhất, hệ quả cho quyết định.
6. **Kết bằng một bước tiếp theo** cụ thể (ví dụ: chọn vùng trống để thử, bổ sung số liệu thật cho điểm đang là giả định, đưa sơ đồ vào bản trình).

## Bảng ánh xạ: framework sang sơ đồ sang công cụ

| Phân tích hoặc framework | Sơ đồ chữ ký | Công cụ ưu tiên |
|---|---|---|
| Blue Ocean, định vị theo đường giá trị | Strategy canvas: trục ngang là yếu tố cạnh tranh, trục dọc là mức đầu tư, mỗi đối thủ một đường | Trang HTML (SVG tự dựng), hoặc Mermaid `xychart-beta` |
| ERRC (loại bỏ, giảm, tăng, tạo mới) | Lưới 4 ô | Lưới HTML hoặc SVG |
| Hành trình khách, các chặng mua | Journey map: chặng, điểm chạm, mức hài lòng | Mermaid `journey` |
| AARRR, phễu bán hàng | Phễu: các bước, tỷ lệ rơi rụng giữa bước | Mermaid `flowchart` hoặc thanh ngang SVG |
| Eisenhower, BCG, chi phí và tác động, rủi ro và lợi ích | Ma trận 2x2 | Mermaid `quadrantChart` |
| STP, định vị so với đối thủ trên hai trục | Bản đồ định vị | Mermaid `quadrantChart` hoặc SVG |
| System thinking, vòng phản hồi | Sơ đồ nhân quả: mũi tên cộng hoặc trừ, nhãn vòng R (tăng cường) và B (cân bằng), ghi độ trễ | Mermaid `flowchart` |
| Mô hình kinh doanh, JTBD, bản tóm một trang | Canvas một trang: 4 đến 9 ô có tiêu đề | Lưới HTML hoặc SVG |
| So sánh nhiều tiêu chí giữa vài phương án | Radar (mạng nhện) | Trang HTML; thư viện biểu đồ nếu người dùng đồng ý, mặc định SVG tự dựng |
| Lộ trình theo giai đoạn | Timeline | Mermaid `timeline` |
| Một framework cần tóm cho người mới | Mindmap | Mermaid `mindmap` |

Framework không có trong bảng: hỏi "đây là so sánh, quy trình, phân cấp hay vòng lặp?" rồi chọn. So sánh thì bảng hoặc 2x2, quy trình thì flowchart, phân cấp thì mindmap, vòng lặp thì sơ đồ nhân quả.

## Cây quyết định công cụ

Chọn theo **ai xem và xem ở đâu**, không theo sở thích.

| Tình huống | Công cụ | Vì sao |
|---|---|---|
| Người dùng không rành kỹ thuật, muốn xem ngay | Trang HTML riêng tư (nếu nền tảng có chỗ đăng trang riêng tư), hoặc Google Slides nếu đã kết nối và họ muốn đưa vào bản trình | Mở bằng một cú nhấp, không cài gì |
| Chỉ có khung trò chuyện, không có kết nối nào | Mermaid trong khối mã, kèm bảng chữ dự phòng | Chạy được ở nhiều nơi, sửa bằng lời dễ |
| Cần đường cong, radar, biểu đồ tương tác | Trang HTML. Mặc định tự dựng SVG, không phụ thuộc gì. Thư viện biểu đồ nạp từ CDN chỉ khi người dùng chọn | Tránh tải mã từ ngoài khi không cần |
| Canvas tự do, bố cục phải chính xác | SVG viết tay, nhúng trong trang HTML | Kiểm soát từng ô |
| Sơ đồ sống lâu trong tài liệu của nhóm kỹ thuật | Mermaid trong tệp văn bản | So sánh phiên bản được |

Mermaid không phải nơi nào cũng hiển thị. Không chắc nơi xem có vẽ được thì đưa kèm bảng chữ, hoặc đề nghị dựng trang HTML.

## Chất lượng của sơ đồ

- **Một sơ đồ một ý.** Quá khoảng 8 nút, 6 đường hay 9 ô thì tách làm hai.
- **Nhãn là từ của người xem,** không phải thuật ngữ nội bộ. Giữ nhãn dưới khoảng 4 từ; chi tiết để ở dòng đọc sơ đồ.
- **Trục có đơn vị và thang rõ.** Ma trận 2x2 ghi "cao" và "thấp" nghĩa là gì; đường giá trị ghi thang 0 đến 10 là gì.
- **Số giả định gắn nhãn.** Điểm ước lượng ghi "ước lượng"; số từ báo cáo ghi nguồn.
- **Màu không là kênh duy nhất:** đường của ai thể hiện bằng nhãn trực tiếp chứ không chỉ bằng màu. Tương phản đủ đọc.
- **Không bóp méo:** cột và phễu bắt đầu từ 0; không cắt trục để chênh lệch trông to hơn.
- **Thông điệp chính đọc được trong năm giây.** Cần giải thích dài nghĩa là sơ đồ chưa tốt.

## Lưu ý theo loại

- **Strategy canvas:** 5 đến 8 yếu tố, 2 đến 3 đường (mình, đối thủ chính, chuẩn ngành). Đường của mình phải có hình dạng khác chuẩn ngành; nếu chồng khít, nói thẳng là chưa khác biệt.
- **Journey map:** mức hài lòng 1 đến 5 ở mỗi điểm chạm; đánh dấu điểm thấp nhất, vì đó là chỗ nên sửa trước.
- **2x2:** đặt tên bốn góc bằng hành động (làm ngay, lên kế hoạch, ủy thác, bỏ), không chỉ bằng tính từ. Điểm dồn hết vào một góc nghĩa là trục chọn chưa tốt.
- **Vòng phản hồi:** mỗi vòng ghi R hoặc B; ghi chỗ có độ trễ; đánh dấu một đòn bẩy để can thiệp.
- **Phễu:** ghi số và tỷ lệ giữ lại giữa hai bước liền kề; tô đậm bước rơi nhiều nhất.
- **Radar:** tối đa 3 phương án và 5 đến 8 tiêu chí; mọi tiêu chí cùng thang, cùng chiều (cao là tốt).
- **Canvas một trang:** mỗi ô tối đa 3 gạch đầu dòng; ô chưa biết ghi "chưa biết" thay vì để trống.

Các mốc số trên là mốc tham khảo cho dễ đọc, không phải luật; điều chỉnh theo nơi trình bày.

## Đầu ra

- Mặc định cho người không rành kỹ thuật: một **trang HTML riêng tư**, hoặc **một slide Google Slides mới** nếu có kết nối. Không có cả hai thì dùng Mermaid hoặc bảng chữ ngay trong câu trả lời.
- Luôn tạo tệp hoặc slide **mới**; không ghi đè tệp có sẵn.
- Đặt tên rõ: loại sơ đồ, chủ đề, ngày.
- Mẫu mã nằm trong `references/`. Đọc đúng mục cần dùng ngay trước khi vẽ, không nạp hết.
  - `references/mermaid-cookbook.md`: khối Mermaid cho từng loại, với ví dụ bịa.
  - `references/html-chart-canvas.md`: mẫu trang HTML tự chứa (đường giá trị, 2x2, canvas lưới, radar) và cách dùng thư viện biểu đồ khi được phép.

## Bước tùy chọn: bản trình bóng bẩy

Nếu người dùng muốn một bản đẹp cho họp hoặc gửi đối tác, có thể **đề nghị** xuất bản chỉnh chu qua công cụ ảnh hoặc thiết kế (nếu có). Luôn hỏi trước, nói rõ dùng công cụ nào và có tốn tín dụng hay chi phí không, rồi chờ đồng ý mới làm. Sơ đồ gốc vẫn là nguồn sự thật; bản đẹp chỉ là lớp trình bày.

## Quy tắc đầu ra chung

- Gắn nhãn mọi giả định và số liệu ước lượng.
- Kết bằng một bước tiếp theo cụ thể.
- Lưu thành Google Doc, Sheet hoặc Slides **mới** nếu có kết nối; không thì trả trong cuộc trò chuyện. Không bao giờ ghi đè tệp có sẵn.
- Không gửi, đăng, chi tiền hay đổi gì ngoài cuộc trò chuyện khi chưa được người dùng đồng ý.
- Các skill phân tích khác chỉ gợi ý nhẹ "muốn vẽ thành sơ đồ không?"; người dùng đồng ý thì mới chạy skill này.

## Kiểm tra chất lượng trước khi giao

- Loại sơ đồ khớp với câu hỏi mà phân tích trả lời?
- Mỗi điểm dữ liệu truy ngược được về phân tích hay nguồn?
- Giả định đã gắn nhãn, thang và trục đã ghi rõ?
- Người ngoài nhìn năm giây có nói được thông điệp chính?
- Mermaid có cú pháp đúng (dòng khai báo loại ở đầu, nhãn không chứa ký tự lạ)? Có bản chữ dự phòng nếu nơi xem không vẽ được?
- Có bước tiếp theo cụ thể ở cuối?
