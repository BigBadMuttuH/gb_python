import sqlite3


connection = sqlite3.connect('context1.db')
cursor = connection.cursor()
cursor.execute("""create table if not exists users(name, age);""")
cursor.execute("""insert into users values ('User', 45);""")
connection.commit()
cursor.close()
