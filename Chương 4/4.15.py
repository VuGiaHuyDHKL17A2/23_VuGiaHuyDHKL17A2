import pandas as pd

ser= pd.Series(['how', 'to', 'kick', 'ass?'])

chuoi_viet_hoa = ser.str

print("Chuỗi ban đầu:")
print(ser)
print("\nChuỗi sau khi chuyển đổi:")
print(chuoi_viet_hoa)
