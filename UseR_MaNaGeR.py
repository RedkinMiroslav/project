import sqlite3
import tkinter as tk

# --- Ініціалізація бази даних --- #
conn = sqlite3.connect("my_database2.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER
)
""")
conn.commit()

# ---Перевірка наявності користувача "Alice" --- #
cursor.execute("SELECT COUNT(*) FROM users WHERE name = 'Alice'")
if cursor.fetchone()[0] == 0:
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 25))
    conn.commit()

# --- Функції для роботи з базою --- #

def refresh_user_list():
    user_list.delete(0, tk.END)
    cursor.execute("SELECT * FROM users")
    for user in cursor.fetchall():
        user_list.insert(tk.END, f"ID: {user[0]} | Ім'я: {user[1]} | Вік: {user[2]}")

def add_user():
    name = name_entry.get()
    age = age_entry.get()
    if name and age.isdigit():
        cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, int(age)))
        conn.commit()
        refresh_user_list()
        name_entry.delete(0, tk.END)
        age_entry.delete(0, tk.END)

def update_user():
    name = name_entry.get()
    age = age_entry.get()
    if name and age.isdigit():
        cursor.execute("UPDATE users SET age = ? WHERE name = ?", (int(age), name))
        conn.commit()
        refresh_user_list()

def delete_user():
    name = name_entry.get()
    if name:
        cursor.execute("DELETE FROM users WHERE name = ?", (name,))
        conn.commit()
        refresh_user_list()
        name_entry.delete(0, tk.END)
        age_entry.delete(0, tk.END)

# --- Графічний інтерфейс --- #
root = tk.Tk()
root.title("Менеджер користувачів")
root.geometry("480x300")
root.configure(bg="#f0f0f0")

# --- Стилізація віджетів --- #
label_font = ("Segoe UI", 10)
entry_font = ("Segoe UI", 10)
button_font = ("Segoe UI", 10, "bold")

# --- Ввідні поля --- #
name_label = tk.Label(root, text="Ім'я користувача:", bg="#f0f0f0", font=label_font)
name_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
name_entry = tk.Entry(root, font=entry_font)
name_entry.grid(row=0, column=1, padx=10, pady=5)

age_label = tk.Label(root, text="Вік користувача:", bg="#f0f0f0", font=label_font)
age_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
age_entry = tk.Entry(root, font=entry_font)
age_entry.grid(row=1, column=1, padx=10, pady=5)

# --- Кнопки --- #
add_button = tk.Button(root, text="Додати", command=add_user, font=button_font, bg="#a0d468")
add_button.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

update_button = tk.Button(root, text="Оновити", command=update_user, font=button_font, bg="#4fc1e8")
update_button.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

delete_button = tk.Button(root, text="Видалити", command=delete_user, font=button_font, bg="#ed5565")
delete_button.grid(row=2, column=2, padx=10, pady=10, sticky="ew")

# --- Список користувачів --- #
user_list = tk.Listbox(root, width=60, font=("Consolas", 10))
user_list.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

refresh_user_list()

root.mainloop()

conn.close()
