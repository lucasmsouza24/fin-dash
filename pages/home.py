from dash import html, register_page

register_page(__name__, path="/")

layout = html.Div(
    children=[
        html.H2("Financial Dashboard - Home"),
        html.P("Here, graphs will be displayed."),
    ]
)
