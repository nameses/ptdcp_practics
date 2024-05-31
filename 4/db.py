import sqlite3


def create_database():
    conn = sqlite3.connect('medical_institute.db')
    cursor = conn.cursor()

    # Створення таблиці пацієнтів
    cursor.execute('''CREATE TABLE IF NOT EXISTS patients (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        age INTEGER NOT NULL,
                        gender TEXT NOT NULL,
                        diagnosis TEXT NOT NULL
                      )''')

    # Можна додати інші таблиці, наприклад для лікарів та призначень

    conn.commit()
    conn.close()


create_database()
