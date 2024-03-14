from dash import html


def render() -> html.Div:
    return html.Div([
        html.H4('Resultados:', style={'margin-top': '10px'}),
        html.Div('15-30: sem autismo'),
        html.Div('30-36: autismo leve-moderado'),
        html.Div('36:60: autismo grave')
    ])
