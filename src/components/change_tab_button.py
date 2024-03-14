from dash import Dash, Input, Output, State
import dash_bootstrap_components as dbc

from components import ids


def render(app: Dash) -> dbc.Button:
    @app.callback(
        Output(ids.TABS, 'active_tab'),
        Input(ids.TAB_BUTTON, 'n_clicks'),
        State(ids.TABS, 'active_tab'),
        prevent_initial_call=True
    )
    def on_click(n: int | None, at: str) -> str:
        if at == ids.FORM:
            return ids.RESULTS
        return ids.FORM
    return dbc.Button(
        'Trocar aba',
        id=ids.TAB_BUTTON,
        class_name='buttons',
        style={'margin-right': '10px'},
        color='link'
    )
