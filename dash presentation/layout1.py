# Run this app with `python app.py` and
# how to set up a basic dashboard
# run file, then visit:
# http://127.0.0.1:8050/

# code: import dependencies 
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

# initialize Dash app object
app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
# for now we have this simple dataframe:
df = pd.DataFrame({
    "Cans": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

# we can use plotly express to create a grouped bar chart
fig = px.bar(df, y="Cans", x="Amount", color="City", barmode="group")

# finally we use the Dash app to display the graph
# begin by using the dash html component Div
app.layout = html.Div(children=[
    #inside, we can have a list of arbitrary children
    # that are turned into basic html
    html.H1(children='Dash Is Cool'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),
    # finally, we use a dash core component (dcc)
    # to display our graph by passing "fig" in for figure
    dcc.Graph(
        id='graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
