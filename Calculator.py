import tkinter as tk

current_expression = ""

def on_button_click(button):
    global current_expression

    if button == "AC":
        current_expression = ""
        display.delete(0, tk.END)

    elif button == "=":
        try:
            result = eval(current_expression)
            display.delete(0, tk.END)
            display.insert(0, str(result))
            current_expression = str(result)
        except Exception as e:
            display.delete(0, tk.END)
            display.insert(0, "Помилка")
            current_expression = ""
            print(f"Error: {e}")

    elif button == "C":
        current_expression = current_expression[:-1]
        display.delete(0, tk.END)
        display.insert(0, current_expression)
    else:
        current_expression += str(button)
        display.delete(0, tk.END)
        display.insert(0, current_expression)

def set_theme(theme):
    if theme == "light":
        root.config(bg="white")
        display.config(bg="lightgray", fg="black")
        button_bg = "lightgray"
        button_fg = "black"
    elif theme == "dark":
        root.config(bg="black")
        display.config(bg="gray", fg="white")
        button_bg = "darkgrey"
        button_fg = "white"
    elif theme == "red":
        root.config(bg="red")
        display.config(bg="lightcoral", fg="white")
        button_bg = "salmon"
        button_fg = "white"
    elif theme == "orange":
        root.config(bg="orange")
        display.config(bg="lightsalmon", fg="white")
        button_bg = "sandybrown"
        button_fg = "white"
    elif theme == "yellow":
        root.config(bg="yellow")
        display.config(bg="lightyellow", fg="black")
        button_bg = "khaki"
        button_fg = "black"
    else:
        root.config(bg="white")
        display.config(bg="lightgray", fg="black")
        button_bg = "lightgray"
        button_fg = "black"

    for button in buttons:
        button.config(bg=button_bg, fg=button_fg)

root = tk.Tk()
root.title("Калькулятор")
root.geometry("385x440")

display = tk.Entry(root, font=("Arial", 24), justify="right")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = []
button_texts = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+",
    "AC", "(", ")", "."
]

row_val = 1
col_val = 0

for text in button_texts:
    button = tk.Button(root, text=text, font=("Times New Roman", 18), width=5, height=2, command=lambda text=text: on_button_click(text))
    button.grid(row=row_val, column=col_val)
    buttons.append(button)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

menubar = tk.Menu(root)
theme_menu = tk.Menu(menubar, tearoff=0)

theme_menu.add_command(label="Світла тема", command=lambda: set_theme("light"))
theme_menu.add_command(label="Темна тема", command=lambda: set_theme("dark"))
theme_menu.add_command(label="Червона тема", command=lambda: set_theme("red"))
theme_menu.add_command(label="Помаранчева тема", command=lambda: set_theme("orange"))
theme_menu.add_command(label="Жовта тема", command=lambda: set_theme("yellow"))

menubar.add_cascade(label="Налаштування", menu=theme_menu)

root.config(menu=menubar)
root.mainloop()