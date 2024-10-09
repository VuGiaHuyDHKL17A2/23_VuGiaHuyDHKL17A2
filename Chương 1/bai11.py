class TamGiac:
    def __init__(self, canh1, canh2, canh3):
        self.canh1 = canh1
        self.canh2 = canh2
        self.canh3 = canh3

    def chu_vi(self):
        return self.canh1 + self.canh2 + self.canh3

class TamGiacVuong(TamGiac):
    def __init__(self, canh_goc_vuong1, canh_goc_vuong2, canh_huyen):
        super().__init__(canh_goc_vuong1, canh_goc_vuong2, canh_huyen)

    def dien_tich(self):
        return 0.5 * self.canh1 * self.canh2

class TamGiacCan(TamGiac):
    def __init__(self, canh_day, canh_bang):
        super().__init__(canh_day, canh_bang, canh_bang)

    def dien_tich(self):
        from math import sqrt
        chieu_cao = sqrt(self.canh2**2 - (self.canh1 / 2)**2)
        return 0.5 * self.canh1 * chieu_cao

class TamGiacDeu(TamGiacCan):
    def __init__(self, canh):
        super().__init__(canh, canh)

    def dien_tich(self):
        from math import sqrt
        return (sqrt(3) / 4) * self.canh1 ** 2


print("Nhập thông số của tam giác vuông:")
canh_goc_vuong1 = float(input("Nhập cạnh góc vuông thứ nhất: "))
canh_goc_vuong2 = float(input("Nhập cạnh góc vuông thứ hai: "))
canh_huyen = float(input("Nhập cạnh huyền: "))
tam_giac_vuong = TamGiacVuong(canh_goc_vuong1, canh_goc_vuong2, canh_huyen)
print(f"Chu vi Tam Giac Vuong: {tam_giac_vuong.chu_vi()}")
print(f"Diện tích Tam Giac Vuong: {tam_giac_vuong.dien_tich()}")

print("\nNhập thông số của tam giác cân:")
canh_day = float(input("Nhập cạnh đáy: "))
canh_bang = float(input("Nhập cạnh bên bằng nhau: "))
tam_giac_can = TamGiacCan(canh_day, canh_bang)
print(f"Chu vi Tam Giac Can: {tam_giac_can.chu_vi()}")
print(f"Diện tích Tam Giac Can: {tam_giac_can.dien_tich()}")

print("\nNhập thông số của tam giác đều:")
canh = float(input("Nhập cạnh của tam giác đều: "))
tam_giac_deu = TamGiacDeu(canh)
print(f"Chu vi Tam Giac Deu: {tam_giac_deu.chu_vi()}")
print(f"Diện tích Tam Giac Deu: {tam_giac_deu.dien_tich()}")

