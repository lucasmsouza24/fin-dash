from dash import html

def KpiCard(title, value, prefix='R$', decimals=2, color=None):
    return html.Div(
        className='kpi-card',
        style={'backgroundColor': color} if color else {},
        children=[
            html.P(title, className='kpi-title'),
            html.H3(f'{prefix} {value:,.{decimals}f}', className='kpi-value')
        ]
    )
