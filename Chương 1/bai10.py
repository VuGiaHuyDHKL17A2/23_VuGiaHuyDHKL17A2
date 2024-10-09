class Diem:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def hien_thi(self):
        print(f"Diem({self.x}, {self.y})")

class Elip(Diem):
    def __init__(self, x, y, truc_lon, truc_nho):
        super().__init__(x, y)
        self.truc_lon = truc_lon
        self.truc_nho = truc_nho

    def dien_tich(self):
        import math
        return math.pi * self.truc_lon * self.truc_nho

class DuongTron(Elip):
    def __init__(self, x, y, ban_kinh):
        super().__init__(x, y, ban_kinh, ban_kinh)

    def dien_tich(self):
        import math
        return math.pi * self.truc_lon ** 2


print("Nhập tọa độ điểm:")
x = float(input("Nhập x: "))
y = float(input("Nhập y: "))

print("\nNhập thông số của elip:")
truc_lon = float(input("Nhập trục lớn: "))
truc_nho = float(input("Nhập trục nhỏ: "))
elip = Elip(x, y, truc_lon, truc_nho)
elip.hien_thi()
print(f"Dien tich Elip: {elip.dien_tich()}")

print("\nNhập thông số của đường tròn:")
ban_kinh = float(input("Nhập bán kính: "))
duong_tron = DuongTron(x, y, ban_kinh)
duong_tron.hien_thi()
print(f"Dien tich Duong Tron: {duong_tron.dien_tich()}")
