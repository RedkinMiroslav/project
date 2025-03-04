import telebot
import schedule
import time

TOKEN = "7569583289:AAGYniyW1l5WsQc2VCIbI0dF1__KZTGOBwU"
bot = telebot.TeleBot(TOKEN)

CHAT_ID = 6128872022

def send_morning_reminder():
    bot.send_message(CHAT_ID, "☀️ Доброго ранку! Час для ранкової зарядки або медитації!")

def send_midday_reminder():
    bot.send_message(CHAT_ID, "🍽️ Не забудьте зробити перерву на обід! Ваш мозок потребує відпочинку.")

def send_evening_reminder():
    bot.send_message(CHAT_ID, "🌙 Вечір - час для відпочинку. Можливо, почитати книгу або послухати музику?")

def send_achievement_reminder():
    bot.send_message(CHAT_ID, "🏆 Хей, не забудь про своє досягнення! Ти сьогодні молодець!")

def send_flower_reminder():
    bot.send_message(CHAT_ID, "🌷 Час полити квіти! Вони чекають на твою турботу.")

schedule.every().day.at("08:00").do(send_morning_reminder)
schedule.every().day.at("13:00").do(send_midday_reminder)
schedule.every().day.at("20:00").do(send_evening_reminder)
schedule.every().day.at("16:00").do(send_achievement_reminder)
schedule.every().day.at("10:00").do(send_flower_reminder)

while True:
    try:
        schedule.run_pending()
        time.sleep(1)
    except Exception as e:
        print(f"Помилка: {e}")
        time.sleep(5)
