import pandas as pd

# Tạo hai Series
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])
result1 = []
for item in ser1:
    if item not in ser2.values:
        result1.append(item)
result1 = pd.Series(result1)
set1 = set(ser1)
set2 = set(ser2)
unique_items = list((set1 - set2).union(set2 - set1))  
result2 = pd.Series(unique_items)

print("1. Từ ser1 xóa các mục có mặt trong ser2:")
print(result1)
print("\n2. Các mục của ser1 và ser2 nhưng không nằm chung trong cả hai:")
print(result2)