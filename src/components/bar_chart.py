from dash import html, Dash, Input, Output, dcc
import plotly.express as px
import pandas as pd

from components import ids
from components.texts.loader import TITLES


def render(app: Dash) -> html.Div:

    @app.callback(
        Output(ids.BAR_CHART, 'figure'),
        Input(ids.STORE_RADIO_ITEMS, 'data'),
    )
    def update(scores: list[float]):
        df = pd.DataFrame({'Escore': scores, 'Títulos': TITLES})
        fig = px.bar(
            df, y='Títulos', x='Escore',
            range_x=[0, 4],
            color='Títulos',
            # orientation='h'
        )
        fig.update_layout(showlegend=False)
        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            # font_color='white'
        )
        return fig

    return html.Div(
        dcc.Graph(id=ids.BAR_CHART),
        style={'margin-top': '10px', 'width': '50%'},
        className='charts'
    )
