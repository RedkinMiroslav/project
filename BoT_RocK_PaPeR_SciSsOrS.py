import telebot
import random

TELEGRAM_BOT_TOKEN = "8028979083:AAGP-BippXolATboa1m-GXRq0mCFlMzlHzQ"

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton(text="Каміння", callback_data="Rock"))
    keyboard.add(telebot.types.InlineKeyboardButton(text="Ножиці", callback_data="Scissors"))
    keyboard.add(telebot.types.InlineKeyboardButton(text="Папір", callback_data="Paper"))
    bot.send_message(message.chat.id, "Виберіть:", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def button(call):
    choice = call.data
    bot_choice = random.choice(["Rock", "Scissors", "Paper"])

    if choice == bot_choice:
        result = "Нічия!"
    elif (choice == "Rock" and bot_choice == "Scissors") or \
         (choice == "Scissors" and bot_choice == "Paper") or \
         (choice == "Paper" and bot_choice == "Rock"):
        result = "Вы_Виграли!"
    else:
        result = "Бот_Виграв!"

    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"Ви_Обрали: {choice}\nБот_Виграв: {bot_choice}\nРезультат: {result}")

@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(message.chat.id, "Цей_Бот_Дає_Змогу_Грати_В_Гру - Камінь, Ножиці, Папір!")

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "Для_Початку_Гри_Надішліть_Команду - /start\
    \nПотім_Виберіть_Камінь, Ножиці_Або_Папір, Натиснувши_На_Відповідну_Кнопку!")

bot.polling()