from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

app = Dash(__name__)
# we can also style things using css as a python dict
colors = {
    'background': '#026661',
    'text': '#ffffff'
}

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5, 3, 6, 2],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal", "Chattanooga", "Chattanooga", "Chattanooga"]
})

fig = px.bar(df, x="City", y="Amount", color="Fruit", barmode="group")

# we can alter the figure before it is displayed 
# so that it better fits within our page
fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'], # UNCOMMENT THIS
    # font_color=colors['text']
)

# you can style the whole enclosing div
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Hello Dash',
        # specify styles for individual elements
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Dash: A web application framework for your data.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='example-graph-2',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
