import customtkinter as ctk

cipher_dicts = {
    "symbolic": {
        'А': '@', 'Б': '#', 'В': '$', 'Г': '%', 'Ґ': '&',
        'Д': '*', 'Е': '(', 'Є': ')', 'Ж': '+', 'З': '-',
        'И': '=', 'І': '_', 'Ї': '{', 'Й': '}', 'К': '[',
        'Л': ']', 'М': ':', 'Н': ';', 'О': "'", 'П': '"',
        'Р': '|', 'С': '/', 'Т': '7', 'У': '~', 'Ф': '^',
        'Х': '?', 'Ц': '!', 'Ч': '@', 'Ш': '#', 'Щ': '$',
        'Ь': '%', 'Ю': '^', 'Я': '&'
    },
    "latin": {
        'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Ґ': 'G',
        'Д': 'D', 'Е': 'E', 'Є': 'Ye', 'Ж': 'Zh', 'З': 'Z',
        'И': 'Y', 'І': 'I', 'Ї': 'Yi', 'Й': 'Y', 'К': 'K',
        'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P',
        'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F',
        'Х': 'Kh', 'Ц': 'Ts', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shch',
        'Ь': '', 'Ю': 'Yu', 'Я': 'Ya'
    },
    "cyrillic": {
        'А': 'Я', 'Б': 'Ю', 'В': 'Э', 'Г': 'Ь', 'Ґ': 'Ы',
        'Д': 'Щ', 'Е': 'Ш', 'Є': 'Ч', 'Ж': 'Ц', 'З': 'Х',
        'И': 'Ф', 'І': 'У', 'Ї': 'Т', 'Й': 'С', 'К': 'Р',
        'Л': 'П', 'М': 'О', 'Н': 'Н', 'О': 'М', 'П': 'Л',
        'Р': 'К', 'С': 'Й', 'Т': 'И', 'У': 'И', 'Ф': 'З',
        'Х': 'Ж', 'Ц': 'Е', 'Ч': 'Є', 'Ш': 'Д', 'Щ': 'Г',
        'Ь': 'В', 'Ю': 'Б', 'Я': 'А'
    }
}

def encrypt(text, cipher_key):
    encrypted_text = ""
    cipher_dict = cipher_dicts[cipher_key]
    for char in text:
        if char.upper() in cipher_dict:
            encrypted_text += cipher_dict[char.upper()]
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, cipher_key):
    decrypted_text = ""
    cipher_dict = cipher_dicts[cipher_key]
    reverse_dict = {v: k for k, v in cipher_dict.items()}
    for char in text:
        if char in reverse_dict:
            decrypted_text += reverse_dict[char]
        else:
            decrypted_text += char
    return decrypted_text

def update_text():
    input_text = text_input.get("1.0", "end-1c")
    cipher_key = cipher_var.get()
    encrypted = encrypt(input_text, cipher_key)
    text_output.delete("1.0", "end")
    text_output.insert("1.0", encrypted)

def decrypt_text():
    input_text = text_input.get("1.0", "end-1c")
    cipher_key = cipher_var.get()
    decrypted = decrypt(input_text, cipher_key)
    text_output.delete("1.0", "end")
    text_output.insert("1.0", decrypted)

root = ctk.CTk()
root.title("Масонський шифратор")
root.geometry("500x450")

text_input = ctk.CTkTextbox(root, width=450, height=100)
text_input.pack(pady=20)

cipher_var = ctk.StringVar(value="symbolic")
cipher_menu = ctk.CTkOptionMenu(root, variable=cipher_var, values=["symbolic", "latin", "cyrillic"])
cipher_menu.pack(pady=10)

encrypt_button = ctk.CTkButton(root, text="Шифрувати", command=update_text)
encrypt_button.pack(pady=10)

decrypt_button = ctk.CTkButton(root, text="Розшифрувати", command=decrypt_text)
decrypt_button.pack(pady=10)

text_output = ctk.CTkTextbox(root, width=450, height=100)
text_output.pack(pady=20)

root.mainloop()