from dash import html, callback, Input, Output, State, dcc
import dash_bootstrap_components as dbc


from components import text_area, text_block, radio_items, ids
from components.texts.loader import CATEGORIES, SCORES, TEXTS


def create_card(category: str, text: dict[str, str]) -> dbc.Card:
    return dbc.Card(
        [
            dbc.CardHeader(html.H3(f"{category}. {text['título']}"),),
            dbc.CardBody(
                [
                    text_block.render(text),
                    radio_items.render(),
                    text_area.render(),
                ],
            ),
        ],
    )


CARDS: list[dbc.Card] = [
    create_card(category, text) for category, text in TEXTS.items()
]


def render() -> dbc.Tab:
    return dbc.Tab(
        label='Formulário',
        children=[
            html.Div(CARDS[0], id=ids.CARD),
            dbc.Pagination(
                id=ids.PAGINATION,
                max_value=len(CATEGORIES),
                active_page=1,
            ),
            dcc.Store(
                id=ids.STORE_RADIO_ITEMS,
                data=[float(SCORES[0])]*len(CATEGORIES)
            ),
            dcc.Store(
                id=ids.OBS_STORE,
                data=['']*len(CATEGORIES)
            ),
        ],
        tab_id=ids.FORM,
    )


@callback(
    [
        Output(ids.CARD, 'children'),
        Output(ids.RADIO_ITEMS, 'value'),
        Output(ids.OBSERVATIONS, 'value'),
    ],
    Input(ids.PAGINATION, 'active_page'),
    [
        State(ids.STORE_RADIO_ITEMS, 'data'),
        State(ids.OBS_STORE, 'data'),
    ],
    prevent_initial_call=True,
)
def change_page(
    page: int,
    scores: list[float],
    observations: list[str]
) -> tuple[dbc.Card, float, str]:
    return CARDS[page - 1], scores[page - 1], observations[page - 1]
