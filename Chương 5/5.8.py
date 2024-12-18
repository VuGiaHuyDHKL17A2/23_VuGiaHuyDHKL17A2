import sqlite3

conn = sqlite3.connect("data.db")
cursor = conn.cursor()
delete_id = 1
cursor.execute("DELETE FROM employees WHERE id = ?;", (delete_id,))
cursor.execute("SELECT * FROM employees;")
rows = cursor.fetchall()
print("Dữ liệu sau khi xóa hàng có ID =", delete_id)
for row in rows:
    print(row)

conn.commit()
conn.close()
