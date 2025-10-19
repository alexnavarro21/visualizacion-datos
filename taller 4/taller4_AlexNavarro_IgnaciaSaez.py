# Importar librerías necesarias
import pandas as pd
import plotly.express as px
import warnings
warnings.filterwarnings('ignore')
from dash import Dash, html, dcc, dash_table
from jupyter_dash import JupyterDash

# Cargar datos desde CSV
df = pd.read_csv('world_happiness_combined.csv')
list(df.columns)


# Crear tabla de datos
table = dash_table.DataTable(
    data=df.to_dict('records'),
    page_size=10
    )

# ¿Cómo varía el puntaje de felicidad por país en el año seleccionado?

# Crear gráfico con Plotly
fig = px.bar(df,
    x='Country',
    y='Happiness Rank',
    color='Region',
    title='Datos por Categoría'
    )

app = JupyterDash()

# Layout con tabla y gráfico
app.layout = html.Div([
    html.H1('Dashboard de Datos'),
    html.H2('Tabla de Datos'),
    table,
    html.H2('Gráfico Interactivo'),
    dcc.Graph(figure=fig)
    ],
    style={'font-family': 'Arial' }
    )

app.run(jupyter_mode='external')