import tkinter as tk
from tkinter import ttk

def add_task():
    task = task_entry.get()
    if task:
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def complete_task():
    try:
        index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(index)
    except IndexError:
        pass

root = tk.Tk()
root.title("Список_Завдань")

root.geometry("260x275")

task_entry = ttk.Entry(root)
task_entry.pack(pady=5)

add_button = ttk.Button(root, text="Добавити_Нове", command=add_task)
add_button.pack(pady=5)

complete_button = ttk.Button(root, text="Завдання_Зроблено", command=complete_task)
complete_button.pack(pady=5)

tasks_listbox = tk.Listbox(root)
tasks_listbox.pack()

root.mainloop()