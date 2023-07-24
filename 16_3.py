# Создайте метод класса для работы с БД,
# который обновляет значение name в записи с заданным id.
# Метод должен принимать два аргумента: id (INT) и новое значение для name (TEXT).

import sqlite3

def update_info(id: int, name: str):
    cursor.execute('''UPDATE table16_3 SET name = ? WHERE ID = ?''', (name, id))
    conn.commit()

def add_info(id: int, name: str):
    cursor.execute('''SELECT count(*) FROM table16_3 WHERE ID=?''', (id,))
    if cursor.fetchone()[0]:
       update_info(id, name)
    else:
        cursor.execute('''INSERT INTO table16_3(ID, name) VALUES (?, ?)''', (id, name))
        conn.commit()


conn = sqlite3.connect('name16_3.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS table16_3(ID INTEGER PRIMARY KEY, name TEXT)''')

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
    cursor.execute('''SELECT * FROM table16_3''')
    k = cursor.fetchall()
    print(k)


