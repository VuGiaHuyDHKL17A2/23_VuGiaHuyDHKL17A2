import pandas as pd


ser1 = pd.Series([10, 9, 6, 5, 3, 1, 12, 8, 13])
ser2 = pd.Series([1, 3, 10, 13])
vi_tri = []
for val in ser2:
    if val in ser1.values:
        vi_tri.append(ser1[ser1 == val].index[0])

print("ser1:", ser1.tolist())
print("ser2:", ser2.tolist())
print("\nVị trí của các mục trong ser2 trong ser1:")
print(vi_tri)
