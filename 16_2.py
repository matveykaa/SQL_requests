# Создайте метод класса для работы с БД, который добавляет новую запись в таблицу.
# Метод должен принимать два аргумента: id (INT) и name (TEXT).
# Запись должна быть добавлена только в том случае, если такого id в таблице еще нет.

import sqlite3

def add_info(id:int, name: str):
    cursor.execute('''SELECT count(*) FROM table16_2 WHERE ID=?''', (id,))
    if cursor.fetchone()[0]:
        print('\n- - ID exists - -')
    else:
        cursor.execute('''INSERT INTO table16_2(ID, name) VALUES (?, ?)''', (id, name))
        conn.commit()


conn = sqlite3.connect('name16_2.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS table16_2(ID INTEGER PRIMARY KEY, name TEXT)''')

while True:
    input_data = input('Введите id и name для таблицы - ')
    if input_data == '':
        raise KeyboardInterrupt('Exit')
    inp_name = input_data.split()[1]
    if input_data.split()[0].isnumeric():
        inp_id = int(input_data.split()[0])
        add_info(inp_id, inp_name)
    else:
        print('\n- - ID should be numeric - -')
    cursor.execute('''SELECT * FROM table16_2''')
    k = cursor.fetchall()
    print(k)