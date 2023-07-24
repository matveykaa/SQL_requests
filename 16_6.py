# Создайте метод класса для работы с БД, который удаляет все записи из таблицы

import sqlite3

def delete_all(cursor):
    cursor.execute('''DELETE FROM table16_6''')
    conn.commit()

def print_all():
    cursor.execute('''SELECT * FROM table16_6''')
    k = cursor.fetchall()
    print(k)

conn = sqlite3.connect('name16_6.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS table16_6(ID INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)''')

input_data = input('Введите text - ')
cursor.execute('''INSERT INTO table16_6(name) VALUES (?)''', (input_data,))
conn.commit()


input_data = input('Удалить все запись в таблице? (y/n)\n')
if input_data == 'y':
    delete_all(cursor)
elif input_data == 'n':
    print_all()
else:
    print('- - Input error - -')
