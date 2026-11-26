#!/usr/bin/env python3
"""In ra các mục chưa tick của một file kế hoạch dạng checkbox.

Cách dùng:
    python context-recovery.py <duong-dan-file-ke-hoach>

File kế hoạch dùng cú pháp Markdown: "- [ ] việc chưa xong", "- [x] việc đã xong".
Chỉ dùng thư viện chuẩn; chạy được trên Windows và Linux.
Mã thoát: 0 nếu đọc được file, 2 nếu thiếu tham số hoặc không đọc được file.
"""
import re
import sys

BOX = re.compile(r"^(\s*)[-*]\s+\[([ xX])\]\s*(.*)$")


def main(argv):
    if len(argv) != 2:
        print("Cách dùng: python context-recovery.py <file-ke-hoach>", file=sys.stderr)
        return 2
    path = argv[1]
    try:
        with open(path, encoding="utf-8", errors="replace") as f:
            lines = f.read().splitlines()
    except OSError as err:
        print(f"Không đọc được {path}: {err}", file=sys.stderr)
        return 2

    done, open_items = 0, []
    for number, line in enumerate(lines, start=1):
        m = BOX.match(line)
        if not m:
            continue
        if m.group(2) in "xX":
            done += 1
        else:
            open_items.append((number, m.group(3).strip()))

    total = done + len(open_items)
    out = sys.stdout
    try:
        out.reconfigure(encoding="utf-8")
    except AttributeError:
        pass

    print(f"Kế hoạch: {path}")
    print(f"Tiến độ: {done}/{total} mục đã xong")
    if total == 0:
        print("File không có checkbox nào. Hãy thêm mục dạng '- [ ] Bước 1: ...'.")
    elif not open_items:
        print("Mọi mục đã tick. Bước tiếp theo: kiểm chứng kết quả rồi báo cáo, không tự mở thêm phạm vi.")
    else:
        print("Các mục chưa xong (làm theo thứ tự này):")
        for number, text in open_items:
            print(f"  dòng {number}: {text}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
