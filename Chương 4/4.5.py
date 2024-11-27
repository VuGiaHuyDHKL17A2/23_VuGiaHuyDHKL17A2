import pandas as pd
import numpy as np

ser = pd.Series(np.random.normal(10, 5, 25))

min_value = ser.min()  
percentile_25 = ser.quantile(0.25)  
median_value = ser.median()  
percentile_75 = ser.quantile(0.75)  
max_value = ser.max()  

print("Giá trị tối thiểu (min):", min_value)
print("Phần centile thứ 25 (25th percentile):", percentile_25)
print("Trung vị (median):", median_value)
print("Phần centile thứ 75 (75th percentile):", percentile_75)
print("Giá trị tối đa (max):", max_value)