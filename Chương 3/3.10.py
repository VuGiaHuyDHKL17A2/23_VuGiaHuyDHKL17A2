import numpy as np

# Đọc dữ liệu từ file drinks.csv
data = np.genfromtxt('drinks.csv', delimiter=',', dtype=None, names=True, encoding='utf-8')

# 1. Đọc dữ liệu từ file
print("Dữ liệu đầu:\n", data[0:5])
print("Tên các cột:\n", data.dtype.names)

# 2. Thống kê dữ liệu
print("Thông kê số liệu:")
print("Số lượng rượu vang tiêu thụ trung bình ở các châu lục:")
avg_wine_servings_by_continent = {continent: np.mean(data['wine_servings'][data['continent'] == continent]) for continent in np.unique(data['continent'])}
print(avg_wine_servings_by_continent)

# 3. Số lượng bia tiêu thụ trung bình ở mỗi châu lục
avg_beer_servings_by_continent = {continent: np.mean(data['beer_servings'][data['continent'] == continent]) for continent in np.unique(data['continent'])}
print("Số lượng bia tiêu thụ trung bình ở mỗi châu lục:\n", avg_beer_servings_by_continent)

# 4. Số lượng rượu mạnh tiêu thụ trung bình ở mỗi châu lục
avg_spirit_servings_by_continent = {continent: np.mean(data['spirit_servings'][data['continent'] == continent]) for continent in np.unique(data['continent'])}
print("Số lượng rượu mạnh tiêu thụ trung bình ở mỗi châu lục:\n", avg_spirit_servings_by_continent)

# 5. Số lượng rượu tiêu thụ trung bình ở mỗi châu lục
avg_total_litres_by_continent = {continent: np.mean(data['total_litres_of_pure_alcohol'][data['continent'] == continent]) for continent in np.unique(data['continent'])}
print("Số lượng rượu tiêu thụ trung bình ở mỗi châu lục:\n", avg_total_litres_by_continent)

# 6. Sắp xếp dữ liệu theo 'total_litres_of_pure_alcohol'
sorted_data = np.sort(data, order='total_litres_of_pure_alcohol')

# 7. Biết thông kê mô tả số lượng bia và rượu
beer_spirit_mean = np.mean(data[['beer_servings', 'spirit_servings']], axis=0)
print("Số lượng bia và rượu trung bình:\n", beer_spirit_mean)