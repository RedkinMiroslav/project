import telebot
from telebot import types

BOT_TOKEN = "7712257279:AAFgJ6ku_s0OYWmAXyESMa59geG74No7MMU"

bot = telebot.TeleBot(BOT_TOKEN)

# --- ХРАНИЛИЩЕ ДАННЫХ --- #
user_data = {}
user_results = {}

# --- ИНФОРМАЦИОННЫЕ ТЕКСТЫ --- #
INFO = {
    "html": "<b>HTML (HyperText Markup Language)</b> — это язык разметки, который используется для структурирования и отображения содержимого веб-страницы. Он является основой любого сайта.",
    "css": "<b>CSS (Cascading Style Sheets)</b> — это язык стилей, который используется для описания внешнего вида документа, написанного на HTML. С помощью CSS задают цвета, шрифты, отступы и расположение элементов.",
    "javascript": "<b>JavaScript (JS)</b> — это язык программирования, который делает веб-страницы интерактивными. Он позволяет реагировать на действия пользователя, изменять контент страницы и отправлять запросы на сервер.",
    "python": "<b>Python</b> — это высокоуровневый язык программирования общего назначения, известный своим простым и чистым синтаксисом. Он используется в веб-разработке, анализе данных, машинном обучении и автоматизации."
}

# --- ВОПРОСЫ ДЛЯ ТЕСТОВ --- #
QUESTIONS = {
    "html": [
        {
            "question": "Какой тег используется для создания самой большой заголовка?",
            "options": ["<h6>", "<h1>", "<h2>", "<head>"],
            "answer": "<h1>"
        },
        {
            "question": "Какой тег используется для вставки изображения?",
            "options": ["<image>", "<pic>", "<img>", "<src>"],
            "answer": "<img>"
        },
        {
            "question": "Какой тега используется для создания ссылки?",
            "options": ["<a>", "<link>", "<ref>", "<href>"],
            "answer": "<a>"
        }
    ],
    "css": [
        {
            "question": "Какое свойство изменяет цвет текста?",
            "options": ["font-color", "text-color", "color", "background-color"],
            "answer": "color"
        },
        {
            "question": "Как выбрать элемент с id 'header'?",
            "options": [".header", "#header", "header", "*header"],
            "answer": "#header"
        },
        {
            "question": "Какое свойство задает внешний отступ?",
            "options": ["padding", "border", "margin", "indent"],
            "answer": "margin"
        }
    ],
    "javascript": [
        {
            "question": "Как объявить переменную в JavaScript?",
            "options": ["var", "let", "const", "Все варианты верны"],
            "answer": "Все варианты верны"
        },
        {
            "question": "Какой символ используется для строгого сравнения?",
            "options": ["==", "===", "=", "!="],
            "answer": "==="
        },
        {
            "question": "Как вывести что-либо в консоль?",
            "options": ["console.log()", "print()", "log()", "debug()"],
            "answer": "console.log()"
        }
    ],
    "python": [
        {
            "question": "Как создать комментарий в Python?",
            "options": ["// Комментарий", "/* Комментарий */", "# Комментарий", ""],
            "answer": "# Комментарий"
        },
        {
            "question": "Какая функция возвращает длину объекта?",
            "options": ["size()", "length()", "count()", "len()"],
            "answer": "len()"
        },
        {
            "question": "Как называется встроенный тип данных для списков?",
            "options": ["array", "list", "tuple", "dictionary"],
            "answer": "list"
        }
    ]
}
# --- Обработчик команды /start --- #
@bot.message_handler(commands=["start"])
def send_welcome(message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    
    # --- Инициализация хранилищ для нового пользователя --- #
    user_data[user_id] = {}
    if user_id not in user_results:
        user_results[user_id] = []

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    btn_info = types.KeyboardButton("/info")
    btn_test = types.KeyboardButton("/test")
    btn_result = types.KeyboardButton("/result")
    btn_commands = types.KeyboardButton("/commands")
    markup.add(btn_info, btn_test)
    markup.add(btn_result, btn_commands)

    bot.send_message(message.chat.id,
                     f"👋 Привет, {user_name}!\nЯ бот 'Тест Знаний'. Выбери, что ты хочешь сделать:",
                     reply_markup=markup)

# --- Обработчик команды /commands --- #
@bot.message_handler(commands=["commands"])
def send_commands(message):
    commands_list = [
        "/start - Перезапуск бота",
        "/info - Получить информацию по теме",
        "/test - Начать новый тест",
        "/result - Посмотреть все ваши результаты",
        "/commands - Показать это сообщение"
    ]
    bot.send_message(message.chat.id, "📌 **Доступные команды:**\n" + "\n".join(commands_list), parse_mode="Markdown")

# --- Обработчик команды /info --- #
@bot.message_handler(commands=["info"])
def request_info(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("HTML", callback_data="info_html")
    btn2 = types.InlineKeyboardButton("CSS", callback_data="info_css")
    btn3 = types.InlineKeyboardButton("JavaScript", callback_data="info_javascript")
    btn4 = types.InlineKeyboardButton("Python", callback_data="info_python")
    markup.add(btn1, btn2, btn3, btn4)

    bot.send_message(message.chat.id, "📚 Выбери тему, по которой хочешь получить информацию:", reply_markup=markup)

# --- Обработчик команды /test --- #
@bot.message_handler(commands=["test"])
def request_test(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("HTML", callback_data="test_html")
    btn2 = types.InlineKeyboardButton("CSS", callback_data="test_css")
    btn3 = types.InlineKeyboardButton("JavaScript", callback_data="test_javascript")
    btn4 = types.InlineKeyboardButton("Python", callback_data="test_python")
    markup.add(btn1, btn2, btn3, btn4)

    bot.send_message(message.chat.id, "📝 Выбери тему для теста:", reply_markup=markup)

# --- Обработчик команды /result --- #
@bot.message_handler(commands=["result"])
def show_results(message):
    user_id = message.from_user.id
    if user_id not in user_results or not user_results[user_id]:
        bot.send_message(message.chat.id, "📊 Вы еще не прошли ни одного теста. Используйте /test, чтобы начать!")
        return

    results_text = "🏆 **Ваши предыдущие результаты:**\n\n"
    for i, result in enumerate(user_results[user_id], 1):
        results_text += f"{i}. Тема: *{result['topic'].upper()}* - {result['score']} из {result['total']}\n"
    
    bot.send_message(message.chat.id, results_text, parse_mode="Markdown")

# --- Обработчик callback-кнопок для информации --- #
@bot.callback_query_handler(func=lambda call: call.data.startswith("info_"))
def callback_info(call):
    topic = call.data.split("_")[1]
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, INFO[topic], parse_mode="HTML")

# --- Обработчик callback-кнопок для начала теста --- #
@bot.callback_query_handler(func=lambda call: call.data.startswith("test_"))
def callback_test_start(call):
    user_id = call.from_user.id
    topic = call.data.split("_")[1]
    
    user_data[user_id] = {
        "topic": topic,
        "question_index": 0,
        "score": 0
    }
    
    bot.answer_callback_query(call.id)
    send_question(call.message.chat.id, user_id)

# --- Обработчик callback-кнопок для ответов на вопросы теста --- #
@bot.callback_query_handler(func=lambda call: call.data.startswith("answer_"))
def callback_answer(call):
    user_id = call.from_user.id
    data = call.data.split("_")
    
    topic = data[1]
    question_index = int(data[2])
    selected_option_index = int(data[3])
    
    # --- Проверка, что пользователь отвечает на текущий вопрос --- #
    if user_data.get(user_id) is None or user_data[user_id]["question_index"] != question_index:
        bot.answer_callback_query(call.id, "Этот вопрос уже неактуален.")
        return

    question = QUESTIONS[topic][question_index]
    selected_answer = question["options"][selected_option_index]
    
    if selected_answer == question["answer"]:
        user_data[user_id]["score"] += 1
        feedback = "✅ Правильно!"
    else:
        feedback = f"❌ Неправильно. Верный ответ: {question['answer']}"
        
    bot.edit_message_text(chat_id=call.message.chat.id,
                          message_id=call.message.message_id,
                          text=f"{call.message.text}\n\nВаш ответ: {selected_answer}\n{feedback}",
                          reply_markup=None)
    
    user_data[user_id]["question_index"] += 1
    
    # --- Отправляем следующий вопрос или завершаем тест --- #
    if user_data[user_id]["question_index"] < len(QUESTIONS[topic]):
        send_question(call.message.chat.id, user_id)
    else:
        finish_test(call.message.chat.id, user_id)
# --- Функция для отправки вопроса --- #
def send_question(chat_id, user_id):
    data = user_data[user_id]
    topic = data["topic"]
    question_index = data["question_index"]
    
    question_data = QUESTIONS[topic][question_index]
    question_text = f"**Вопрос {question_index + 1}/{len(QUESTIONS[topic])}:**\n\n{question_data['question']}"
    
    markup = types.InlineKeyboardMarkup()
    for i, option in enumerate(question_data["options"]):
        callback_data = f"answer_{topic}_{question_index}_{i}"
        markup.add(types.InlineKeyboardButton(option, callback_data=callback_data))
        
    bot.send_message(chat_id, question_text, reply_markup=markup, parse_mode="Markdown")

# --- Функция для завершения теста --- #
def finish_test(chat_id, user_id):
    data = user_data[user_id]
    topic = data["topic"]
    score = data["score"]
    total_questions = len(QUESTIONS[topic])
    
    # --- Сохраняем результат --- #
    user_results.setdefault(user_id, []).append({
        "topic": topic,
        "score": score,
        "total": total_questions
    })
    
    # --- Очищаем временные данные --- #
    del user_data[user_id]
    
    result_text = f"🎉 **Тест завершен!** 🎉\n\nТема: *{topic.upper()}*\nПравильных ответов: *{score}* из *{total_questions}*"
    result_text += "\n\nЧтобы начать новый тест, используй /test."
    
    bot.send_message(chat_id, result_text, parse_mode="Markdown")

# --- ЗАПУСК БОТА --- #
if __name__ == "__main__":
    print("Бот запущен...")
    bot.polling(none_stop=True)