import pandas as pd
import numpy as np

truth = pd.Series(range(10))
pred = pd.Series(range(10)) + np.random.random(10)
sai_so = ((truth - pred) ** 2).mean()
print("Chuỗi thực tế (truth):")
print(truth)
print("\nChuỗi dự đoán (pred):")
print(pred)
print("\nSai số bình phương trung bình (MSE):", sai_so)
