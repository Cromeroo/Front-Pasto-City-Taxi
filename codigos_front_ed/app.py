import dash
import dash_bootstrap_components as dbc

app = dash.Dash(
    __name__, external_stylesheets=[
        {'rel':'stylesheet', 'href':'style_snow.css'},
        {'rel':'stylesheet',' href':'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.12.1/css/all.min.css'}],
    meta_tags=[
            { 
            'charset':'utf-8',
            'name': 'viewport',
            'content': 'width=device-width, initial-scale=1.0'
            }
        ],
    external_scripts=['https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.1/jquery.min.js',],
    )

app.title = 'TaxisRCP'
server = app.server

# We need this for function callbacks not present in the app.layout
app.config.suppress_callback_exceptions = True