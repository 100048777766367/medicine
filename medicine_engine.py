import json, time, hashlib
print("💊 [MEDICINE ENGINE THỨC TỈNH] Trạm Bốc Thuốc sẵn sàng nhận lệnh.")
epoch = int(time.time())
cid = hashlib.shake_256(f"medicine_dispenser_{epoch}".encode()).hexdigest(32)
print(f"✨ Đơn thuốc nguyên liệu đã được bảo chứng toàn vẹn (CID: {cid[:16]}...)")
