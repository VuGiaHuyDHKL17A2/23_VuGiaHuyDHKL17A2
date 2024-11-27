import pandas as pd
drinks = pd.read_csv('drinks.csv', index_col=0)

# 1. Hiển thị kiểu dữ liệu (type), kích thước (shape) của drinks
print("\n1. Kiểu dữ liệu và kích thước:")
print(drinks.info())
print(drinks.shape)

# 2. Hiển thị tên các cột
print("\n2. Tên các cột:")
print(drinks.columns)

# 3. Hiển thị 5 dòng đầu và cuối cùng
print("\n3. 5 dòng đầu:")
print(drinks.head())
print("\n3. 5 dòng cuối:")
print(drinks.tail())

# 4. Thống kê thông tin các cột (describe)
print("\n4. Thống kê thông tin chi tiết:")
print(drinks.describe())

# 5. Tính trung bình của 'beer_servings'
print("\n5. Trung bình của beer_servings:")
print(drinks['beer_servings'].mean())

# 6. Tính trung bình các loại rượu cho từng châu lục
mean_values = drinks.groupby('continent').mean(numeric_only=True)
print(mean_values)


# 7. Sắp xếp dữ liệu tăng dần theo 'wine_servings'
print("\n7. Sắp xếp theo wine_servings:")
sorted_drinks = drinks.sort_values(by='wine_servings')
print(sorted_drinks)

# Cho biết quốc gia có lượng tiêu thụ bia cao nhất và thấp nhất
print("\nQuốc gia có lượng tiêu thụ bia cao nhất:")
print(drinks.loc[drinks['beer_servings'].idxmax()])
print("\nQuốc gia có lượng tiêu thụ bia thấp nhất:")
print(drinks.loc[drinks['beer_servings'].idxmin()])
