import sqlite3

conn = sqlite3.connect("data.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    salary REAL
)
""")

cursor.execute("INSERT INTO employees (name, salary) VALUES ('Huy', 50000);")
cursor.execute("INSERT INTO employees (name, salary) VALUES ('Chè', 60000);")
cursor.execute("SELECT * FROM employees;")
rows = cursor.fetchall()
print("Danh sách nhân viên:")
for row in rows:
    print(row)

conn.commit()
conn.close()
