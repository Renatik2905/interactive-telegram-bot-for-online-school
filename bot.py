from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Функция для старта
def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_text(
        f"Привет, {user.first_name}! Я помогу тебе с расписанием уроков. Нажми на кнопку, чтобы получить расписание.",
        reply_markup=ReplyKeyboardMarkup([['Получить расписание']], one_time_keyboard=True)
    )

# Функция для получения расписания
def get_schedule(update: Update, context: CallbackContext) -> None:
    # Здесь можно добавить настоящие данные расписания
    schedule = "Понедельник: Математика, Вторник: Физика, Среда: Химия"
    update.message.reply_text(f"Ваше расписание:\n{schedule}")

# Основная функция для запуска бота
def main() -> None:
    updater = Updater("7753771624:AAET2iwRX4YeBHkTKaNGHj2VybLvVgvDV5Y")
    
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, get_schedule))
    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
