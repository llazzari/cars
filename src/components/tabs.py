from dash import Dash
import dash_bootstrap_components as dbc

from components import ids, form_tab, results_tab


def render(app: Dash) -> dbc.Tabs:
    return dbc.Tabs(
        [
            form_tab.render(),
            results_tab.render(app)
        ],
        id=ids.TABS,
        active_tab=ids.FORM,
        style={'margin-bottom': '10px'}
    )
