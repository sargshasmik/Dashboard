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


dash.register_page(__name__,
                   path="/MInfor",
                   name="More Info",
                   title="Stocks"
                   )

# Load data
df = pd.read_csv("HR_Employee_Attrition.csv")

layout = dbc.Container([
    dbc.Row(
        [
            dbc.Col(
                dcc.Graph(id='job-role-bar'),
                width=6
            ),
            dbc.Col(
                dcc.Graph(id='educ-field-bar'),
                width=6
            )
        ]
    )
])


# Define callback to update plots for page 1
@callback(
    Output('job-role-bar', 'figure'),
    Output('educ-field-bar', 'figure'),
    [ Input('job-role-bar', 'id'),
    Input('educ-field-bar', 'id')]
)

def update_graph3( dummy_input_job, dummy_input_educ):
   

    # Calculate the count of each job role
    jobrole_counts = df['JobRole'].value_counts()

    # Create horizontal bar plot for the count of each job role using Plotly
    jobrole_count_plot = px.bar(x=jobrole_counts.values, y=jobrole_counts.index, orientation='h',
                                labels={'x': 'Count', 'y': 'Role'},
                                title='Count of Each Role', color_discrete_sequence=px.colors.qualitative.Set2)

    educ_counts = df['EducationField'].value_counts()

    # Create horizontal bar plot for the count of each education field using Plotly
    educ_count_plot = px.bar(x=educ_counts.values, y=educ_counts.index, orientation='h',
                                labels={'x': 'Count', 'y': 'Education Field'},
                                title='Count of Education Field', color_discrete_sequence=px.colors.qualitative.D3)

    return jobrole_count_plot, educ_count_plot

