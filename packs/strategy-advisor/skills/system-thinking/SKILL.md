---
name: system-thinking
description: Phân tích một vấn đề như một hệ thống qua 4 bước (toàn cảnh, gốc rễ, mối liên kết, quy trình giải pháp) và trả báo cáo có cấu trúc cố định. Dùng khi hỏi "phân tích theo tư duy hệ thống", "tại sao X cứ xảy ra", "tìm nguyên nhân gốc", "vấn đề cứ lặp lại", "debug quy trình". English - analyse a problem as a system in four steps (big picture, root cause, connections and feedback loops, workflow solution) and return a fixed-structure report; use when symptoms keep coming back or fixes cause side effects.
---

# Tư duy hệ thống

Nhìn vấn đề như một hệ thống gồm nhiều phần liên kết với nhau, thay vì sửa từng triệu chứng rời. Khi người dùng đưa một vấn đề cần phân tích, làm đủ bốn bước theo thứ tự rồi trả báo cáo đúng cấu trúc ở cuối. Mỗi bước dựa vào kết quả của bước trước.

## Khi không dùng skill này

- Câu hỏi có đáp án rõ, một bước (tra cứu, tính toán): trả lời thẳng.
- Cần quyết định chiến lược có số liệu thị trường: dùng skill chiến lược phù hợp (ví dụ `business-strategist`); nếu chưa cài, dùng skill này làm khung phân tích.
- Cần vẽ sơ đồ kết quả: có thể nhờ `visual-thinking` nếu đã cài; không thì vẽ bằng chữ.

## Chuẩn bị

Nếu mô tả vấn đề còn thiếu (ở đâu, từ khi nào, ai bị ảnh hưởng, đã thử gì), hỏi một lượt, mỗi câu kèm đề xuất mặc định. Đừng bịa bối cảnh. Chỗ nào chưa rõ thì ghi "giả định" trong báo cáo.

## Bốn bước

### Bước 1. Toàn cảnh
Mục đích: hiểu vấn đề nằm ở đâu trong cả hệ thống, không chỉ phần nổi.

Liệt kê **rộng trước, loại sau**. Mọi thành phần nằm trong cùng hệ thống đều có thể bị ảnh hưởng hoặc là nguyên nhân ngầm, dù thoạt nhìn không liên quan. Đừng loại sớm.

Hỏi: vấn đề xảy ra ở đâu? Hệ thống gồm những phần nào? Ai dùng và ai vận hành? Khi vấn đề xảy ra, điều gì khác bị kéo theo?

Chú ý **độ trễ**: triệu chứng hôm nay thường là hệ quả của một thay đổi vài tuần hay vài tháng trước. Hỏi: có thay đổi nào xảy ra trước triệu chứng, đủ lâu để hệ quả dồn lên?

### Bước 2. Gốc rễ
Mục đích: không dừng ở triệu chứng, đào xuống nguyên nhân thật sự mà mình tác động được.

Hỏi "tại sao" ít nhất ba lần, mỗi lần xuống một lớp. Gốc rễ tốt là thứ có thể đổi hoặc kiểm soát (quy trình, thói quen, thiếu thông tin, thiếu người chịu trách nhiệm), chứ không phải "vì không ai làm". Dừng ở lớp đầu ("vì nhóm làm không kịp") gần như luôn là dừng ở triệu chứng.

### Bước 3. Mối liên kết
Mục đích: hiểu các phần tác động qua lại thế nào, vì sửa một điểm có thể gây hiệu ứng lan.

Hỏi: ai liên quan (người, nhóm, phòng ban)? Quy trình nào chạy quanh vấn đề? Hệ thống hay công cụ nào phụ thuộc nhau? Đâu là nút thắt? Nếu đổi X thì Y và Z ra sao?

Tìm **vòng phản hồi**, vì đó là thứ làm hệ thống tự giữ vấn đề:
- **Vòng khuếch đại:** X làm Y tệ hơn, Y làm X tệ hơn. Ví dụ: trễ hạn, áp lực làm vội, chất lượng giảm, phải làm lại, trễ thêm.
- **Vòng cân bằng:** hệ thống có cơ chế tự chỉnh không (họp rút kinh nghiệm, duyệt, cảnh báo)? Không có thì vấn đề sẽ lặp lại.

