import sqlite3

class Database:
    def __init__(self):
        self.connection = sqlite3.connect("../../data/data.db")

    def execute(self, query: str, params: tuple = ()):
        with self.connection:
            self.connection.execute(query, params)

    def fetch_one(self, query: str, params: tuple = ()):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(query, params)

            return cursor.fetchone()

    def fetch_all(self, query: str, params: tuple = ()):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(query, params)

            return cursor.fetchall()

    def fetch_many(self, query: str, size: int, params: tuple = ()):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(query, params)

            return cursor.fetchmany(size)