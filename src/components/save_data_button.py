from dash import Dash, Input, Output, State, no_update
import dash_mantine_components as dmc
from typing import Any

from components import ids
from data import cars
from data.patient import get_patient_names


def render(app: Dash) -> dmc.Button:
    @app.callback(
        Output(ids.ALERT_SAVE, 'hide'),
        Output(ids.ALERT_SAVE, 'children'),
        Output(ids.SELECT_PATIENT, 'data'),
        Input(ids.SAVE_BUTTON, 'n_clicks'),
        [
            State(ids.NAME, 'value'),
            State(ids.BIRTHDATE, 'value'),
            State(ids.DATE, 'value'),
            State(ids.STORE_RADIO_ITEMS, 'data'),
            State(ids.OBS_STORE, 'data'),
        ],
        prevent_initial_call=True,
    )
    def on_click(
        _,
        name: str,
        birthdate: str,
        date: str,
        scores: list[float],
        observations: list[str]
    ) -> tuple[bool, str, Any]:
        if not name:
            return False, 'Preencha o nome.', no_update

        patient_data: dict[str, str] = {'name': name, 'birthdate': birthdate}
        cars.insert_scores(patient_data, date, scores, observations)

        return False, 'Os dados foram salvos com sucesso!', get_patient_names()
    return dmc.Button(
        'Salvar',
        id=ids.SAVE_BUTTON,
        radius='xl',
        variant='outline',
        className='load-and-save',
    )
