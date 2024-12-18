import sqlite3

conn = sqlite3.connect("data.db")
cursor = conn.cursor()
cursor.execute("UPDATE employees SET salary = salary * 1.1;")
cursor.execute("SELECT * FROM employees;")
rows = cursor.fetchall()
print("Dữ liệu sau khi cập nhật:")
for row in rows:
    print(row)

conn.commit()
conn.close()
