from dash import html, register_page, Output, Input, callback
import pandas as pd
import plotly.express as px
from components.kpi_card import KpiCard
from services.home import calculate_kpis

register_page(__name__, path="/")

df = pd.read_csv('./data/data.csv')

layout = html.Div(
    children=[
        html.H2("Financial Dashboard - Home"),
        html.Div(
            id='id-kpi-container',
            className='kpi-card-container',
            children=[]
        )
    ]
)

# callbacks
@callback(
    Output('id-kpi-container', 'children'),
    Input('period-filter', 'value')
)
def update_example_graph(_):
    kpis = calculate_kpis(df)
    return [
        KpiCard('Revenue', kpis['revenue'], color="#d4edda"),
        KpiCard('Expense', kpis['expense'], color="#f8d7da"),
        KpiCard('Profit', kpis['profit'], color="#d1ecf1")
    ]
