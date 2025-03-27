import sqlite3
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Токен бота
TOKEN = "7753771624:AAET2iwRX4YeBHkTKaNGHj2VybLvVgvDV5Y"

# Функция для старта
def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    keyboard = [['Понедельник', 'Вторник', 'Среда'], ['Четверг', 'Пятница']]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)

    update.message.reply_text(
        f"Привет, {user.first_name}! Выбери день недели, чтобы получить расписание.",
        reply_markup=reply_markup
    )

# Функция получения расписания из БД
def get_schedule(update: Update, context: CallbackContext) -> None:
    day = update.message.text  # Получаем день от пользователя
    conn = sqlite3.connect("schedule.db")
    cursor = conn.cursor()

    cursor.execute("SELECT lesson_number, time, subject, teacher FROM lessons WHERE day = ? ORDER BY lesson_number", (day,))
    lessons = cursor.fetchall()
    conn.close()

    if lessons:
        response = f"📅 Расписание на {day}:\n"
        for num, time, subject, teacher in lessons:
            response += f"📖 {num}-й урок ({time})\n   {subject} - {teacher}\n\n"
    else:
        response = "❌ Расписание на этот день не найдено."

    update.message.reply_text(response)

# Основная функция для запуска бота
def main() -> None:
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, get_schedule))

    print("Бот запущен...")
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
