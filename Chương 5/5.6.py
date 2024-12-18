import sqlite3
conn = sqlite3.connect("data.db")
cursor = conn.cursor()
cursor.execute("SELECT COUNT(*) FROM employees;")
count = cursor.fetchone()[0]

print("Số lượng bản ghi trong bảng employees:", count)
conn.close()
