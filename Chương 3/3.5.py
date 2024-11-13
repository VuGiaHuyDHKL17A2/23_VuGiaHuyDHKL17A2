import numpy as np

# Giả sử dữ liệu được lưu trong các mảng numpy như sau:
heights = np.loadtxt('heights_1.txt')
weights = np.loadtxt('weights_1.txt')

# 1. Tạo numpy array từ list height và weight
arr_height = np.array(heights)
arr_weight = np.array(weights)

# 2. Chuyển đổi đơn vị từ inch sang mét và pound sang kg
arr_height_m = arr_height * 0.0254
arr_weight_kg = arr_weight * 0.453592

# 3. Tính chỉ số BMI
arr_bmi = arr_weight_kg / (arr_height_m ** 2)

# 4. Giá trị cân nặng tại vị trí index = 50
weight_index_50 = arr_weight_kg[50]

# 5. Tạo arr_height_m_100 gồm các phần tử từ 100 đến 110
arr_height_m_100 = arr_height_m[100:111]

# 6. Các cầu thủ có BMI < 21
arr_bmi_less_21 = arr_bmi[arr_bmi < 21]

# 7. Chiều cao trung bình và cân nặng trung bình
avg_height = np.mean(arr_height_m)
avg_weight = np.mean(arr_weight_kg)

# 8. Chiều cao và cân nặng lớn nhất
max_height = np.max(arr_height_m)
max_weight = np.max(arr_weight_kg)

# 9. Chiều cao và cân nặng nhỏ nhất
min_height = np.min(arr_height_m)
min_weight = np.min(arr_weight_kg)

print(f'Chiều cao trung bình: {avg_height:.2f} m')
print(f'Cân nặng trung bình: {avg_weight:.2f} kg')
print(f'Thấp nhất, Chiều cao: {min_height:.2f} m, Cân nặng: {min_weight:.2f} kg')
print(f'Béo nhất, Chiều cao: {max_height:.2f} m, Cân nặng: {max_weight:.2f} kg')