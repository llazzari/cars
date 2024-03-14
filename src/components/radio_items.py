from dash import html, callback, Output, Input, State
import dash_bootstrap_components as dbc

from components.texts.loader import SCORES
from components import ids


def render() -> html.Div:
    return html.Div(
        dbc.RadioItems(
            options=[
                {'label': score, 'value': round(float(score), 1)}
                for score in SCORES
            ],
            value=int(SCORES[0]),
            # id=f'ri_{category}',
            id=ids.RADIO_ITEMS,
            inline=True,
            style={'margin-bottom': '10px'}
        ),
    )


@callback(
    Output(ids.STORE_RADIO_ITEMS, 'data'),
    Input(ids.RADIO_ITEMS, 'value'),
    [
        State(ids.PAGINATION, 'active_page'),
        State(ids.STORE_RADIO_ITEMS, 'data'),
    ],
    prevent_initial_call=True,
)
def store(radio_value: float, page: int, data: list[float]) -> list[float]:
    data[page - 1] = radio_value
    return data
