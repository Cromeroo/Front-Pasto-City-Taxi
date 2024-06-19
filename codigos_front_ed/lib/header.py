import pathlib
import os
import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html

from app import app

bar_head = html.Div( children=
[   
           html.Div(className="left_area", children=
               [
                   html.H3(["TAXIS", html.Span(["RCP"] ) ]),
               ]),
           html.Div(className="right_area", children=
               [
                   html.A(className="facebook_btn", href="https://www.facebook.com/taxisrcp/", children=
                       [
                           html.Img(src="../assets/images/fb_black.jpg",style={'height' : '40px', 'width' : '40px',})
                       ]),
               ]),
          
])


#     html.Label( htmlFor="check", children=
#               [
#                   html.I(className="fas fa-bars", id="sidebar_btn", children=[]),
#               ]),
           