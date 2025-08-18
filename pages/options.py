from dash import html, register_page

register_page(__name__, path='/options')

layout = html.Div(
    children=[
        html.H2('Option page'),
        html.P('Here will be displayed the options')
    ]
)
