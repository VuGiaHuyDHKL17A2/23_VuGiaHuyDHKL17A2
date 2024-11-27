import numpy as np
import pandas as pd


mylist = list('abcdefghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))
ser = pd.Series(mydict)

# Chuyển Series thành DataFrame
df = ser.reset_index()
df.columns = ['Index', 'Value']

# Kết quả
print("Series:")
print(ser)
print("\nDataFrame:")
print(df)



