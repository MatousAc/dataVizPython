from dash import Dash, html, dcc

app = Dash(__name__)

# turns out you can just use markdown to create your webpage!
markdown_text = '''
### Dash and Markdown
***
Dash apps can be written in **Markdown**.
Dash uses the [CommonMark](http://commonmark.org/)
specification of Markdown.
'''

info = '''
For instance, you could use this to display information quickly and easily.
'''

app.layout = html.Div([
    dcc.Markdown(children=markdown_text),
    dcc.Markdown(info) # we can omit the "children"
])

if __name__ == '__main__':
    app.run_server(debug=True)
