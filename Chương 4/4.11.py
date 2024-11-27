import pandas as pd

ser = pd.Series(list('abcdefghijklmnopqrstuvwxyz'))
pos = [0, 4, 8, 14, 20]

result = []
for i in pos:
    result.append(ser[i])

print("Dữ liệu ban đầu:")
print(ser)
print("\nVị trí cần lấy:", pos)
print("\nKết quả:")
print(result)
