import sqlite3


connection = sqlite3.connect(":memory:")
cursor = connection.cursor()
print("Đã tạo cơ sở dữ liệu SQLite trong bộ nhớ.")
connection.close()
