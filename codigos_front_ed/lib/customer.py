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
# import pickle
plt.style.use('seaborn')

# ------------------------------------------------------------------------------------------------------
filename = 'data/DistributionCustomers.html'
metric_list = ['N requests', 'Avg monthly requests', 'Frequency: Avg quarterly rq',
               'Recency', 'Months seniority']


custom = html.Div( className="customer" , children=
[
    html.Section( id="cus", children=
        [
            html.H2( children=["Know Your Customer"], style={ 'textAlign': 'center'}),
            html.Div( children=['''This module shows a client segmentation based on customer activity's freshness (Time since last activity) and the customers' total number of requests.
    ''']),
            html.Div( id="cus-con" , children=
                [
                    html.Div( id="figura1", children=[html.Iframe(id='fig', srcDoc=open(filename,'r').read(),width='900vh', height = '500px')]),
                    html.Div( id="textmark", children=[dcc.Markdown('''
                        #### Identify a segment of customers:
                        
                        - **One-time:** *50%* are one-time service customer.
                        - **Who are their best customers?** *4%* are Premium: Recently have requested a service, and they are the most often customers.
                        *5%* of your customers are Loyal. 
                        - **Who has the potential to become valuable customers? *3%* are Potential Loyalist, they are recent customers with average frequency.
                        - **New Customers** Start building relationships with these customers by providing onboarding support. *4%* are new customers.
                        - **At-Risk Customers** *3%* of your customers are at risk to churn. They request a service often but have not required a service recently.
                        - **Can't Lose Them** They are similar to Premium customers but haven't been requesting a service recently. *7%* of your customers are in this segment.
                        - **Need Attention** *5%* of your customers you need incentivizing to use your service.
                        - **Hibernating**: *20%* of your customers contribute to your churn rate.\n
                        **You can graph some metrics to see the differences in each segment.**

                        ''')], 
                        style={'text-align':'justify'}),
   
        ]),
                ]),
            
        html.Div( id="menu" , children=
            [
                html.H4('Select Metric', style={'text-align':'justify'}),
                dcc.Dropdown( id='co-select', options= [ {'label': str(metric), 'value': metric } for metric in metric_list], value= 'N requests' ),
                ]),
    html.Section(id="graficas" , children=
        [

            html.Div([ dcc.Graph( id='metricG1')]),
            html.Div([ dcc.Graph( id='metricG2')]),
         ]),
])