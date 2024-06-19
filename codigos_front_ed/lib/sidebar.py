import pathlib
import os
import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html

from app import app

lateral_bar = html.Div( children=
[   
    html.Div(className="profile_info", children=
        [
            html.Img(src="../assets/logo.png", className="profile_image", alt=""),
            html.H4(["MENU"]),
        ]),
    html.A(href="/", children=[html.I(className="fas fa-desktop"),html.Span(["Dashboard"])]),
    html.A(href="/", children=[html.I(className="fas fa-cogs"), html.Span(["Geomap"])]),
    html.A(href="/", children=[html.I(className="fas fa-table"),html.Span(["Heatmap"])]),
    html.A(href="/", children=[html.I(className="fas fa-info-circle"),html.Span(["About"])]),

])