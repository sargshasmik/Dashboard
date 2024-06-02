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
                   path="/MoreInfo",
                   name="Monthly Income",
                   title="Stocks"
                   )

# Load data
df = pd.read_csv("HR_Employee_Attrition.csv")

layout = dbc.Container([
    dbc.Row(
        dbc.Col(
            dcc.Dropdown(
                id='department-dropdown',
                options=[{'label': dept, 'value': dept} for dept in df['Department'].unique()],
                value=df['Department'].unique()[0],
                clearable=False,
                style={'width': '50%'}
            ),
            width=12
        )
    ),
    dbc.Row(
        dbc.Col(
            dcc.Graph(id='income-histogram'),
            width=12
        )
    )
])

# Define callback to update plots for page 1
@callback(
    Output('income-histogram', 'figure'),
    [Input('department-dropdown', 'value')]
)

def update_histogram(selected_department):
    filtered_df = df[df['Department'] == selected_department]

    # Create histogram for monthly income by selected department using Plotly Express
    income_histogram = px.histogram(filtered_df, x='MonthlyIncome', color='Department', facet_col='Department',
                                 facet_col_wrap=4, barmode='overlay', title=f'Histogram of Monthly Income for {selected_department}')

    # Update layout to add labels and adjust title
    income_histogram.update_xaxes(title='Monthly Income')
    income_histogram.update_yaxes(title='Frequency')
    income_histogram.update_layout(title=f'Histogram of Monthly Income for {selected_department}',
                                   margin=dict(l=20, r=20, t=50, b=50),  # Adjust margins
                                   paper_bgcolor='rgba(255,255,255,0.8)',  # Set background color
                                   plot_bgcolor='rgba(255,255,255,0.8)',  # Set plot area color
                                   font=dict(color='black'),  # Set font color
                                   height=600,  # Set figure height
                                   width=1000,  # Set figure width
                                   )

    # Rotate x-axis labels for better visibility
    income_histogram.update_xaxes(tickangle=45)

    # Update legend position and orientation
    income_histogram.update_layout(legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1))

    return income_histogram