# --- ClassWork --- #

import sqlite3

conn = sqlite3.connect('restaurant_menu.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS menu (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    dish_name TEXT,
    category TEXT,
    price INT,
    available TEXT
)
""")

cursor.execute("INSERT INTO menu (dish_name, category, price, available) VALUES ('макарони', 'головна страва', 45, 'ТАК')")
cursor.execute("INSERT INTO menu (dish_name, category, price, available) VALUES ('морозиво', 'десерт', 50, 'ТАК')")
cursor.execute("INSERT INTO menu (dish_name, category, price, available) VALUES ('піцца', 'головна страва', 150, 'НІ')")
cursor.execute("INSERT INTO menu (dish_name, category, price, available) VALUES ('картопля', 'головна страва', 5, 'ТАК')")
cursor.execute("INSERT INTO menu (dish_name, category, price, available) VALUES ('суп', 'суп', 60, 'НІ')")

cursor.execute("SELECT dish_name, category, price, available FROM menu WHERE dish_name LIKE '%макарони%'")
print(cursor.fetchall())

cursor.execute("SELECT dish_name, category, price, available FROM menu WHERE category LIKE '%головна страва%'")
print(cursor.fetchall())

cursor.execute("SELECT dish_name, category, price, available FROM menu WHERE price > 15 AND available LIKE '%ТАК%'")
print(cursor.fetchall())

conn.close()

# --- HomeWork --- #

import sqlite3

conn = sqlite3.connect('my_favorites.db')
cursor = conn.cursor()

cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS favorites (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        genre TEXT,
        release_year INTEGER,
        rating REAL,
        comments TEXT
    )
''')

title1 = 'Інтерстеллар'
genre1 = 'Наукова фантастика'
year1 = 2014
rating1 = 9.0
comment1 = 'Один з моїх найулюбленіших фільмів про космос!'

title2 = 'Кримінальне чтиво'
genre2 = 'Кримінал'
year2 = 1994
rating2 = 8.9
comment2 = 'Культовий фільм з чудовими діалогами.'

title3 = 'Драйв'
genre3 = 'Бойовик'
year3 = 2011
rating3 = 7.8
comment3 = 'Стильний та напружений бойовик з чудовою музикою.'

cursor.execute(f"INSERT INTO favorites (title, genre, release_year, rating, comments) VALUES ('{title1}', '{genre1}', {year1}, {rating1}, '{comment1}')")
cursor.execute(f"INSERT INTO favorites (title, genre, release_year, rating, comments) VALUES ('{title2}', '{genre2}', {year2}, {rating2}, '{comment2}')")
cursor.execute(f"INSERT INTO favorites (title, genre, release_year, rating, comments) VALUES ('{title3}', '{genre3}', {year3}, {rating3}, '{comment3}')")

conn.commit()

cursor.execute(f"SELECT title, release_year, rating FROM favorites WHERE genre LIKE 'Наукова фантастика'")
print(cursor.fetchall())

cursor.execute(f"SELECT title, genre, rating FROM favorites WHERE release_year > 2010")
print(cursor.fetchall())

cursor.execute(f"SELECT title, genre, release_year FROM favorites WHERE rating > 8.5")
print(cursor.fetchall())

conn.close()