import tkinter as tk

root = tk.Tk()
root.title("Привіт")

def say_hello():
    name = entry.get()
    greeting_label.config(text=f"Привіт, {name}!")

entry = tk.Entry(root)
button = tk.Button(root, text="Привітатись", command=say_hello)
greeting_label = tk.Label(root, text="")

entry.pack(pady=10)
button.pack(pady=10)
greeting_label.pack(pady=10)

root.mainloop()



import tkinter as tk
import random

colors = ['red', 'green', 'blue', 'yellow', 'cyan', 'magenta']

root = tk.Tk()
root.title('Колірна магія')

instruction_label = tk.Label(root, text="Натисни кнопку, щоб змінити колір фону!")
instruction_label.pack(pady=20)

def change_color():
    color = random.choice(colors)
    root.config(bg=color) 

change_button = tk.Button(root, text="Магія (змінити колір)", command=change_color)
change_button.pack(pady=20)

root.mainloop()