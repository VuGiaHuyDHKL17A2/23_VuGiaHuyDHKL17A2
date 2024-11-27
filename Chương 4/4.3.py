import numpy as np
import pandas as pd

# Tạo hai Series
ser1 = pd.Series(list('abcdefghijklmnopqrstuvwxyz'))
ser2 = pd.Series(np.arange(26))

# Kết nối hai Series thành DataFrame
df = pd.concat([ser1, ser2], axis=1)
df.columns = ['Column1', 'Column2']

# Kết quả
print("Series 1:")
print(ser1)
print("\nSeries 2:")
print(ser2)
print("\nDataFrame:")
print(df)