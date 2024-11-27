import pandas as pd

ser = pd.Series([1, 3, 6, 10, 15, 21, 27, 35])
hieu_so = ser.diff()

print("Chuỗi ban đầu:")
print(ser)
print("\nHiệu số giữa các số liên tiếp:")
print(hieu_so)
