# Mẫu trang HTML cho sơ đồ

Một trang HTML tự chứa, mở bằng trình duyệt, không cài gì, không tốn tiền. Mặc định **không phụ thuộc thư viện nào**: sơ đồ được dựng bằng SVG nhúng trực tiếp. Thư viện biểu đồ chỉ dùng khi người dùng chọn.

Dữ liệu dưới đây là bịa (app "Gọn Việc" so với app phổ thông). Thay bằng dữ liệu từ phân tích.

## Cách dùng

1. Chọn mẫu: đường giá trị (mục 1) hoặc lưới canvas (mục 2).
2. Thay mảng dữ liệu ở đầu khối script hoặc các ô chữ trong lưới.
3. Lưu thành trang HTML **mới**, đặt tên theo loại, chủ đề, ngày. Đăng lên nơi riêng tư nếu nền tảng có; không thì đưa mã cho người dùng lưu.
4. Thêm ba dòng đọc sơ đồ dưới hình (cho thấy gì, điểm đáng chú ý, hệ quả).

Khi nhúng SVG trong trang HTML thì không cần khai báo không gian tên; không viết SVG thành tệp riêng trừ khi biết cách thêm khai báo đó.

## 1. Đường giá trị tự dựng (không thư viện)

```html
<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<title>Strategy canvas</title>
<style>
  body { font-family: sans-serif; margin: 0; padding: 24px; background: #fafaf7; color: #223; }
  .wrap { max-width: 860px; margin: 0 auto; }
  h1 { font-size: 20px; }
  svg { width: 100%; height: auto; background: #fff; border-radius: 10px; }
  .note { font-size: 13px; color: #556; }
</style>
</head>
<body>
<div class="wrap">
  <h1>Strategy canvas: Gọn Việc và app phổ thông (số liệu bịa)</h1>
  <svg id="chart" viewBox="0 0 800 420" role="img" aria-label="Đường giá trị"></svg>
  <p class="note">Thang 0 đến 10 là mức đầu tư của mỗi bên vào từng yếu tố. Điểm là ước lượng.</p>
</div>
<script>
const factors = ["Giá rẻ", "Nhiều tính năng", "Dễ dùng", "Nhắc việc thông minh", "Làm việc nhóm nhỏ"];
const series = [
  { name: "App phổ thông", color: "#b33", values: [8, 9, 5, 2, 3] },
  { name: "Gọn Việc",      color: "#157a4a", values: [6, 3, 9, 9, 8] }
];
const W = 800, H = 420, L = 60, R = 130, T = 30, B = 80, MAX = 10;
const x = i => L + i * (W - L - R) / (factors.length - 1);
const y = v => T + (1 - v / MAX) * (H - T - B);
let s = "";
for (let g = 0; g <= MAX; g += 2) {
  s += `<line x1="${L}" x2="${W - R}" y1="${y(g)}" y2="${y(g)}" stroke="#e3e3dc"/>`;
  s += `<text x="${L - 10}" y="${y(g) + 4}" text-anchor="end" font-size="12" fill="#667">${g}</text>`;
}
factors.forEach((f, i) => {
  s += `<text x="${x(i)}" y="${H - B + 28}" text-anchor="middle" font-size="12" fill="#334">${f}</text>`;
});
series.forEach(se => {
  const pts = se.values.map((v, i) => `${x(i)},${y(v)}`).join(" ");
  s += `<polyline points="${pts}" fill="none" stroke="${se.color}" stroke-width="3"/>`;
  se.values.forEach((v, i) => { s += `<circle cx="${x(i)}" cy="${y(v)}" r="4" fill="${se.color}"/>`; });
  const last = se.values.length - 1;
  s += `<text x="${x(last) + 12}" y="${y(se.values[last]) + 4}" text-anchor="start" font-size="13" font-weight="bold" fill="${se.color}">${se.name}</text>`;
});
document.getElementById("chart").innerHTML = s;
</script>
</body>
</html>
```

