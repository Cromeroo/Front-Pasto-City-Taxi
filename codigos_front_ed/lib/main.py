import pathlib
import os
import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html

from app import app
from lib import sandra_app, customer
content = html.Div( children=
[   
    html.Section( className="mid-content", children=
        [
            html.Div( className="secciones", children=
                [
                    sandra_app.sandra
                ]),
            html.Div( id= "mid-area", children=
                [
                    html.Div(className="sub", id="geomap", children=
                        [
                            
                            html.Div( className="text", children=
                               [
                                   html.H2(["Where do people request a Taxicab in Pasto?"]),
                                   html.P(["With this map, we can identify places with the most demand; this will allow us to manage the taxi's availability to supply demand in particular areas."]),
                               ]),
                            html.Iframe(id='map', srcDoc=open('data/mpasto.html','r').read()),

                       ]),
                    html.Div(className="sub", id="forecas" ,children=
                        [
                           
                            html.Div( className="text", children=
                               [                           
                                   html.H2(["Time Series Forecasting"]),
                                   html.P(["We use Prophet, an open-source time-series forecasting library made available by Facebook.  The graph shows the historical and predicted values; we also include holidays to realize the forecast."]),
                                   html.Iframe(id='model_HDS', srcDoc=open('data/model_HDS.html','r').read()),
                               ]),
                        ]),
                ]),
            html.Div( id='customer', children=
                [
                   customer.custom
                ]),

        ]),

    dbc.Navbar(className="barrapu", children=
       [
           html.Ul( id="ds4alogo", children=
               [
                   html.Li(html.Img(src="../assets/ds4a-img.svg",style={'height' : '100%', 'width' : '100%',}),),
               ]), 
       ]),
])