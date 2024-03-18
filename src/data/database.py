import sqlite3
from sqlite3 import Cursor
from typing import Callable
from pathlib import Path

DATA_PATH = Path.cwd() / 'src' / 'data'
DB_FILE: Path = DATA_PATH / 'patients.db'


def connect_to_database(act_on_database: Callable[[Cursor], Cursor]) -> None:
    "Helper function to open and close a connection to the database."
    with sqlite3.connect(DB_FILE) as connection:
        cursor = connection.cursor()
        cursor = act_on_database(cursor)
        connection.commit()
