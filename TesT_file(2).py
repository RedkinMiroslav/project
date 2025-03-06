import telebot

TOKEN = "7739112116:AAEQyvd3sBclyZzY-9NX_zJEYmP0Xew-NX8"
bot = telebot.TeleBot(TOKEN)
chat_id = 6128872022

def convert_unit(value, from_units, to_units):
    conversions = {
        "чашки": {"мілілітри": 240},
        "столових ложок": {"мілілітри": 15},
        "чайних ложок": {"мілілітри": 5},
        "склянки": {"мілілітри": 250}
    }
    if from_units in conversions and to_units in conversions[from_units]:
        return value * conversions[from_units][to_units]
    else:
        return None
@bot.message_handler(commands=["start"])
def send_hello(message):
    bot.send_message(message.chat.id,"Привіт! Я допоможу тобі конвертувати задану кількість чашок, ложок, склянок у мілілітри.\
        \nНапиши в такому форматі: 5 чашки в мілілітри.")
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text.lower()
    try:
        parts = text.split(" в ")
        value_and_from_unit = parts[0].split()
        to_unit = parts[1]
        value = float(value_and_from_unit[0])
        from_unit = value_and_from_unit[1]
        result = convert_unit(value, from_unit, to_unit)
        if result is not None:
            bot.send_message(message.chat.id, f"{value} {from_unit} = {result:.2f} {to_unit}")
        else:
            bot.send_message(message.chat.id, "Перепрошую, Спробуйте ще раз.")
    except Exception as e:
        bot.send_message(message.chat.id, "Виникла помилка. Спробуйте пізніше.")
bot.polling()
