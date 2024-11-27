import pandas as pd
import numpy as np
fruit = pd.Series(np.random.choice(['apple', 'banana', 'carrot'], 10))
weights = pd.Series(np.linspace(1, 10, 10))
khoi_luong_trung_binh = weights.groupby(fruit).mean()

print("Weights:", weights.tolist())
print("Fruits:", fruit.tolist())
print("\nKhối lượng trung bình từng loại quả:")
print(khoi_luong_trung_binh)
