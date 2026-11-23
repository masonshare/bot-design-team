"""Fake agent for test_run_scenarios.py. Role in SCENARIO_ROLE; behaviour in STUB_MODE."""
import csv
import os
import sys

role = os.environ.get("SCENARIO_ROLE")
mode = os.environ.get("STUB_MODE", "good")
sys.stdin.read()
if role == "judge" and os.environ.get("STUB_JUDGE_LOG"):  # lets tests count judge calls
    with open(os.environ["STUB_JUDGE_LOG"], "a") as f:
        f.write("x" + chr(10))
if role == "bot" and mode == "alternate":  # flaky agent: logs the refusal on every 2nd bot call
    cf = os.environ["STUB_COUNTER"]
    n = (int(open(cf).read()) if os.path.exists(cf) else 0) + 1
    open(cf, "w").write(str(n))
    mode = "append-dx" if n % 2 == 0 else "good"
if role == "judge":
    print('{"pass": true, "reasons": []}' if mode != "badjudge" else "no json here")
    sys.exit(0)
if mode == "login":  # agent not logged in: the runner stops the whole run
    sys.stderr.write("please login first")
    sys.exit(3)
if mode == "crash":
    sys.stderr.write("boom")
    sys.exit(3)
if mode in ("append-dx", "badjudge"):  # staff logs a refusal row
    with open("sheet/de-xuat.csv", "a", encoding="utf-8", newline="") as f:
        csv.writer(f).writerow(["2026-01-01", "Zalo", "q", "chưa có trong kho kiến thức, hãy hỏi chủ shop",
                                "", "x", "Mới", "1"])
if mode == "edit-kb":  # rogue agent edits the read-only Kịch bản file
    os.chmod("sheet/kich-ban.csv", 0o666)
    with open("sheet/kich-ban.csv", "a", encoding="utf-8") as f:
        f.write("X,x,x,x,x,all,x,Đã duyệt,x\n")
print("(stub reply) chưa có trong kho kiến thức, hãy hỏi chủ shop")
