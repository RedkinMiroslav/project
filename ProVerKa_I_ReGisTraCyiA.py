# --- Импорт необходимых библиотек --- #
import tkinter as tk
from tkinter import messagebox
import bcrypt

# --- База данных пользователей --- #
users_db = []

# --- Функция для регистрации нового пользователя --- #
def register_user():
    username = username_entry.get()
    password = password_entry.get()

    if username and password:
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)
        users_db.append({"username": username, "hashed_password": hashed_password})
        messagebox.showinfo("Регистрация", f"Пользователь {username} успешно зарегистрирован!")
    else:
        messagebox.showerror("Ошибка", "Имя пользователя и пароль не могут быть пустыми!")

# --- Функция для авторизации пользователя --- #
def login_user():
    username = username_entry.get()
    password = password_entry.get()

    for user in users_db:
        if user["username"] == username:
            if bcrypt.checkpw(password.encode("utf-8"), user["hashed_password"]):
                messagebox.showinfo("Авторизация", f"Добро пожаловать в клуб, {username}!")
                app.configure(bg="green")
                return
            else:
                messagebox.showerror("Авторизация", "Пароль неверный, ты точно за нас? 🧐")
                app.configure(bg="red")
                return

    messagebox.showerror("Авторизация", f"Пользователь {username} не найден!")

# --- Создание главного окна программы --- #
app = tk.Tk()
app.title("Авторизация")
app.geometry("500x650")

# --- Добавление поля для ввода имени пользователя --- #
tk.Label(app, text="Имя пользователя:").pack(pady=5)
username_entry = tk.Entry(app)
username_entry.pack(pady=5)

# --- Добавление поля для ввода пароля --- #
tk.Label(app, text="Пароль:").pack(pady=5)
password_entry = tk.Entry(app, show="*")
password_entry.pack(pady=5)

# --- Добавление кнопок для регистрации и авторизации --- #
tk.Button(app, text="Регистрация", command=register_user).pack(pady=10)
tk.Button(app, text="Авторизация", command=login_user).pack(pady=10)

# --- Добавление изображения персонажа --- #
character_image = tk.PhotoImage(file="character.png")
tk.Label(app, image=character_image).pack(pady=10)

# --- Запуск главного цикла программы --- #
app.mainloop()