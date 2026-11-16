# Dựng bot trong OpenMausBot

Có hai cách. Cách A mất vài phút. Cách B cho bạn toàn quyền kiểm soát và dùng được cho mọi bot, không chỉ ba bot trong repo này.

Trước khi làm theo cách nào, hãy điền [bản thiết kế chung](00-platform-neutral.md).

## Soul của ba bot nằm ở đâu

Ba bot (Pink Pepper Coated Lotus Seeds, Mango Spring Roll, Dried Plum) được định nghĩa trong tệp `team.md` ở thư mục gốc của repo. Mỗi bot có một mục riêng trong đó, gồm vai trò và soul, tức là chỉ dẫn thường trực của bot. Các soul này cũng nằm sẵn thành tệp riêng trong `bots/` (bản đọc tiếng Việt ở `bots/vi/`). OpenMausBot lưu chúng trong ô Instructions của bot.

## Cách A: nhập cả repo (nhanh)

OpenMausBot tìm `botmrr.md` hoặc `team.md` ở thư mục gốc của repo, trên nhánh `main` hoặc `master`. Repo này có `team.md`.

1. Mở **Teams → Import**. Tên menu khác nhau giữa các nguồn của OpenMausBot; có nguồn ghi **Templates → Import** (chưa kiểm chứng). Dùng cái nào phiên bản của bạn hiển thị.
2. Dán liên kết repo: `https://github.com/masonshare/bot-design-team`.
3. Xem màn hình duyệt lại, rồi xác nhận. Quá trình nhập tạo 3 bot cùng soul, skill (đang tắt) và lịch chạy (đang tạm dừng).
4. Mở hồ sơ từng bot → **Skills**. Chỉ bật skill được giao, tắt mọi skill khác nhìn thấy, kể cả skill kế thừa. Làm đủ [quy trình kiểm tra skill](#kiểm-tra-skill-sau-cả-hai-cách) bên dưới.
5. Chọn mô hình cho từng bot. Việc nhập không mang theo mô hình, nên mỗi bot bắt đầu bằng mô hình mặc định của bạn. Dùng mô hình mạnh hơn cho việc thiết kế, mô hình nhẹ hơn cho các lần kiểm tra nhỏ.
6. Kiểm tra mức truy cập. Bot nhập về bắt đầu ở Full access. Chọn **Ask for approval** nếu muốn các hành động rủi ro phải chờ bạn duyệt.
7. Để lịch chạy ở trạng thái tạm dừng cho đến khi bạn đã thử từng cái (xem Cách B, bước 9).

Việc nhập không mang theo: mô hình, thông tin đăng nhập, bộ nhớ, quyền truy cập ứng dụng đã kết nối, và các thư mục `references/`, `scripts/` của skill. Chỉ phần văn bản `SKILL.md` được nhập. Các skill trong repo này được viết để chạy đủ chỉ với `SKILL.md`. Nếu muốn có cả các tệp `references/` tùy chọn, hãy nhập thư mục skill từ máy của bạn: **Bot profile → Skills**, nhập một thư mục (chưa kiểm chứng; tài liệu mô tả cách làm nhưng không nêu tên nút).

Sau đó hãy tự thêm ghi chú bộ nhớ và tự kết nối các ứng dụng của bạn.

## Cách B: tạo từng bot bằng tay

Lặp lại cho từng bot trong ba bot.

1. **Tạo bot.** Ở thanh bên chọn **New or share** (hoặc `Ctrl/Cmd+N`), rồi **New bot**. Bot xuất hiện ngay với tên không trùng và AI mặc định. Dưới lời chào, **Set me up** cho phép bạn mô tả việc trong một câu.
2. **Mở Bot settings** và điền theo thứ tự sau. Tài liệu liệt kê các mục nhưng không nêu thứ tự trên màn hình, nên thứ tự này chỉ là gợi ý (bố cục chưa kiểm chứng).
   1. Name (tên).
   2. Title và description: dòng vai trò lấy từ bản thiết kế của bạn.
   3. Avatar và màu.
   4. Instructions: mở tệp của bot này trong `bots/` (`prompt-designer.md`, `skill-designer.md` hoặc `bot-architect.md`), chép toàn bộ, dán vào đây. Giới hạn là 24 KB.
   5. Engine và model. Chế độ Advanced liệt kê các mô hình; chế độ Simple dùng AI mặc định.
   6. Working folder (tùy chọn).
   7. Computer. Điều khiển máy cục bộ mặc định đang tắt.
3. **Đặt mức truy cập.** Bot mới bắt đầu ở Full access. Chọn **Ask for approval** trong lúc thử nghiệm.
4. **Gieo bộ nhớ.** Bộ nhớ bật sẵn. Thêm các ghi chú ban đầu vào `MEMORY.md`.
5. **Thêm skill.** Mở hồ sơ bot, vào **Skills**. Dán nội dung `SKILL.md` từ `skills/<tên>/SKILL.md` hoặc nhập cả thư mục. Với nhóm này, chỉ bật skill được giao cho bot và tắt mọi skill khác nhìn thấy. Làm đủ [quy trình kiểm tra skill](#kiểm-tra-skill-sau-cả-hai-cách) bên dưới.
6. **Kết nối ứng dụng.** Với mỗi dịch vụ chọn một trong ba: mọi công cụ, danh sách công cụ cụ thể, hoặc không công cụ nào. Chọn mức hẹp nhất vẫn chạy được.
7. **Cất bí mật vào Vault.** Dùng tham chiếu Vault hoặc thẻ yêu cầu thông tin xác thực. Không dán khóa vào chat hay vào skill.
8. **Cài đặt nhóm (tùy chọn).** Đặt ba bot vào cùng một phòng ban (department). Cho Dried Plum làm Chief of Staff bằng **Also in charge of**. Dùng **Bots it may talk to** để các bot chuyển việc cho nhau.
9. **Thêm lịch chạy sau cùng.** Chọn một lần, theo khoảng, hoặc theo ngày trong tuần. Để mỗi lịch ở trạng thái tạm dừng. Chạy thử một lần bằng tay, đọc kết quả, rồi mới bật. Mỗi lịch có thể dùng mô hình riêng, ví dụ mô hình nhẹ hơn.

Mẹo: **App settings → General → Defaults for new bots → Edit** đặt giá trị mặc định cho các bot sau này. Nó không đổi bot đã có.

## Kiểm tra skill sau cả hai cách

Mặc định mỗi bot chỉ bật đúng một skill (kỹ năng):

| Bot | Skill duy nhất được bật | Mọi skill khác nhìn thấy |
|---|---|---|
| Dried Plum | `bot-design` | Tắt |
| Mango Spring Roll | `skill-design` | Tắt |
| Pink Pepper Coated Lotus Seeds | `prompt-design` | Tắt |

Đã cài, được giao và đang bật là ba trạng thái khác nhau. Mục `skills` trong `team.md` giao skill cho bot; nó không chứng minh trạng thái bật đã lưu hoặc loại trừ skill kế thừa. Dùng bảng này làm đích cài đặt, trừ khi người dùng yêu cầu thay đổi rõ ràng.

1. Đọc toàn bộ danh sách skill hiện tại của từng bot, gồm cả đang bật và đang tắt. Ghi đúng tên thực tế; không dùng số lượng cố định hoặc danh sách nhớ từ lần trước.
2. Bật skill được giao; tắt mọi skill khác nhìn thấy trên bot đó, kể cả skill lập trình, nghiên cứu, viết lách được kế thừa. Chỉ tắt, giữ nguyên tệp nguồn dùng chung và các bot khác. Nếu thiếu skill được giao, báo cài đặt chưa hoàn tất và xử lý việc cài trong phạm vi người dùng đã cho phép.
3. Mở lại danh sách Skills đã lưu. Xác nhận tập skill đang bật chỉ chứa đúng skill được giao, tất cả mục còn lại đều tắt. Đọc trạng thái rõ ràng thay vì đoán theo màu nút gạt hoặc tên hành động trên nút.
4. Báo tên từng bot, danh sách bật chính xác, danh sách tắt và thay đổi còn chờ hoặc bị lỗi. Chỉ hoàn tất khi cả ba trạng thái đã lưu khớp bảng. Lệnh đã gửi hoặc bản tóm tắt của đồng đội chưa đủ chứng minh; kiểm tra trực tiếp trạng thái đã lưu nếu có quyền, nếu không thì lấy kết quả đọc mới và ghi rõ là do bot báo cáo.
5. Mở cuộc trò chuyện mới với từng bot, yêu cầu đọc lại trạng thái skill hiện tại. Nếu lần đọc mới khác lần trước, giữ trạng thái chưa hoàn tất, lưu cả hai kết quả và báo sự khác biệt mà không đoán nguyên nhân.

Khi giao bot đã được cấp phép tự kiểm tra hoặc sửa, dùng yêu cầu sau:

> Đọc toàn bộ danh sách skill bằng `skills_list`. Skill duy nhất được bật của bạn phải là `<skill-được-giao>`. Nếu việc cài đặt hoặc sửa này đã được cho phép, dùng `skill_manage` với hành động rõ ràng `enable` cho skill đó và `disable` cho từng skill khác đang nhìn thấy; nếu chưa được phép thì chỉ báo sai lệch. Đọc lại bằng `skills_list`, trả về danh sách bật và tắt chính xác, cùng thay đổi còn chờ hoặc bị lỗi. Không xóa skill hoặc sửa bot khác. Yêu cầu chỉ kiểm tra thì chỉ được báo cáo. Nếu thiếu các công cụ này, báo trở ngại và cách làm thủ công thay vì nhận đã xong.

Nếu skill được giao đang tắt trong khi skill ngoài vai trò đang bật, sửa về đích rồi kiểm tra lại. Đây là sai lệch trạng thái, chưa chứng minh một lỗi nhập cụ thể hay thao tác bị đảo chiều. Quy trình này dùng lúc cài đặt hoặc sửa, không tạo lịch giám sát.

## Kiểm tra bot chạy đúng

- Gửi cho mỗi bot một yêu cầu lấy từ bản thiết kế, rồi so kết quả với tiêu chí "xong khi" của bạn.
- Hỏi bot cho xem danh sách skill và chỉ dẫn; xác nhận khớp với những gì bạn đã dán.
- Xác nhận không có lịch chạy nào đang bật mà bạn chưa thử.

## Liên quan

- [field-mapping.md](field-mapping.md) cho biết mỗi mục thiết kế nằm ở đâu trong OpenMausBot.
- Nếu bạn chuyển từ Grok Bot sang: **Settings → Import & export → Move from Grok Bot** mang theo hồ sơ, chỉ dẫn, skill và các lịch chạy (đang tạm dừng) của một Bot (đã kiểm chứng trong tài liệu OpenMausBot).
