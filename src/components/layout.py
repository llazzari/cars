from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

from components import (
    ids,
    tabs,
    save_data_button,
    alert_save,
    load_data_button,
    patient_info
)


def render(app: Dash) -> dbc.Container:
    return dbc.Container(
        children=[
            dcc.Download(id=ids.DOWNLOAD_DATA),
            html.H1(app.title),
            html.Hr(),
            patient_info.render(),
            alert_save.render(),
            dbc.Row(
                [
                    dbc.Col(load_data_button.render(app), width='auto'),
                    dbc.Col(save_data_button.render(app), width='auto')
                ],
                justify='end',
            ),
            tabs.render(app),
        ],
        className="dbc"
    )
