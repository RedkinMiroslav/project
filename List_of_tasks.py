import tkinter as tk

def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        tk.messagebox.showwarning(title="Попередження!", message="Виберіть задачу!")

def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        tk.messagebox.showwarning(title="Попередження!", message="Виберіть задачу!")

def mark_done():
    try:
        task_index = listbox_tasks.curselection()[0]
        task = listbox_tasks.get(task_index)
        
        if task.startswith("✅ "):
            listbox_tasks.delete(task_index)
            listbox_tasks.insert(task_index, task[2:])
        else:
            listbox_tasks.delete(task_index)
            listbox_tasks.insert(task_index, "✅ " + task)
    except:
        tk.messagebox.showwarning(title="Попередження!", message="Виберіть задачу!")

window = tk.Tk()
window.title("Список_Завдань")

frame_tasks = tk.Frame(window)
frame_tasks.pack()

listbox_tasks = tk.Listbox(frame_tasks, height=15, width=50)
listbox_tasks.pack(side=tk.LEFT)

scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tk.Entry(window, width=52)
entry_task.pack()

button_add_task = tk.Button(window, text="Добавити", width=48, command=add_task)
button_add_task.pack()

button_delete_task = tk.Button(window, text="Видалити", width=48, command=delete_task)
button_delete_task.pack()

button_mark_done = tk.Button(window, text="Зроблено", width=48, command=mark_done)
button_mark_done.pack()

window.mainloop()
