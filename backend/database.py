import psycopg2
from settings import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT

class DB():
    def __init__(self):
        # establishing the connection
        self._conn = psycopg2.connect(
        database="ods",
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        self._cursor = self._conn.cursor()

    def __del__(self):
        self._conn.close()

    def read(self, sql: str, data: tuple = None) -> list:
        # trail of queers
        self._cursor.execute(sql, data)
        return self._cursor.fetchall()

    def write(self, sql: str, data: tuple or list = None) -> None:
        if data is None:
            self._cursor.execute(sql)
        elif isinstance(data, tuple):
            self._cursor.execute(sql, data)
        elif isinstance(data, list):
            self._cursor.executemany(sql, data)

        self._conn.commit()
