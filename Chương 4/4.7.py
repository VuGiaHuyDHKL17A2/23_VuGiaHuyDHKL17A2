import pandas as pd
import numpy as np

np.random.RandomState(100)
ser = pd.Series(np.random.randint(1, 5, [12]))
freq = ser.value_counts()
top_2 = freq.index[:2]
ser = ser.where(ser.isin(top_2), 'Other')

print("Series sau khi thay các giá trị ít xuất hiện bằng 'Other':")
print(ser)