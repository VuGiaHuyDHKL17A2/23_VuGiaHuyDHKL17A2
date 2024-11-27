import pandas as pd

ser1 = pd.Series(range(5))
ser2 = pd.Series(list('abcde'))

chieu_doc= pd.concat([ser1, ser2], ignore_index=True)
chieu_ngang= pd.DataFrame({'ser1': ser1, 'ser2': ser2})

print("Dữ liệu ban đầu:")
print("ser1:", ser1.tolist())
print("ser2:", ser2.tolist())
print("\nKết quả xếp chồng theo chiều dọc:")
print(chieu_doc)
print("\nKết quả xếp chồng theo chiều ngang:")
print(chieu_ngang)
