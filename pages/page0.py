import dash
from dash import dcc, html, callback
from dash.dependencies import Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd
import pandas_datareader.data as web
import datetime
import plotly.graph_objects as go
import plotly.express as px
from dash import dcc, html, Input, Output, callback, dash_table

dash.register_page(__name__,
                   path="/",
                   name="Overview",
                   title="Stocks"
                   )

# Load data
df = pd.read_csv("HR_Employee_Attrition.csv")

layout = dbc.Container([
    dbc.Row(
        [
            dbc.Col(
                dcc.Graph(id='department-pie'),
                width=6
            ),
            dbc.Col(
                dcc.Graph(id='working-years-box'),
                width=6
            )
        ]
    ), 
    dbc.Row(
        dbc.Col(
            dash_table.DataTable(
                id='data-table',
                columns=[{"name": i, "id": i} for i in df.columns],
                data=df.head().to_dict('records'),
                style_table={'overflowX': 'auto'},
                style_cell={'textAlign': 'left'}
            ),
            width=12
        )
    )
])

# Define callback to update plots for page 1
@callback(
    Output('department-pie', 'figure'),
    Output('working-years-box', 'figure'),
    [Input('department-pie', 'id'),
    Input('working-years-box', 'id')]
)
def update_graph_1(dummy_input_dep, dummy_input_work):
    #if pathname == '/':
        # Calculate department distribution
        department_counts = df['Department'].value_counts()
        department_pie = px.pie(names=department_counts.index, values=department_counts.values, title='Distribution of Departments')

        # Create box plot for the distribution of working years by department using Plotly
        working_years_box = px.box(df, x='Department', y='TotalWorkingYears', color='Department',
                                      title='Working Years Distribution by Department')

        # Update layout to add labels and adjust title
        working_years_box.update_xaxes(title='Department')
        working_years_box.update_yaxes(title='Working Years')
        working_years_box.update_layout(title='Working Years Distribution by Department')

        return department_pie, working_years_box
    #return {}, {}
