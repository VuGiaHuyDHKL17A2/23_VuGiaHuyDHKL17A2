import json

du_lieu_json = '''
{
    "ten_cong_ty": "Công ty TNHH Đất Việt",
    "dia_chi": "abc Giải Phóng – Hà Nội",
    "cac_don_vi": [
        {"ten": "Đơn vị A1", "so_nhan_vien": 10},
        {"ten": "Đơn vị A2", "so_nhan_vien": 15},
        {"ten": "Đơn vị A3", "so_nhan_vien": 8},
        {"ten": "Đơn vị A4", "so_nhan_vien": 12}
    ]
}
'''


du_lieu = json.loads(du_lieu_json)

tong_nhan_vien = sum(don_vi['so_nhan_vien'] for don_vi in du_lieu['cac_don_vi'])

print(f"Tên công ty: {du_lieu['ten_cong_ty']}")
print(f"Địa chỉ: {du_lieu['dia_chi']}")
print("-----Thống kê nhân viên theo đơn vị-----")

for i, don_vi in enumerate(du_lieu['cac_don_vi'], start=1):
    ten = don_vi['ten']
    so_nhan_vien = don_vi['so_nhan_vien']
    ty_le = (so_nhan_vien / tong_nhan_vien) * 100
    print(f"{i}. Tên đơn vị: {ten}")
    print(f"   - Số nhân viên: {so_nhan_vien}")
    print(f"   - Tỷ lệ: {ty_le:.2f}%\n")