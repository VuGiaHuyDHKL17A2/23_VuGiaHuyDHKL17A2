import pandas as pd
import numpy as np
ser = pd.Series(np.random.randint(1, 10, 35))
#1. ý nghĩa mã lệnh
# Lệnh này tạo một chuỗi dữ liệu với 35 giá trị ngẫu nhiên, mỗi giá trị là số nguyên từ 1 đến 9 
df = ser.values.reshape(7, 5)  
df = pd.DataFrame(df) 
print("Chuỗi gốc:")
print(ser)
print("\nDataFrame (7 hàng, 5 cột):")
print(df)