class TS:
    def __init__(self, ho_ten, toan, ly, hoa):
        self.ho_ten = ho_ten
        self.toan = toan
        self.ly = ly
        self.hoa = hoa
    def tinh_tong_diem(self):
        return self.toan + self.ly + self.hoa
    # Nhập danh sách thi sinh
danh_sach = []

while True:
    ho_ten = input("Nhập họ tên thi sinh: ")
    toan = int(input("Nhập điểm môn Toán: "))
    ly = int(input("Nhập điểm môn Lý: "))
    hoa = int(input("Nhập điểm môn Hoá: "))

    if toan >= 20 and ly >= 20 and hoa >= 20:
        danh_sach.append(TS(ho_ten, toan, ly, hoa)) 
        print("Thi sinh trúng tuyển:")
        for ts in danh_sach:
                print(ts.ho_ten, ts.tinh_tong_diem()) 
