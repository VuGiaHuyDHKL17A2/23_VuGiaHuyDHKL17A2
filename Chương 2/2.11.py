import json
from datetime import datetime

def ghi_giao_dich():
    giao_dich = []
    
    while True:
        loai = input("Nhập loại giao dịch (tiền/vàng): ")
        so_luong = float(input("Nhập số lượng: "))
        giao_dich.append({"loai": loai, "so_luong": so_luong})
        
        tiep_tuc = input("Bạn có muốn tiếp tục giao dịch không? (có/không): ").strip().lower()
        if tiep_tuc != 'có':
            break
    
    ghi_file = input("Bạn có muốn ghi giao dịch vào tập tin không? (1: Có, 0: Không): ").strip()
    if ghi_file == '1':
        thoi_gian_hien_tai = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        ten_tap_tin = f'giao_dich_{thoi_gian_hien_tai}.json'
        with open(ten_tap_tin, 'w', encoding='utf-8') as f:
            json.dump(giao_dich, f, ensure_ascii=False, indent=4)
        print(f"Giao dịch đã được ghi vào {ten_tap_tin}")
    else:
        print("Không ghi giao dịch vào tập tin.")

ghi_giao_dich()