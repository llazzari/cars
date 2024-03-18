import json
import sqlite3

from data.database import DATA_PATH, DB_FILE
from data.patient import GET_PATIENT_ID, INSERT_PATIENT

INSERT_SCORES = DATA_PATH / 'sql' / 'insert_cars_scores.sql'
UPDATE_SCORES = DATA_PATH / 'sql' / 'update_cars_scores.sql'


def insert_scores(
    patient_data: dict[str, str],
    date: str,
    scores: list[float],
    observations: list[str]
) -> None:
    total_score: float = round(sum(scores), 1)
    json_scores = json.dumps(scores)

    with sqlite3.connect(DB_FILE) as connection:
        cursor = connection.cursor()

        cursor.execute(INSERT_PATIENT.read_text(), patient_data)
        cursor.execute(GET_PATIENT_ID.read_text(), patient_data)
        patient_id: int = cursor.fetchone()[0]

        select_score_sql = """
          SELECT id FROM cars_scores
          WHERE patient_id = ? AND date = ?
        """
        cursor.execute(select_score_sql, (patient_id, date))
        row = cursor.fetchone()
        test_score_id = row[0] if row else None

        if not test_score_id:
            cursor.execute(
                INSERT_SCORES.read_text(),
                (
                    patient_id,
                    date,
                    json_scores,
                    total_score,
                    json.dumps(observations)
                )
            )
        else:
            cursor.execute(
                UPDATE_SCORES.read_text(),
                (
                    json_scores,
                    total_score,
                    json.dumps(observations),
                    patient_id,
                    date
                )
            )
        connection.commit()


def get_scores_and_observations(
    patient_data: dict[str, str],
) -> tuple[list[float], list[str], str]:
    with sqlite3.connect(DB_FILE) as connection:
        cursor = connection.cursor()
        cursor.execute(GET_PATIENT_ID.read_text(), patient_data)
        patient_id: int = cursor.fetchone()[0]

        cursor.execute(
            'SELECT scores FROM cars_scores WHERE patient_id = ?',
            (patient_id,),
        )
        scores = json.loads(cursor.fetchone()[0])

        cursor.execute(
            'SELECT observations FROM cars_scores WHERE patient_id = ?',
            (patient_id,),
        )
        observations: list[str] = json.loads(cursor.fetchone()[0])

        cursor.execute(
            'SELECT date FROM cars_scores WHERE patient_id = ?',
            (patient_id,),
        )
        date: str = cursor.fetchone()[0]

    return scores, observations, date
