from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

from components import (
    pacient_info,
    ids,
    tabs,
    upload_data_button,
    save_data_button
)


def render(app: Dash) -> dbc.Container:
    return dbc.Container(
        children=[
            dcc.Download(id=ids.DOWNLOAD_DATA),
            html.H1(app.title),
            html.Hr(),
            pacient_info.render(),
            dbc.Row(
                [
                    dbc.Col(upload_data_button.render(app), width='auto'),
                    dbc.Col(save_data_button.render(app), width='auto')
                ],
                justify='end'
            ),
            tabs.render(app),
        ],
        # style={'margin': '10px'},
        className="dbc"
    )