Nhãn đường nằm ngay bên phải điểm cuối của đường nên không phụ thuộc màu và không đè lên đường; lề phải (`R`) chừa chỗ cho nhãn và cho nhãn trục cuối, tăng nếu tên dài. Thêm đường thứ ba: thêm một đối tượng vào `series`. Radar: đổi sang tọa độ cực (góc = chỉ số yếu tố nhân 360 độ chia số yếu tố, bán kính = giá trị) và nối kín đa giác; giữ tối đa 3 phương án.

## 2. Canvas một trang bằng lưới CSS

Dùng cho mô hình kinh doanh, ERRC, JTBD, bản tóm một trang. Số ô tùy ý (4 đến 9), mỗi ô một tiêu đề và vài gạch đầu dòng ngắn.

```html
<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<title>ERRC</title>
<style>
  body { font-family: sans-serif; margin: 0; padding: 24px; background: #fafaf7; color: #223; }
  .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; max-width: 860px; margin: 0 auto; }
  .cell { border-radius: 10px; padding: 14px 16px; border: 1px solid #ccd; background: #fff; }
  .cell h2 { font-size: 15px; margin: 0 0 8px; }
  .cell ul { margin: 0; padding-left: 18px; font-size: 14px; line-height: 1.5; }
  .e { background: #fdecec; } .r { background: #fff6e8; }
  .a { background: #eef7ee; } .c { background: #eef2fb; }
</style>
</head>
<body>
<h1 style="text-align:center;font-size:20px">ERRC cho Gọn Việc (bịa)</h1>
<div class="grid">
  <div class="cell e"><h2>Loại bỏ</h2><ul><li>Báo cáo năng suất dài</li></ul></div>
  <div class="cell r"><h2>Giảm</h2><ul><li>Số thẻ cấu hình ban đầu</li></ul></div>
  <div class="cell a"><h2>Tăng</h2><ul><li>Tốc độ thêm việc: một chạm</li></ul></div>
  <div class="cell c"><h2>Tạo mới</h2><ul><li>Nhắc theo thói quen của từng người</li></ul></div>
</div>
</body>
</html>
```

Ô chưa biết ghi "chưa biết". Ô nào quá 3 gạch đầu dòng thì tách hoặc rút gọn.

## 3. Dùng thư viện biểu đồ (chỉ khi người dùng đồng ý)

- Hỏi một lần: "Có muốn nạp một thư viện biểu đồ từ CDN để có tương tác (di chuột xem số, đường cong mượt) không? Mặc định là bản tự dựng, không tải gì từ ngoài."
- Được đồng ý thì thêm một thẻ `script` nạp thư viện biểu đồ phổ biến, ghim đúng một phiên bản cụ thể thay vì "mới nhất" để tránh thay đổi bất ngờ. Địa chỉ nạp lấy từ tài liệu chính thức của thư viện đó (người dùng có thể dán cho bạn), không đoán.
- Dữ liệu vẫn nằm trong mảng ở đầu khối script như mẫu 1; chỉ thay phần vẽ. Loại biểu đồ: đường cho strategy canvas, radar cho so sánh nhiều tiêu chí, cột ngang cho phễu.
- Trang công khai trên web: thêm thuộc tính kiểm tra toàn vẹn cho thẻ script hoặc tải thư viện về lưu cùng trang. Trang chỉ mở trên máy mình thì không bắt buộc.
- Trang cần mạng mới vẽ được; nếu người xem offline, mẫu tự dựng vẫn chạy.

## Kiểm tra trang trước khi giao

- Mở được và hiển thị đúng (nếu có công cụ mở trình duyệt thì xem thử; không thì nói rõ chưa kiểm tra bằng mắt).
- Thang, trục, đơn vị có chú thích; số giả định gắn nhãn.
- Không dữ liệu riêng tư nào bị đưa vào trang nếu người dùng định chia sẻ.
