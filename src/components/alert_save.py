from dash import html
import dash_mantine_components as dmc

from components import ids


def render() -> html.Div:
    return html.Div(
        dmc.Alert(
            id=ids.ALERT_SAVE,
            color="violet",
            variant='filled',
            duration=3000,
            hide=True,
        ),
    )
