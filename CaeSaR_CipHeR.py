import tkinter as tk

is_text_encrypted = False

def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if 'a' <= char <= 'z': # --- Англ. строчные --- #
            base = ord('a')
            result += chr((ord(char) - base + shift) % 26 + base) if mode == 'encrypt' else chr((ord(char) - base - shift + 26) % 26 + base)
        elif 'A' <= char <= 'Z': # --- Англ. заглавные --- #
            base = ord('A')
            result += chr((ord(char) - base + shift) % 26 + base) if mode == 'encrypt' else chr((ord(char) - base - shift + 26) % 26 + base)
        elif 'а' <= char <= 'я': # --- Рус./Укр. строчные --- #
            base = ord('а')
            result += chr((ord(char) - base + shift) % 32 + base) if mode == 'encrypt' else chr((ord(char) - base - shift + 32) % 32 + base)
        elif 'А' <= char <= 'Я': # --- Рус./Укр. заглавные --- #
            base = ord('А')
            result += chr((ord(char) - base + shift) % 32 + base) if mode == 'encrypt' else chr((ord(char) - base - shift + 32) % 32 + base)
        elif '0' <= char <= '9': # --- Цифры --- #
            base = ord('0')
            result += chr((ord(char) - base + shift) % 10 + base) if mode == 'encrypt' else chr((ord(char) - base - shift + 10) % 10 + base)
        else: # - Другие символы
            result += char
    return result

def process_text_toggle():
    global is_text_encrypted
    
    text = text_area.get("1.0", tk.END).strip()
    shift_str = shift_input.get().strip()

    if not text or not shift_str:
        return 
    
    try:
        shift = int(shift_str)
    except ValueError:
        return
    
    if is_text_encrypted:
        processed_text = caesar_cipher(text, shift, 'decrypt')
        is_text_encrypted = False 
    else:
        processed_text = caesar_cipher(text, shift, 'encrypt')
        is_text_encrypted = True 
        
    text_area.delete("1.0", tk.END)
    text_area.insert("1.0", processed_text)

# --- Настройка GUI --- #

window = tk.Tk()
window.title("CaeSaR_CipHeR")
window.geometry("400x280")
window.resizable(False, False)

tk.Label(window, text="TexT:").pack(pady=5)
text_area = tk.Text(window, height=8, width=40)
text_area.pack(pady=5)

shift_frame = tk.Frame(window)
shift_frame.pack(pady=5)
tk.Label(shift_frame, text="SHIFT:").pack(side=tk.LEFT)
shift_input = tk.Entry(shift_frame, width=5)
shift_input.insert(0, "3")
shift_input.pack(side=tk.LEFT, padx=5)

button_frame = tk.Frame(window)
button_frame.pack(pady=10)

tk.Button(button_frame, text="ToGGle (ENCrypt/DECrypt)", command=process_text_toggle).pack(padx=10)

window.mainloop()