from dash import dcc, html, Output, Input, State, callback

from components import ids


def render() -> html.Div:
    return html.Div(
        dcc.Textarea(
            id=ids.OBSERVATIONS,
            placeholder='Observações',
            style={'width': '80%', 'height': 80, 'margin-left': '10px'},
        ),
    )


@callback(
    Output(ids.OBS_STORE, 'data'),
    Input(ids.OBSERVATIONS, 'value'),
    [
        State(ids.OBS_STORE, 'data'),
        State(ids.PAGINATION, 'active_page'),
    ],
    prevent_initial_call=True
)
def store(
    observation: str,
    observations: list[str],
    page: int,
) -> list[str]:
    observations[page - 1] = observation
    return observations
