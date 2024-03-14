from dash import Dash, html
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc

from components import (
    bar_chart,
    outcomes,
    radar_chart,
    scores_table,
    ids
)


def render(app: Dash) -> dbc.Tab:
    return dbc.Tab(
        label='Resultados',
        children=[
            dmc.Card(
                [
                    scores_table.render(app),
                    outcomes.render(),
                ],
                shadow='sm',
                radius='xl',
                style={'background-color': 'var(--bs-secondary)'}
            ),
            html.Div(
                [
                    bar_chart.render(app),
                    radar_chart.render(app)
                ],
                className="row"
            ),
        ],
        tab_id=ids.RESULTS
    )
