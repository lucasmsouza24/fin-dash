from dash import html, register_page, Output, Input, callback
import pandas as pd
import plotly.express as px
from components.kpi_card import KpiCard

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
    total_revenue = df.revenue.sum()
    total_expense = df.expense.sum()
    total_profit = df.profit.sum()

    revenue = KpiCard('Revenue', total_revenue, color="#d4edda")
    expense = KpiCard('Expense', total_expense, color="#f8d7da")
    profit = KpiCard('Profit', total_profit, color="#d1ecf1")

    return [revenue, expense, profit]
