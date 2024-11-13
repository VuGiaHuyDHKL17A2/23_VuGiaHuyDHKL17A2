import numpy as np

# Giả sử dữ liệu được lưu trong tệp "euro2012.csv"
# Đọc dữ liệu từ file sử dụng numpy
data = np.genfromtxt('euro2012.csv', delimiter=',', dtype=None, names=True, encoding=None)

# 1. Giá trị cột Goals
col_goals = data['Goals']
print("Cột Goals:", col_goals)

# 2. Số đội tham gia
num_teams = len(np.unique(data['Team']))
print("Số đội tham gia:", num_teams)

# 3. Tạo DataFrame chỉ chứa cột Team, Yellow Cards, Red Cards
cols = np.array([data['Team'], data['Yellow Cards'], data['Red Cards']])
discipline = np.core.records.fromarrays(cols, names='Team, Yellow Cards, Red Cards', formats='U20, i4, i4')
print("Dataframe:", discipline)

# 4. Sắp xếp theo Red Cards, Yellow Cards
sorted_discipline = np.sort(discipline, order=['Red Cards', 'Yellow Cards'])

# 5. Trung bình số thẻ vàng
mean_yellow_cards = np.mean(data['Yellow Cards'])
print("Số thẻ vàng trung bình:", mean_yellow_cards)

# 6. Lọc các đội có ghi 6 bàn thắng
teams_6_goals = data[data['Goals'] == 6]
print("Các đội ghi 6 bàn:", teams_6_goals)

# 7. Ở cột Group có chứa ký tự 'G'
teams_group_g = data[np.char.find(data['Group'], 'G') != -1]
print("Các đội có Group chứa G:", teams_group_g)

# 8. In tất cả các cột từ 7 đến 11
cols_7_11 = data[:, 6:11]
print("Các cột từ 7 đến 11:", cols_7_11)

# 9. Tất cả các cột, chỉ 3 cột cuối
teams_3_last_cols = data[:, -3:]
print("Các cột, chỉ 3 cột cuối:", teams_3_last_cols)

# 10. Cột Team và 'Shooting Accuracy'
team_shooting_acc = data[['Team', 'Shooting Accuracy']]
print("Cột Team và Shooting Accuracy:", team_shooting_acc)