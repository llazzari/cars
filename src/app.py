import dash_bootstrap_components as dbc
from dash import Dash

from components import layout
from data.tables import create_tables
from data.patient import insert_patient


dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"

app = Dash(
    __name__,
    external_stylesheets=[
        dbc_css,
        dbc.themes.MORPH,
    ],
)
app.title = 'Childhood Autism Rating Scale (CARS)'
create_tables()
insert_patient({'name': 'João', 'birthdate': '01/01/2020'})
insert_patient({'name': 'Maria', 'birthdate': '02/02/2020'})
insert_patient({'name': 'Josefina', 'birthdate': '03/03/2020'})
app.layout = layout.render(app)
app.scripts.config.serve_locally = True
server = app.server


if __name__ == '__main__':
    app.run(debug=True, port='8050')
