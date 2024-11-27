import pandas as pd
import numpy as np


ser = pd.Series(np.random.randint(1, 10, 7))
indices = []
for i in range(len(ser)):
    if ser[i] % 3 == 0:
        indices.append(i)

print("Chuỗi gốc:")
print(ser)
print("\nVị trí của các số là bội của 3:")
print(indices)
