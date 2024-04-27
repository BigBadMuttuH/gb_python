import psycopg2


class PostgresConnection:
    def __init__(self, dsn):
        """
        Инициализация соединения.
        DSN (Data Source Name) - строка соединения с базой данных.
        """
        self.dsn = dsn
        self.conn = None

    def __enter__(self):
        """
        Устанавливает соединение и возвращает его для использования в блоке with.
        """
        self.conn = psycopg2.connect(self.dsn)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Закрывает соединение после выхода из блока with.
        """
        self.conn.close()


# Использование менеджера контекста:
# Host=localhost;Username=postgres;Password=postgres;Database=Library
dsn = 'dbname=Library user=postgres password=postgres host=localhost'
with PostgresConnection(dsn) as conn:
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM books;""")
    for row in cursor.fetchall():
        print(row)
