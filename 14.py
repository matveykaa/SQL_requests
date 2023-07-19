import sqlite3

conn = sqlite3.connect('name.db')
cursor = conn.cursor()

cursor.execute(''' CREATE TABLE IF NOT EXISTS table_one (ID INTEGER PRIMARY KEY AUTOINCREMENT, column_one INT)''')

input_data = input('Введите параметры для бд - ')
list_data = input_data.split()
chislo = 77

if len(list_data) == 1:
    if list_data[0].isnumeric():
        cursor.execute('''INSERT INTO table_one(column_one) VALUES (?)''', (int(list_data[0]),))
        conn.commit()
    else:
        print('Параметр не число')
elif len(list_data) == 2:
    if list_data[1].isnumeric():
        cursor.execute('''DELETE FROM table_one WHERE ID = (SELECT MIN(ID) FROM table_one)''')
        conn.commit()
    else:
        print('Второй параметр не число')
elif len(list_data) == 3:
    if list_data[2].isnumeric():
        cursor.execute('''UPDATE table_one SET column_one = ? WHERE ID = (SELECT ID FROM table_one LIMIT 1 OFFSET 2)''', (chislo,))
        conn.commit()
    else:
        print('Третий параметр не число')

cursor.execute('''SELECT * FROM table_one''')
k = cursor.fetchall()
print(k)
