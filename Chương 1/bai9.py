class DaGiac:
    def __init__(self, cac_canhs):
        self.cac_canhs = cac_canhs

    def chu_vi(self):
        return sum(self.cac_canhs)

class HinhBinhHanh(DaGiac):
    def __init__(self, day, canh, chieu_cao):
        super().__init__([day, canh, day, canh])
        self.day = day
        self.chieu_cao = chieu_cao
    def dien_tich(self):
        return self.day * self.chieu_cao

class HinhChuNhat(HinhBinhHanh):
    def __init__(self, chieu_dai, chieu_rong):
        super().__init__(chieu_dai, chieu_rong, chieu_rong)
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong

    def dien_tich(self):
        return self.chieu_dai * self.chieu_rong

class HinhVuong(HinhChuNhat):
    def __init__(self, canh):
        super().__init__(canh, canh)


print("Hình bình hành")
day = float(input("Nhập độ dài đáy: "))
canh = float(input("Nhập độ dài cạnh: "))
chieu_cao = float(input("Nhập chiều cao: "))
hinh_binh_hanh = HinhBinhHanh(day, canh, chieu_cao)
print(f"Chu vi: {hinh_binh_hanh.chu_vi()}")
print(f"Diện tích: {hinh_binh_hanh.dien_tich()}")

print("\nHình chữ nhật")
chieu_dai = float(input("Nhập chiều dài: "))
chieu_rong = float(input("Nhập chiều rộng: "))
hinh_chu_nhat = HinhChuNhat(chieu_dai, chieu_rong)
print(f"Chu vi: {hinh_chu_nhat.chu_vi()}")
print(f"Diện tích: {hinh_chu_nhat.dien_tich()}")

print("\nHình vuông")
canh = float(input("Nhập độ dài cạnh: "))
hinh_vuong = HinhVuong(canh)
print(f"Chu vi: {hinh_vuong.chu_vi()}")
print(f"Diện tích: {hinh_vuong.dien_tich()}")
