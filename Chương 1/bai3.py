class PS:
    def __init__(self):
        self.tu = 0
        self.mau = 1  

    def kiem_tra_tinh_hop_le(self):
        return self.mau != 0  

    def nhap_phan_so(self):
        self.tu = int(input("Nhập tử số: "))
        self.mau = int(input("Nhập mẫu số: "))
        if not self.kiem_tra_tinh_hop_le():
            print("Mẫu số không hợp lệ! Mẫu số phải khác 0.")
            self.mau = 1  

    def in_phan_so(self):
  
        if self.kiem_tra_tinh_hop_le():
            print(f"Phân số: {self.tu}/{self.mau}")
        else:
            print("Phân số không hợp lệ.")
phan_so = PS()
phan_so.nhap_phan_so()
phan_so.in_phan_so()