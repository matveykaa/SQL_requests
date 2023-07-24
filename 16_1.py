import sqlite3


conn = sqlite3.connect('name16_1.db')
cursor = conn.cursor()
def check_table_exists(table_name, cursor):
    cursor.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
    return cursor.fetchone()[0] == 1

if check_table_exists("table16_1", cursor):
    raise KeyboardInterrupt('Table already exists')
else:
    cursor.execute(''' CREATE TABLE IF NOT EXISTS table16_1 (ID INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)''')

    input_name = input('Введите имя - ')

    cursor.execute('''INSERT INTO table16_1(name) VALUES (?)''', (input_name,))
    conn.commit()

cursor.execute('''SELECT * FROM table16_1''')
k = cursor.fetchall()
print(k)
