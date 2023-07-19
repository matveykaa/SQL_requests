import sqlite3

conn = sqlite3.connect('name.db')
cursor = conn.cursor()

cursor.execute(''' CREATE TABLE IF NOT EXISTS table_one (ID INTEGER PRIMARY KEY AUTOINCREMENT, column_one INT)''')

input_data = input('Введите параметры для бд - ')
list_data = input_data.split()
chislo = 77

if len(list_data) == 1:
    cursor.execute('''INSERT INTO table_one(column_one) VALUES (?)''', (int(list_data[0]),))
    conn.commit()
elif len(list_data) == 2:
    if type(list_data[1]) is int:
        cursor.execute('''DELETE FROM table_one WHERE ID = 1''')
        conn.commit()
elif len(list_data) == 3:
    if type(list_data[2]) is int:
        cursor.execute('''UPDATE table_one SET column_one = ? WHERE ID = 3''', (chislo,))
        conn.commit()

cursor.execute('''SELECT * FROM table_one''')
k = cursor.fetchall()
print(k)
