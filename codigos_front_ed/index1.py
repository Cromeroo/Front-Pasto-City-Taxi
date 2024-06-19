from datetime import date, datetime
import pandas as pd
import dash
import re
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots
plt.style.use('seaborn')



#------------------------------------
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from apps import home
import gc
gc.collect()



###########################################################################################

# Get data. Functions.
def get_forecastH(path):
    df = pd.read_csv(path)
    return df

def get_forecastD(path):
    df = pd.read_csv(path)
    return df
    
def date_time(df, column):
    
    """
    Creates time series features from datetime index.
    """
    df[column] = pd.to_datetime(df[column])
    df['year'] = df[column].dt.year
    df['week'] = df[column].dt.isocalendar().week
    df['dayofweek'] = df[column].dt.dayofweek
    df['weekday'] = df[column].dt.day_name()
    df['hour'] = df[column].dt.strftime('%I%p')
    df['hour1'] = df[column].dt.hour
    

# Heatmap: Prediction.
def calmap(df, scale, date, year, week):
    years = df.year.unique().tolist()
    fig = make_subplots(rows=1, cols=1, shared_xaxes=True, vertical_spacing=0.005)
    
    data = df[(df['year'] == year) & (df['week'] == week)]
    fig.add_trace(go.Heatmap(
        z=data.Count.astype('int'),
        x=data.hour,
        y=data.weekday,
        hovertemplate='Hour: %{x}<br>Day: %{y}<br>Requests: %{z}<extra></extra>',
        xgap=3,
        ygap=3,
        coloraxis="coloraxis",
        name='day',),
        1, 1)
    fig.update_yaxes(title_text='Day', tickfont=dict(size=10), row=1, col=1)
    
    title = 'Taxicab service demand. Week: '+ str(week) + '. Date: ' + date
    fig.update_xaxes(title_text='Hour', range=[-1, 24], tickfont=dict(size=10), nticks=25)
    fig.update_layout(coloraxis={'colorscale': scale})
    fig.update_layout(template='seaborn', title=title)
    return fig


def get_customer(path):
    df = pd.read_csv(path)
    return df

# Violin: Graph.
def graph_distributionG1(var_intg='N requests'):
    if var_intg == 'N requests':
        max_value = 2000
    elif var_intg == 'Avg monthly requests':
        max_value = 80
    elif var_intg == 'Frequency: Avg quarterly rq':
        max_value = 200
    else: max_value = 10000
    
    group_type_user = df_total.groupby(['Type of user', 'Phone'], as_index=False)[var_intg].mean().dropna()
    group_type_user2 = group_type_user[(group_type_user[var_intg] < max_value) & (group_type_user['Type of user'].isin(['Premium', "Can't Lose Them"]))].copy()
    fig = px.violin(group_type_user2, x='Type of user', color='Type of user', y=var_intg, box=True, hover_name='Type of user')
    fig.update_xaxes(title_text='Type of user')
    fig.update_yaxes(title_text='Mean: ' + var_intg)
    fig.update_layout(template='seaborn', title='Distribution by Type of user - Var: ' + var_intg, legend_title_text='Type of User')
    return fig
    
def graph_distributionG2(var_intg='N requests'):
    group_type_user = df_total.groupby(['Type of user', 'Phone'], as_index=False)[var_intg].mean().dropna()
    group_type_user2 = group_type_user[group_type_user['Type of user'].isin(['At-Risk', 'Hibernating', 'Loyal Customers', 'Need Attention', 'New Customers',
                                                                             'One-Time', 'Potential Loyalists'])].copy()
    fig = px.violin(group_type_user2, x='Type of user', color='Type of user', y=var_intg, box=True, hover_name='Type of user')
    fig.update_xaxes(title_text='Type of user')
    fig.update_yaxes(title_text='Mean: ' + var_intg)
    fig.update_layout(template='seaborn', title='Distribution by Type of user - Var: ' + var_intg, legend_title_text='Type of User')
    return fig


###########################################################################################

app.layout = html.Div(style={'margin-left': 0, 'margin-right': 0, 'padding-left': 0, 'padding-top': 0, 'padding-right': 0, 'padding-bottom': 0}, children=[ 
    dcc.Location(id='url', refresh=False), 
    html.Div(id='page-content', style={'margin-left': 0, 'margin-right': 0, 'padding-left': 0, 'padding-top': 0, 'padding-right': 0, 'padding-bottom': 0})])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return home.layout
    else:
        return '404'
    
# 

@app.callback(
    Output('output-container-date-picker', 'children'),
    [Input('my-date-picker', 'date')])
def update_output(date):
    string_prefix = 'You have selected: '
    if date is not None:
        date_object = date
        string_prefix = string_prefix + 'Date: ' + date_object
    if len(string_prefix) == len('You have selected: '):
        return 'Select a date to see it displayed here'
    else:
        return string_prefix


    
###########################################################################################
df = get_forecastH('data/model_HDS_H.csv')
df_d = get_forecastD('data/model_HDS.csv')

# Calculate DateTime columns to the "forecast_df" table.
date_time(df, 'ds')

group = df.groupby(['year', 'week', 'dayofweek', 'weekday', 'hour1', 'hour'], as_index=False).yhat.sum()
group.rename(columns={'yhat': 'Count'}, inplace=True)

###########################################################################################
## =========  PLot Forecast =============
@app.callback(
    Output('forecast', 'figure'),
    [Input('output-container-date-picker', 'children')]
)
def graph(date):
    return calmap(group, 'YlGn', date[-10:], year=datetime.strptime(date[-10:], '%Y-%m-%d').year,
                  week=datetime.strptime(date[-10:], '%Y-%m-%d').isocalendar()[1])

@app.callback(
    Output('rq_text', "children"),
    [Input('output-container-date-picker', 'children')],)
def get_requests(date):

    value = df_d[df_d.ds == date[-10:]]['yhat'].values[0].astype('int')
    return datetime.strptime(date[-10:], '%Y-%m-%d').strftime("%A") + ' ' + date[-10:] + ': ' + str(value)

###########################################################################################
@app.callback(
    Output(component_id='barplots', component_property='style'),
   [Input(component_id='day-select', component_property='value'),])

def show_hide_element(visibility_state):
    if visibility_state == 'n':
        return {'display': 'none'}
    if visibility_state == 'm':
        return {'display': 'block'}

df_total = get_customer('data/customer_seg.csv')

# ## =========  PLot Distribution =============
@app.callback(
    dash.dependencies.Output('metricG1', 'figure'),
    [dash.dependencies.Input('co-select', 'value')]
)
def graph(metric):
    return graph_distributionG1(metric)

@app.callback(
    dash.dependencies.Output('metricG2', 'figure'),
    [dash.dependencies.Input('co-select', 'value')]
)
def graph2(metric):
    return graph_distributionG2(metric)



###########################################################################################
if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port="8050", debug=False)
