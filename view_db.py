import sqlite3

conn = sqlite3.connect("stocks.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM stock_data")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()


