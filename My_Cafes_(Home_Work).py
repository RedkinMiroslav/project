import sqlite3

conn = sqlite3.connect('my_cafes.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS cafes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    rating REAL,
    city TEXT
)
''')

cursor.execute("INSERT INTO cafes (name, rating, city) VALUES ('Coffee House', 4.5, 'Sumy')")
cursor.execute("INSERT INTO cafes (name, rating, city) VALUES ('Sweet Dreams Cafe', 4.8, 'Kyiv')")
cursor.execute("INSERT INTO cafes (name, rating, city) VALUES ('Morning Glory', 4.2, 'Lviv')")

conn.commit()

cursor.execute("SELECT * FROM cafes")
print(cursor.fetchall())

conn.close()