import dash
from dash import html

dash.register_page(__name__)

layout = html.H1("This is the custom 404 content")
