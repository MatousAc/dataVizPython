from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')

# in this section we feature the plotly scatterplot.
# this a great example of having many ways to encode data:
fig = px.scatter(df, 
    x="gdp per capita", y="life expectancy", # 2d position
    size="population", # size
    color="continent", # colour
    hover_name="country",
    # if you want to control the x and y scale:
    log_x=True, size_max=60)

app.layout = html.Div([
    # using simple graph component again
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
