import sqlite3

conn = sqlite3.connect("data.db")
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Danh sách các bảng:")
for table in tables:
    print(table[0])

conn.close()
