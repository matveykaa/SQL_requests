# Создайте метод класса для работы с БД,
# который удаляет запись с заданным id.
# Метод принимает один аргумент - id (INT).


import sqlite3

def delete_info(id: int):
    cursor.execute('''DELETE FROM table16_4 WHERE ID = ?''', (id,))
    conn.commit()


conn = sqlite3.connect('name16_4.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS table16_4(ID INTEGER PRIMARY KEY AUTOINCREMENT, txt TEXT)''')

while True:
    print('Выберите пукт: ')
    print('1 - Добавить запись    2 - Удалить запись   3 - Выход\n')
    option = int(input())
    if option == 3:
        raise KeyboardInterrupt('Exit')
    elif option == 1:
        input_data = input('Введите text - ')
        cursor.execute('''INSERT INTO table16_4(txt) VALUES (?)''', (input_data,))
        conn.commit()
    elif option == 2:
        input_data = input('Введите id - ')
        if input_data.isnumeric():
            cursor.execute('''DELETE FROM table16_4 WHERE ID = ?''', (int(input_data),))
            conn.commit()
        else:
            print('\n- - ID should be numeric - -')


    cursor.execute('''SELECT * FROM table16_4''')
    k = cursor.fetchall()
    print(k)