# Создайте метод класса для работы с БД, который выводит все записи из таблицы.


import sqlite3

def print_all():
    cursor.execute('''SELECT * FROM table16_5''')
    k = cursor.fetchall()
    print(k)

conn = sqlite3.connect('name16_5.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS table16_5(ID INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)''')

input_data = input('Введите text - ')
cursor.execute('''INSERT INTO table16_5(name) VALUES (?)''', (input_data,))
conn.commit()
print_all()