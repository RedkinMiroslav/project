import telebot
from telebot import types

TOKEN = "7739112116:AAEQyvd3sBclyZzY-9NX_zJEYmP0Xew-NX8"
bot = telebot.TeleBot(TOKEN)

conversions = {
    "об'єм": {
        "чашки": {"мілілітри": 240, "літри": 0.24},
        "столові ложки": {"мілілітри": 15, "літри": 0.015},
        "чайні ложки": {"мілілітри": 5, "літри": 0.005},
        "склянки": {"мілілітри": 250, "літри": 0.25},
        "літри": {"мілілітри": 1000, "чашки": 4.167, "столові ложки": 66.67, "чайні ложки": 200},
        "мілілітри": {"літри": 0.001, "чашки": 0.004167, "столові ложки": 0.06667, "чайні ложки": 0.2}
    },
    "вага": {
        "грами": {"кілограми": 0.001, "фунти": 0.00220462},
        "кілограми": {"грами": 1000, "фунти": 2.20462},
        "фунти": {"грами": 453.592, "кілограми": 0.453592}
    }
}

user_data = {}

@bot.message_handler(commands=["start"])
def send_hello(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Об\'єм')
    itembtn2 = types.KeyboardButton('Вага')
    markup.add(itembtn1, itembtn2)
    bot.send_message(message.chat.id, "Привіт! Я допоможу тобі конвертувати одиниці вимірювання. Вибери, що ти хочеш конвертувати:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ["Об'єм", "Вага"])
def handle_unit_type(message):
    user_data[message.chat.id] = {"unit_type": message.text.lower()}
    markup = types.ReplyKeyboardMarkup(row_width=3)
    items = list(conversions[user_data[message.chat.id]["unit_type"]].keys())
    for item in items:
        markup.add(types.KeyboardButton(item.capitalize()))
    bot.send_message(message.chat.id, f"Вибери одиницю вимірювання {user_data[message.chat.id]['unit_type']}:", reply_markup=markup)
    bot.register_next_step_handler(message, handle_from_unit)

def handle_from_unit(message):
    user_data[message.chat.id]["from_unit"] = message.text.lower()
    if user_data[message.chat.id]["from_unit"] in conversions[user_data[message.chat.id]["unit_type"]]:
        markup = types.ReplyKeyboardMarkup(row_width=3)
        items = list(conversions[user_data[message.chat.id]["unit_type"]][user_data[message.chat.id]["from_unit"]].keys())
        for item in items:
            markup.add(types.KeyboardButton(item.capitalize()))
        bot.send_message(message.chat.id, f"Вибери одиницю, в яку хочеш конвертувати {user_data[message.chat.id]['from_unit']}:", reply_markup=markup)
        bot.register_next_step_handler(message, handle_to_unit)
    else:
        bot.send_message(message.chat.id, "Неправильна одиниця вимірювання. Спробуйте ще раз.")

def handle_to_unit(message):
    user_data[message.chat.id]["to_unit"] = message.text.lower()
    if user_data[message.chat.id]["to_unit"] in conversions[user_data[message.chat.id]["unit_type"]][user_data[message.chat.id]["from_unit"]]:
        bot.send_message(message.chat.id, f"Введіть кількість {user_data[message.chat.id]['from_unit']}:")
        bot.register_next_step_handler(message, handle_value)
    else:
        bot.send_message(message.chat.id, "Неправильна одиниця вимірювання. Спробуйте ще раз.")

def handle_value(message):
    try:
        value = float(message.text)
        result = value * conversions[user_data[message.chat.id]["unit_type"]][user_data[message.chat.id]["from_unit"]][user_data[message.chat.id]["to_unit"]]
        bot.send_message(message.chat.id, f"{value} {user_data[message.chat.id]['from_unit']} = {result:.2f} {user_data[message.chat.id]['to_unit']}")
    except ValueError:
        bot.send_message(message.chat.id, "Неправильне значення. Введіть число.")
    except Exception as e:
        bot.send_message(message.chat.id, f"Виникла помилка: {e}")
    del user_data[message.chat.id]

bot.polling()