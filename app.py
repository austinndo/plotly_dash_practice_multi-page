import dash
from dash import Dash, html,  dcc

app = Dash(__name__, use_pages=True)

# In each of my pages the layout is defined using the variable 'layout'. This can also be done by useing a function called 'layout' (i.e. def layout(): )

# When creating an app with Pages, only use app.layout here on the main app.py file
app.layout = html.Div([
    html.H1('Multi-page app with Dash Pages'),
    html.Div([
        html.Div(
            dcc.Link(
                f"{page['name']} - {page['path']}", href=page["relative_path"]
            )
        )
        for page in dash.page_registry.values()
    ]),
    dash.page_container
])

if __name__ == '__main__':
    app.run_server(debug=True)
