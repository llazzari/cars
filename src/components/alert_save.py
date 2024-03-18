from dash import html
import dash_mantine_components as dmc
from dash_iconify import DashIconify

from components import ids


def render() -> html.Div:
    return html.Div(
        dmc.Alert(
            id=ids.ALERT_SAVE,
            variant='outlined',
            duration=3000,
            hide=True,
            radius='xl',
            className='alert',
            icon=DashIconify(
                icon='mdi:alert-circle-outline',
                width=20,
                color='var(--bs-info)'
            ),
        ),
    )
