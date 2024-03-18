from pathlib import Path
from sqlite3 import Cursor
import sqlite3

from data.database import DATA_PATH, DB_FILE, connect_to_database


PATIENT_TABLE: Path = DATA_PATH / 'sql' / 'create_patient_table.sql'
CARS_TABLE: Path = DATA_PATH / 'sql' / 'create_cars_table.sql'


def create_tables() -> None:
    def create(cursor: Cursor) -> Cursor:
        cursor.execute(PATIENT_TABLE.read_text())
        cursor.execute(CARS_TABLE.read_text())
        return cursor

    connect_to_database(create)


def get_number_of_patients() -> int:
    with sqlite3.connect(DB_FILE) as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT COUNT(*) FROM patients')
        return cursor.fetchone()[0]
