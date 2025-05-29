import telebot

# --- Инициализация бота --- #
bot = telebot.TeleBot('7629716355:AAHnK0ECT5Uy7UQL4_Vixt2qGgwoLUfA6ZY')

# --- Функция шифрования --- #
def encrypt_text(text):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - 65 + 3) % 26 + 65)
            else:
                result += chr((ord(char) - 97 + 3) % 26 + 97)
        else:
            result += char
    return result

# --- Функция расшифровки --- #
def decrypt_text(text):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - 65 - 3) % 26 + 65)
            else:
                result += chr((ord(char) - 97 - 3) % 26 + 97)
        else:
            result += char
    return result

# --- Команда старта --- #
@bot.message_handler(commands=['start'])
def start_command(message):
    bot.reply_to(message, "🤖 Привет! Я бот для шифрования.\nКоманды: /encrypt <текст>, /decrypt <текст>")

# --- Команда помощи --- #
@bot.message_handler(commands=['help'])
def help_command(message):
    help_text = """📖 Доступные команды:
🔐 /encrypt <текст> - зашифровать текст
🔓 /decrypt <текст> - расшифровать текст
❓ /help - показать эту справку"""
    bot.reply_to(message, help_text)

# --- Команда шифрования --- #
@bot.message_handler(commands=['encrypt'])
def encrypt_command(message):
    text = message.text[9:]
    if not text:
        bot.reply_to(message, "⚠️ Введите текст для шифрования")
        return
    
    encrypted = encrypt_text(text)
    bot.reply_to(message, f"📝 Оригинал: {text}\n🔐 Зашифровано: {encrypted}")

# --- Команда расшифровки --- #
@bot.message_handler(commands=['decrypt'])
def decrypt_command(message):
    text = message.text[9:]
    if not text:
        bot.reply_to(message, "⚠️ Введите текст для расшифровки")
        return
    
    decrypted = decrypt_text(text)
    bot.reply_to(message, f"🔐 Зашифровано: {text}\n🔓 Расшифровано: {decrypted}")

# --- Обработка неизвестных команд --- #
@bot.message_handler(func=lambda message: True)
def default_handler(message):
    bot.reply_to(message, "❌ Неизвестная команда. Используйте /help")

if __name__ == "__main__":
    bot.polling()