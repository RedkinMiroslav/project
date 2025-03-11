import telebot
import random

TOKEN = "7838766145:AAH1Qz14uITxxUhRtc39aiD-DKgYW0sLmvI"
bot = telebot.TeleBot(TOKEN)

UPLOAD_FOLDER = r"D:\memes/"
memes = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg", "6.jpg", "7.jpg", "8.jpg", "9.jpg", "10.jpg", "11.jpg", "12.jpg", "13.jpg", "14.jpg", "15.jpg", "16.jpg", "17.jpg", "18.jpg", "19.jpg", "20.jpg"]

@bot.message_handler(commands=["start"])
def send_hello(message):
    bot.send_message(message.chat.id, "Вітаю тебе в мем-боті! Ось команди які доступні: /meme, /photo, /count")

@bot.message_handler(content_types=["photo"])
def receive_meme(message):
    file_info = bot.get_file(message.photo[-1].file.id)
    downloaded_file = bot.download_file(file_info.file_path)
    file_name = str(len(memes) + 1) + ".jpg"
    
    with open(UPLOAD_FOLDER + file_name, "wb") as new_file:
        new_file.write(downloaded_file)
    memes.append(file_name)
    bot.reply_to(message, "Мем отримано і збережено!")

@bot.message_handler(commands=["meme"])
def send_random_meme(message):
    if memes:
        meme = random.choice(memes)
        with open(UPLOAD_FOLDER + meme, "rb") as photo:
            sent_message = bot.send_photo(message.chat.id, photo)
            bot.send_message(message.chat.id, "Тобі сподобався мем? Відповідай: 👍 або 👎")
            bot.register_next_step_handler(sent_message, process_rating)
    else:
        bot.reply_to(message, "Мемів поки немає 😢")

def process_rating(message):
    if message.text == "👍":
        bot.send_message(message.chat.id, "Радий, що сподобалось! 😊")
    elif message.text == "👎":
        bot.send_message(message.chat.id, "Шкода, спробую знайти щось краще наступного разу! 😢")
    else:
        bot.send_message(message.chat.id, "Не зрозумів твою відповідь. Будь ласка, використовуй 👍 або 👎")

@bot.message_handler(commands=["count"])
def meme_count(message):
    if memes:
        memes_count = len(memes)
        bot.reply_to(message, f"Додано мемів: {memes_count}")
    else:
        bot.reply_to(message, "Мемів не знайдено!")

@bot.message_handler(commands=["photo"])
def send_all_memes(message):
    if memes:
        for meme in memes:
            try:
                with open(UPLOAD_FOLDER + meme, "rb") as photo:
                    bot.send_photo(message.chat.id, photo)
            except FileNotFoundError:
                bot.send_message(message.chat.id, f"Файл {meme} не знайдено.")
    else:
        bot.reply_to(message, "Мемів не знайдено!")

bot.polling(none_stop=True)