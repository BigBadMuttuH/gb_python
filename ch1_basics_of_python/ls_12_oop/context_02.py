import sqlite3


class SQLiteContext:
    def __init__(self, name):
        self.name = name
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.name)
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, traceback):
        self.connection.commit()
        self.connection.close()
        self.cursor = self.connection = None


db = SQLiteContext('context2.db')
with db as cur:
    cur.execute("""CREATE TABLE IF NOT EXISTS user(name, age);""")
    cur.execute("""INSERT INTO user VALUES ('User2', 40);""")

