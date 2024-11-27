import pandas as pd
import numpy as np

data = np.random.random(20)
ser = pd.Series(data)

deciles = pd.qcut(ser, q=10, labels=False)

print("Dữ liệu ban đầu:")
print(ser)
print("\nPhân vị (deciles):")
print(deciles)
