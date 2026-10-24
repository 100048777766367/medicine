import os, json, subprocess

print("💊 [MEDICINE ENGINE] Trạm Bốc Thuốc đang đóng gói khay nguyên liệu...")

SHARED_DIR = "/tmp/bodhi_workspace"
os.makedirs(SHARED_DIR, exist_ok=True)

try:
    with open("synapses/investigation_report.json", "r") as f: report = json.load(f)
    if report.get("status") != "AUDITED_AND_APPROVED":
        raise Exception("Đơn thuốc chưa được Investigation thẩm định duyệt!")

    requested = report.get("requested_items", [])
    basket = []

    # Tìm repo nguồn (ví dụ retina) trên máy ảo để trích xuất mã nguồn thực tế
    donor_dir = f"{SHARED_DIR}/donor_source/retina"
    if not os.path.exists(donor_dir):
        subprocess.run(["git", "clone", "--depth", "1", "https://github.com/100048777766367/retina.git", donor_dir], capture_output=True)

    for item in requested:
        target_path = os.path.join(donor_dir, item)
        if os.path.exists(target_path):
            with open(target_path, "r", encoding="utf-8", errors="ignore") as fr:
                code_content = fr.read()
            basket.append({"target": item, "content": code_content, "lines": len(code_content.splitlines())})
            print(f"  ├── 📦 Đã bốc thành công vị thuốc: '{item}' ({len(code_content.splitlines())} dòng)")

    # Đóng gói Khay Nguyên Liệu (Selected Basket)
    os.makedirs("synapses", exist_ok=True)
    with open("synapses/selected_basket.json", "w", encoding="utf-8") as f:
        json.dump(basket, f, indent=4, ensure_ascii=False)

    print("✅ [MEDICINE] Khay nguyên liệu đã được niêm phong hoàn chỉnh, sẵn sàng sang Bàn Bào Chế (cover)!")

except Exception as e:
    print(f"🔴 Lỗi bốc thuốc: {e}")
