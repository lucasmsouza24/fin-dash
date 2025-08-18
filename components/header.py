from dash import html, dcc

def Header():
    return html.Div(
        className='header',
        children=[
            # Title container
            html.Div(
                html.H1('Financial Dashboard'),
                className='header-title'
            ),

            # Dropdown and navigation container
            html.Div(
                children=[
                    html.Nav([
                        dcc.Link('Home', href='/'),
                        dcc.Link('Options', href='/options')
                    ], className='header-nav'),
                    dcc.Dropdown(
                        id='period-filter',
                        options=[
                            {'label': 'Last 30 days', 'value': '30d'},
                            {'label': 'Last 6 months', 'value': '6m'},
                            {'label': 'Last year', 'value': '1y'},
                        ],
                        value='30d',
                        clearable=False,
                        className='header-dropdown'
                    )
                ],
                className='header-right'
            )
        ]
    )
