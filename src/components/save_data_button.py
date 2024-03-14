from pathlib import Path
from dash import Dash, Input, Output, State, dcc
import dash_bootstrap_components as dbc
import pandas as pd

from components import ids


def render(app: Dash) -> dbc.Button:
    @app.callback(
        Output(ids.DOWNLOAD_DATA, 'data'),
        Input(ids.SAVE_BUTTON, 'n_clicks'),
        [
            State(ids.NAME, 'value'),
            State(ids.AGE, 'value'),
            State(ids.BIRTHDATE, 'value'),
            State(ids.DATE, 'value'),
            State(ids.STORE_RADIO_ITEMS, 'data'),
            State(ids.OBS_STORE, 'data'),
        ],
        prevent_initial_call=True
    )
    def on_click(
        _,
        name: str,
        age: str,
        birthdate: str,
        date: str,
        scores: list[float],
        observations: list[str],
    ):
        df = pd.DataFrame(
            {
                'Nome': name,
                'Data de nascimento': birthdate,
                'Data de avaliação': date,
                'Score': scores,
                'Observações': observations,
            },
        )
        file_path: Path = Path.cwd() / 'src' / 'data' / f'{name}_{age}.csv'
        return dcc.send_data_frame(df.to_csv, file_path, index=False)
    return dbc.Button(
        'Salvar',
        id=ids.SAVE_BUTTON,
        class_name='me-1',
        style={'margin-right': '10px'},
        color='info'
    )
