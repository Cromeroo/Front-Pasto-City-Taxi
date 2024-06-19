import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from app import app
from lib import header, sidebar, main

layout = html.Div(
[ 
    html.Header(
       [
           header.bar_head
       ]),
    html.Div(className="sidebar", children=
        [
           sidebar.lateral_bar
        ]),
    html.Div( className="content", children=
        [
            main.content
        ]),
])