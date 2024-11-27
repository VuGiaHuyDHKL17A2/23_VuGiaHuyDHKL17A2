import pandas as pd


euro12 = pd.read_csv('euro2012.csv')

# 1. In giá trị cột Goals
print("1. Giá trị cột Goals:")
print(euro12['Goals'])

# 2. Có bao nhiêu đội tham gia Euro2012?
print("\n2. Số đội tham gia Euro2012:", euro12['Team'].nunique())

# 3. In thông tin của Euro2012
print("\n3. Thông tin của Euro2012:")
print(euro12.info())

# 4. Tạo DataFrame mới từ euro12 có cột 'Team', 'Yellow Cards', 'Red Cards'
discipline = euro12[['Team', 'Yellow Cards', 'Red Cards']]
print("\n4. DataFrame Discipline:")
print(discipline)

# 5. Sắp xếp discipline giảm dần theo cột 'Red Cards', 'Yellow Cards'
discipline_sorted = discipline.sort_values(by=['Red Cards', 'Yellow Cards'], ascending=False)
print("\n5. Discipline được sắp xếp giảm dần:")
print(discipline_sorted)

# 6. Tính trung bình Yellow Cards
print("\n6. Trung bình số thẻ vàng:", euro12['Yellow Cards'].mean())

# 7. Lọc các đội ghi được hơn 6 bàn thắng
print("\n7. Các đội ghi hơn 6 bàn thắng:")
print(euro12[euro12['Goals'] > 6])

# 8. Lọc các đội có tên bắt đầu bằng chữ 'G'
print("\n8. Các đội bắt đầu bằng chữ 'G':")
print(euro12[euro12['Team'].str.startswith('G')])

# 9. In 7 cột đầu của euro12
print("\n9. 7 cột đầu của Euro2012:")
print(euro12.iloc[:, :7])

# 10. In tất cả các cột, trừ 3 cột cuối
print("\n10. Tất cả các cột trừ 3 cột cuối:")
print(euro12.iloc[:, :-3])

# 11. In các cột hiển thị 'Team', 'Shooting Accuracy' với đội 'England', 'Italy', 'Russia'
print("\n11. Cột 'Team' và 'Shooting Accuracy' của England, Italy, Russia:")
print(euro12[euro12['Team'].isin(['England', 'Italy', 'Russia'])][['Team', 'Shooting Accuracy']])




