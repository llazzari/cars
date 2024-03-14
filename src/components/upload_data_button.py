import base64
import io
from dash import Dash, Input, Output, dcc
import dash_bootstrap_components as dbc
import pandas as pd

from components import ids


def process_data(decoded: bytes) -> pd.DataFrame:
    df = pd.read_csv(
        io.StringIO(decoded.decode('utf-8')),
        parse_dates=True,
        date_format='%Y-%m-%d',
        dtype={
            'Nome': str,
            'Data de nascimento': str,
            'Data de avaliação': str,
            'Idade': int,
            'Scores': float,
            'Observações': str,
        },
    )
    df.fillna('Observações', inplace=True)

    return df


PacientInfo = tuple[str, str, str, int, list[float], list[str], int]


def render(app: Dash) -> dcc.Upload:
    @app.callback(
        [
            Output(ids.NAME, 'value'),
            Output(ids.BIRTHDATE, 'value'),
            Output(ids.DATE, 'value'),
            Output(ids.AGE, 'value'),
            Output(ids.STORE_RADIO_ITEMS, 'data', allow_duplicate=True),
            Output(ids.OBS_STORE, 'data', allow_duplicate=True),
            Output(ids.PAGINATION, 'active_page'),
        ],
        Input(ids.UPLOAD_DATA, 'contents'),
        prevent_initial_call=True,
    )
    def upload(contents: str) -> PacientInfo:
        _, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)

        df: pd.DataFrame = process_data(decoded)

        return (
            df['Nome'].iloc[0],
            df['Data de nascimento'].iloc[0],
            df['Data de avaliação'].iloc[0],
            df['Idade'].iloc[0],
            df['Score'].to_list(),
            df['Observações'].to_list(),
            1
        )
    return dcc.Upload(
        dbc.Button(
            'Upload',
            id=ids.UPLOAD_BUTTON,
            color='info',
            outline=True,
            className='me-1'
        ),
        id=ids.UPLOAD_DATA,
        className='buttons',
        style={'margin-bottom': '10px'}
    )
