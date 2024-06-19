from datetime import date, datetime
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
import re
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots
plt.style.use('seaborn')

colors = {
    'background': '#2f323a',
    'text': '#ffffff'
}

# Define LAYOUT
sandra = html.Div(id= "sandra_map",style={'backgroundColor': colors['background']},children=[
    html.H2(
        children='Taxicab Requests Prediction',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    html.Div(style={'color': colors['text']}, children='''
    This module shows the number of requests predicted for a particular day and hour. It uses a time series forecasting model called Prophet, which is developed by Facebook.
    '''),
    html.H3(
        children='Select the day to forecast.',
        style={
            'textAlign': 'left',
            'color': colors['text']
        }
    ),
    html.Div(
        [
            html.Div(style={'color': colors['text']}, children=
            [
                dcc.DatePickerSingle(
                                    id='my-date-picker',
                                    min_date_allowed=date(2020, 8, 17),
                                    max_date_allowed=date(2021, 2, 6),
                                    initial_visible_month=date(2020, 8, 17),
                                    date=date(2020, 8, 17)
                ),
                html.Div(id='output-container-date-picker')
            ]),
            html.Div([
        dcc.Graph( id='forecast' )]),
        html.Div(style={'color': colors['text']}, children= [html.H3("No. of Requests predicted:"), html.H3(id='rq_text')], id="rq", className="mini_container",),])        
])