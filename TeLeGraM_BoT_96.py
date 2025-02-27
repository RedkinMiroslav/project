import telebot
import random
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot("8009708072:AAEWBhcPYxUsbccaCGbCr0s5Pd5keXIPuxw") 

facts = {"Планети":
        ["Юпітер - найбільша планета Сонячної системи.",
        "Венера - найгарячіша планета.",
        "Марс називають Червоною планетою.",
        "Сатурн відомий своїми кільцями.",
        "Уран обертається на боці.",
        "Нептун - найвіддаленіша планета від Сонця."],
    "Зорі": 
        ["Сонце - найближча до нас зоря.",
        "Проксима Центавра - найближча до Сонця зоря.",
        "Бетельгейзе - червоний надгігант.",
        "Сиріус - найяскравіша зоря на нічному небі."],
    "Чорні діри": 
        ["Чорні діри мають надзвичайно сильну гравітацію.",
        "Ніщо не може покинути чорну діру, навіть світло.",
        "Існування чорних дір було передбачено Ейнштейном.",
        "В центрі більшості галактик є чорні діри."]}

    

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "Привіт! Я твій бот, який розповість цікаві факти про космос!")
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton("Планети")
    button2 = KeyboardButton("Зорі")
    button3 = KeyboardButton("Чорні діри")
    keyboard.add(button1, button2, button3)
    bot.send_message(message.chat.id, "Обери тему:", reply_markup=keyboard)

@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
    if message.text in facts:
        topic = message.text
        fact = random.choice(facts[topic])
        bot.send_message(message.chat.id, f"Цікавий факт про {topic}:\n{fact}")
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = KeyboardButton("Планети")
        button2 = KeyboardButton("Зорі")
        button3 = KeyboardButton("Чорні діри")
        keyboard.add(button1, button2, button3)
        bot.send_message(message.chat.id, "Бажаєш дізнатися ще?", reply_markup=keyboard)
    else:
        bot.send_message(message.chat.id, "Я не знаю такої команди, оберіть тему з кнопок.")

bot.polling()