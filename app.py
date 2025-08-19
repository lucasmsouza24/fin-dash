from dash import Dash, html, page_container
from components.header import Header

app = Dash(__name__, use_pages=True)
app.title = 'Financial Dashboard'
server = app.server

app.layout = html.Div(
    children=[
        Header(),
        page_container
    ]
)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8050', debug=True)
