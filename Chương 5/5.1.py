import sqlite3

connection = sqlite3.connect("data.db")
cursor = connection.cursor()
cursor.execute("SELECT sqlite_version();")
version = cursor.fetchone()

print("SQLite version:", version[0])
connection.close()
