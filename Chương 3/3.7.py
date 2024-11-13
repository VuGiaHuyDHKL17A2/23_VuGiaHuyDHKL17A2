import numpy as np
baseball = np.loadtxt('baseball_2D.txt')

# 1. Tạo numpy array từ file
np_baseball = np.array(baseball)

# 2. In các giá trị từ dòng thứ 50
np_baseball_50 = np_baseball[49]  # dòng thứ 50, nhưng do chỉ số mảng từ 0-49 nên lấy index 49
print("Các giá trị từ dòng thứ 50:", np_baseball_50)

# 3. Tạo numpy array từ chiều cao và cân nặng
np_height = np_baseball[:, 1]  # giả sử cột 1 là chiều cao
np_weight = np_baseball[:, 2]  # giả sử cột 2 là cân nặng

# 4. Biết chiều cao của vận động viên thứ 124 (chỉ số mảng là 123)
height_124 = np_height[123]
print("Chiều cao vận động viên thứ 124:", height_124)

# 5. Biết chiều cao trung bình
mean_height = np_height.mean()
print("Chiều cao trung bình:", mean_height)

# 6. Mối tương quan giữa chiều cao và cân nặng
correlation = np.corrcoef(np_height, np_weight)[0,1]  # hệ số tương quan giữa chiều cao và cân nặng
print("Hệ số tương quan giữa chiều cao và cân nặng:", correlation)