from datetime import date
import dash_mantine_components as dmc
from dash_iconify import DashIconify

from components import ids


def render() -> dmc.Card:
    today = date.today()
    return dmc.Card(
        dmc.Grid(
            [
                dmc.Col(
                    dmc.TextInput(
                        id=ids.NAME,
                        label='Nome',
                        placeholder='Digite o nome do paciente',
                        radius='xl',
                        required=True,
                        type='text',
                    ),
                    span=4,
                ),
                dmc.Col(
                    dmc.DatePicker(
                        id=ids.BIRTHDATE,
                        label='Data de nascimento',
                        icon=DashIconify(
                            icon='material-symbols-light:edit-calendar-outline',
                            width=20,
                        ),
                        minDate=date(2012, 12, 12),
                        value=today,
                        inputFormat='DD/MM/YYYY',
                        maxDate=today,
                        clearable=False,
                        required=True,
                        radius='xl',
                        dropdownPosition='bottom-start',
                        dropdownType='modal',
                    ),
                    span='auto',
                ),
                dmc.Col(
                    dmc.DatePicker(
                        id=ids.DATE,
                        label='Data da avaliação',
                        icon=DashIconify(
                            icon='material-symbols-light:edit-calendar-outline',
                            width=20,
                        ),
                        minDate=date(2024, 1, 1),
                        value=today,
                        inputFormat='DD/MM/YYYY',
                        maxDate=today,
                        clearable=False,
                        required=True,
                        radius='xl',
                        dropdownPosition='bottom-start',
                        dropdownType='modal',
                    ),
                    span='auto',
                ),
                # dmc.Col(
                #     dmc.TextInput(
                #         label='Idade',
                #         radius='xl',
                #         required=True,
                #         placeholder='Idade do paciente',
                #         id=ids.AGE,
                #         type='number',
                #     ),
                #     span='auto',
                # ),
            ],
            grow=True,
            gutter='xl',
        ),
        style={
            'margin-bottom': '10px',
            'background-color': 'var(--bs-secondary)'
        },
    )
