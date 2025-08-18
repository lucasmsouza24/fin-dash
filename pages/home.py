from dash import html, dcc, register_page, Output, Input, callback
import pandas as pd
import plotly.express as px

register_page(__name__, path="/")

df = pd.read_csv('./data/data.csv')

layout = html.Div(
    children=[
        html.H2("Financial Dashboard - Home"),
        html.P("Here, graphs will be displayed."),
        dcc.Graph(
            id='id-example-graph',
            figure={}
        )
    ]
)

# callbacks
@callback(
    Output('id-example-graph', 'figure'),
    Input('period-filter', 'value')
)
def update_example_graph(_):
    return px.bar(df, x='month', y='revenue')