Cố vẽ ra ít nhất một vòng; thường nó chỉ ra điểm can thiệp mạnh nhất.

### Bước 4. Quy trình giải pháp
Mục đích: ra một quy trình làm ngay được và cải thiện dần, không chỉ lời khuyên chung.

Quy trình tốt có thứ tự bước rõ, nói ai làm gì, có điểm kiểm tra, và lặp lại được mà không phải nghĩ lại từ đầu.

## Bẫy hay gặp

- **Đổ cho con người** ("vì nhóm không cố gắng"): thường chưa đào đủ sâu. Hỏi tiếp vì sao họ không làm được; câu trả lời hay nằm ở quy trình hoặc công cụ.
- **Chỉ nhìn phần thấy được** (giao diện, khẩu hiệu, con số) mà bỏ phần ngầm (cách khen thưởng, thông tin không chảy): phần ngầm thường là gốc.
- **Đo sai thời điểm:** đo hài lòng lúc mới học dùng khác với đo khả năng tự dùng sau đó. Hỏi chỉ số đang đo có thật sự nói lên kết quả mong muốn không.
- **Giải pháp một điểm cho hệ thống nhiều điểm:** nếu bước 3 chỉ ra ba nút thắt mà chỉ sửa một, hệ thống không hồi lại. Quy trình ở bước 4 phải chạm các nút quan trọng.

## Cấu trúc báo cáo

Luôn trả đủ bốn mục, giữ nguyên tên:

```
## 1. Toàn cảnh
[Vấn đề trong hệ thống lớn. Liệt kê rộng các thành phần, kể cả phần trông không liên quan. Rồi chỉ ra phạm vi thật của vấn đề.]

## 2. Gốc rễ
[Chuỗi "tại sao" từ ba lớp trở lên, từ triệu chứng xuống nguyên nhân tác động được.]

## 3. Mối liên kết
[Bản đồ người, nhóm, quy trình, công cụ và cách chúng tác động nhau. Chỉ ra nút thắt và rủi ro lan. Nêu ít nhất một vòng phản hồi nếu thấy.]

## 4. Giải pháp: quy trình
[Từng bước, ai làm gì, thứ tự, điểm kiểm tra. Lặp lại và cải thiện được.]
```

## Ví dụ ngắn

**Vấn đề:** "Nhóm marketing hay trễ hạn dù đầu tuần nào cũng họp kế hoạch."

1. **Toàn cảnh:** hệ thống gồm nhóm marketing (viết, thiết kế, mạng xã hội), nhóm sản phẩm (đưa yêu cầu), công cụ quản lý việc, kênh đăng, nhóm bán hàng. Sản phẩm và bán hàng trông xa hạn chót nhưng vẫn tác động: yêu cầu đổi muộn và đơn gấp phá kế hoạch. Triệu chứng trực tiếp: hạn bị trễ 2 đến 3 ngày.
2. **Gốc rễ:** vì sao trễ, do việc xong muộn; vì sao muộn, do yêu cầu bị đổi giữa chừng; vì sao đổi, do sản phẩm không chốt yêu cầu trước khi giao. Gốc rễ: thiếu điểm chốt yêu cầu mà hai bên cùng đồng ý.
3. **Liên kết:** yêu cầu đi một chiều, không có vòng phản hồi và chốt chính thức; thay đổi diễn ra qua tin nhắn mà không cập nhật công cụ nên ai nhìn công cụ cũng thấy bản cũ; không ai chịu trách nhiệm chốt.
4. **Quy trình:** sáng thứ hai sản phẩm gửi yêu cầu theo mẫu; đầu giờ chiều hai bên duyệt và chốt; thứ ba đến thứ tư làm đúng bản đã chốt, thay đổi sau chốt chuyển sang tuần sau; thứ năm gửi bản nháp và duyệt; cuối chu kỳ xem yêu cầu nào hay đổi để cải thiện mẫu.

Đây chỉ là ví dụ minh họa. Luôn dùng dữ kiện thật của người dùng.

## Cách trả lời

Trả báo cáo bốn mục, nêu rõ giả định. Nếu lưu, đặt vào Google Docs mới nếu có kết nối; không thì trả trong cuộc trò chuyện.
