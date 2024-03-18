from sqlite3 import Cursor
import sqlite3

from data.database import DB_FILE, connect_to_database, DATA_PATH

INSERT_PATIENT = DATA_PATH / 'sql' / 'insert_patient.sql'
REMOVE_PATIENT = DATA_PATH / 'sql' / 'delete_patient.sql'
GET_PATIENT_ID = DATA_PATH / 'sql' / 'get_patient_id.sql'


def insert_patient(patient_data: dict[str, str]) -> None:
    def insert(cursor: Cursor) -> Cursor:
        cursor.execute(INSERT_PATIENT.read_text(), patient_data)
        print(f'rowcount = {cursor.rowcount}')
        return cursor

    connect_to_database(insert)


def remove_patient(patient_data: dict[str, str]) -> None:
    def remove(cursor: Cursor) -> Cursor:
        return cursor.execute(REMOVE_PATIENT.read_text(), patient_data)

    connect_to_database(remove)


def get_patient_names() -> list[str]:
    with sqlite3.connect(DB_FILE) as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT name FROM patients')
        return [name[0] for name in cursor.fetchall()]


def get_patient_birthdate(name: str) -> str:
    with sqlite3.connect(DB_FILE) as connection:
        cursor = connection.cursor()
        cursor.execute(
            'SELECT birthdate FROM patients WHERE name = ?',
            (name,)
        )
        return cursor.fetchone()[0]
