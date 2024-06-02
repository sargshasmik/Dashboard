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
        [
            dbc.Col(
                dcc.Graph(id='income-by-dep-hist'),
                width=6
            )

        ]
    )
])

# Define callback to update plots for page 1
@callback(
    Output('income-by-dep-hist', 'figure'),
    [ Input('income-by-dep-hist', 'id')]
)

def update_graph2(dummy_input_income):
   
    # Create histograms for monthly income by department using Plotly
    income_histograms = px.histogram(df, x='MonthlyIncome', color='Department', facet_col='Department',
                                    facet_col_wrap=4, barmode='overlay', title='Histograms of Monthly Income by Department')

    # Update layout to add labels and adjust title
    income_histograms.update_xaxes(title='Monthly Income')
    income_histograms.update_yaxes(title='Frequency')
    income_histograms.update_layout(title='Histograms of Monthly Income by Department')

    # Adjust spacing between facet columns
    income_histograms.update_layout(margin=dict(l=20, r=20, t=50, b=50),  # Adjust margins
                                    paper_bgcolor='rgba(255,255,255,0.8)',  # Set background color
                                    plot_bgcolor='rgba(255,255,255,0.8)',  # Set plot area color
                                    font=dict(color='black'),  # Set font color
                                    height=600,  # Set figure height
                                    width=1000,  # Set figure width
                                    )
    # Rotate x-axis labels for better visibility
    income_histograms.update_xaxes(tickangle=45)

    # Update legend position and orientation
    income_histograms.update_layout(legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1),
                                    )

    # Adjust spacing between subplots
    income_histograms.update_layout(
        margin=dict(l=40, r=40, t=40, b=40),  # Adjust overall margin
        autosize=False,
        width=1000,
        height=600,
        hovermode="closest",
        template="plotly_white"
    )



    return income_histograms
