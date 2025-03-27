import sqlite3

# Подключаемся к базе данных
conn = sqlite3.connect("schedule.db")
cursor = conn.cursor()

# Создаём таблицу с расписанием
cursor.execute('''
CREATE TABLE IF NOT EXISTS lessons (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    day TEXT NOT NULL,
    lesson_number INTEGER NOT NULL,
    time TEXT NOT NULL,
    subject TEXT NOT NULL,
    teacher TEXT NOT NULL
)
''')

# Заполняем расписание (пример для всей недели)
data = [
    # Понедельник
    ("Понедельник", 1, "08:00-08:45", "Математика", "Иванов И.И."),
    ("Понедельник", 2, "08:55-09:40", "Русский язык", "Петрова А.В."),
    ("Понедельник", 3, "09:50-10:35", "Физика", "Сидоров С.С."),
    ("Понедельник", 4, "10:45-11:30", "Английский язык", "Козлова Е.Н."),
    ("Понедельник", 5, "11:40-12:25", "История", "Морозов Д.Д."),
    ("Понедельник", 6, "12:35-13:20", "Биология", "Никитина Л.П."),

    # Вторник
    ("Вторник", 1, "08:00-08:45", "Литература", "Козлова Е.Н."),
    ("Вторник", 2, "08:55-09:40", "Алгебра", "Иванов И.И."),
    ("Вторник", 3, "09:50-10:35", "География", "Кузнецов В.В."),
    ("Вторник", 4, "10:45-11:30", "Химия", "Сидоров С.С."),
    ("Вторник", 5, "11:40-12:25", "Физкультура", "Смирнов А.А."),
    ("Вторник", 6, "12:35-13:20", "Информатика", "Павлов Е.Г."),

    # Среда
    ("Среда", 1, "08:00-08:45", "Обществознание", "Фёдорова Л.В."),
    ("Среда", 2, "08:55-09:40", "Английский язык", "Козлова Е.Н."),
    ("Среда", 3, "09:50-10:35", "Физика", "Сидоров С.С."),
    ("Среда", 4, "10:45-11:30", "Геометрия", "Иванов И.И."),
    ("Среда", 5, "11:40-12:25", "Химия", "Сидоров С.С."),
    ("Среда", 6, "12:35-13:20", "Технология", "Алексеев Н.Н."),

    # Четверг
    ("Четверг", 1, "08:00-08:45", "Биология", "Никитина Л.П."),
    ("Четверг", 2, "08:55-09:40", "Физика", "Сидоров С.С."),
    ("Четверг", 3, "09:50-10:35", "Русский язык", "Петрова А.В."),
    ("Четверг", 4, "10:45-11:30", "Математика", "Иванов И.И."),
    ("Четверг", 5, "11:40-12:25", "История", "Морозов Д.Д."),
    ("Четверг", 6, "12:35-13:20", "ОБЖ", "Павлов Е.Г."),

    # Пятница
    ("Пятница", 1, "08:00-08:45", "Литература", "Козлова Е.Н."),
    ("Пятница", 2, "08:55-09:40", "Алгебра", "Иванов И.И."),
    ("Пятница", 3, "09:50-10:35", "Информатика", "Павлов Е.Г."),
    ("Пятница", 4, "10:45-11:30", "Физкультура", "Смирнов А.А."),
    ("Пятница", 5, "11:40-12:25", "Обществознание", "Фёдорова Л.В."),
    ("Пятница", 6, "12:35-13:20", "География", "Кузнецов В.В."),
]

cursor.executemany("INSERT INTO lessons (day, lesson_number, time, subject, teacher) VALUES (?, ?, ?, ?, ?)", data)
conn.commit()
conn.close()

print("База данных обновлена! 📚")
