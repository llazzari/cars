from dash import Dash, Input, Output, html
import dash_mantine_components as dmc
from dash_iconify import DashIconify
import datetime

from components import ids
from data.patient import get_patient_birthdate, get_patient_names
from data import cars


Entries = tuple[str, str, str, list[float], list[str], int]


def render(app: Dash) -> html.Div:
    @app.callback(
        Output(ids.NAME, 'value'),
        Output(ids.BIRTHDATE, 'value'),
        Output(ids.DATE, 'value'),
        Output(ids.STORE_RADIO_ITEMS, 'data', allow_duplicate=True),
        Output(ids.OBS_STORE, 'data', allow_duplicate=True),
        Output(ids.PAGINATION, 'active_page'),
        Input(ids.SELECT_PATIENT, 'value'),
        prevent_initial_call=True,
    )
    def upload(patient_name: str) -> Entries:
        try:
            birthdate: str = get_patient_birthdate(patient_name)
        except TypeError:
            birthdate: str = str(datetime.date.today())
        patient_data: dict[str, str] = {
            'name': patient_name,
            'birthdate': birthdate
        }
        try:
            scores, observations, date = cars.get_scores_and_observations(
                patient_data
            )
        except TypeError:
            scores: list[float] = [1.]*15
            observations: list[str] = ['']*15
            date: str = str(datetime.date.today())

        return (patient_name, birthdate, date, scores, observations, 1)
    return html.Div(
        dmc.Select(
            placeholder='Selecionar paciente para carregar os dados',
            data=get_patient_names(),
            id=ids.SELECT_PATIENT,
            searchable=True,
            nothingFound='Nenhum paciente encontrado.',
            icon=DashIconify(
                icon="radix-icons:magnifying-glass",
                color='var(--bs-info)'
            ),
            rightSection=DashIconify(icon="radix-icons:chevron-down"),
            clearable=True,
            className='load-and-save',
        ),
    )
