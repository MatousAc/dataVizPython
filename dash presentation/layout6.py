# in this program, we introduce basic core components that 
# provide more interactivity to a user (akin to Tableaus filters)
from dash import Dash, html, dcc

# extracting the repeated list
cities = ['New York City', 'Montréal', 'San Francisco']
app = Dash(__name__)

# layout
app.layout = html.Div([
	# column 1
	html.Div(children=[
		# single dropdown
		html.Label('Dropdown'),
		dcc.Dropdown(cities, 'Montréal'),

		# multi-select
		html.Br(),
		html.Label('Multi-Select Dropdown'),
		dcc.Dropdown(cities,
									['Montréal', 'San Francisco'],
									multi=True),

		# radio
		html.Br(),
		html.Label('Radio Items'),
		dcc.RadioItems(cities, 'Montréal'),
	], style={'padding': 10, 'flex': 1}),

	# column 2
	html.Div(children=[
		# czech boxes
		html.Label('Checkboxes'),
		dcc.Checklist(cities,
			['Montréal', 'San Francisco']
		),

		# basic text
		html.Br(),
		html.Label('Text Input'),
		dcc.Input(value='MTL', type='text'),

		# slider
		html.Br(),
		html.Label('Slider'),
		dcc.Slider(
			min=0,
			max=9,
			marks={i: f'Label {i}' if i == 1 else str(i) for i in range(1, 6)},
			value=5,
		),
	], style={'padding': 10, 'flex': 1}) # column styling
], style={'display': 'flex', 'flex-direction': 'row'}) # embedded component styling

if __name__ == '__main__':
	# help(dcc.Dropdown)
	app.run_server(debug=True)
