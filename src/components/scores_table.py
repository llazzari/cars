from dash import dash_table, Dash, Input, Output, html
import pandas as pd

from components import ids
from components.texts.loader import CATEGORIES


def render(app: Dash) -> html.Div:
    @app.callback(
        Output(ids.SCORE_TABLE, 'data'),
        Input(ids.STORE_RADIO_ITEMS, 'data'),
    )
    def update(scores: list[float]) -> list[dict]:
        table_data = pd.DataFrame(
            {cat: float(score) for cat, score in zip(CATEGORIES, scores)},
            index=[0],
        )
        table_data['Total'] = sum(scores)
        return table_data.to_dict('records')
    return html.Div(
        dash_table.DataTable(
            id=ids.SCORE_TABLE,
            style_as_list_view=True,
            style_header={
                # 'backgroundColor': 'var(--bs-info)',
                'fontWeight': 'bold',
            },
            style_cell_conditional=[
                {
                    'if': {'column_id': 'Total'},
                    'width': '60px',
                },
            ],
            style_data={
                'width': '30px',
                'maxWidth': '30px',
                'minWidth': '30px',
            },
        )
    )
