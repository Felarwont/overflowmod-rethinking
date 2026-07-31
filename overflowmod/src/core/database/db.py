import sqlite3
from pathlib import Path
from typing import Any

from .models import GameBaseModel

data_path = Path(__file__).resolve().parents[4] / "overflowmod" / "data" / "data.db"

class Database:
    def __init__(self):
        self.connection = sqlite3.connect(data_path)
    
    def create_table(self, table: type[GameBaseModel]):
        with self.connection:
            self.connection.execute(table.create_query())

    def execute(self, query: str, params: tuple = ()) -> int:
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(query, params)

            return cursor.rowcount

    def fetch_one(self, query: str, params: tuple = ()) -> tuple[Any]:
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(query, params)

            return cursor.fetchone()

    def fetch_all(self, query: str, params: tuple = ()) -> list[tuple]:
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(query, params)

            return cursor.fetchall()

    def fetch_many(self, query: str, size: int, params: tuple = ()) -> list[tuple]:
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(query, params)

            return cursor.fetchmany(size)

    def close(self) -> None:
        self.connection.close()