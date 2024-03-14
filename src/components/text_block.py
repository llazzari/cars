from dash import html

from components.texts.loader import ANSWERS


def create_text_block(text: str) -> html.P:
    return html.P(
        text,
        # style={
        #     'padding-bottom': '10px',
        #     'width': '90%',
        #     'text-align': 'justify',
        #     'margin-left': '10px',
        #     'font-size': '18px'
        # }
    )


def render(data: dict[str, str]) -> html.Div:
    return html.Div([create_text_block(data[i]) for i in ANSWERS])
