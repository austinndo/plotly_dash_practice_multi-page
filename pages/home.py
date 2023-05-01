import dash
from dash import html, dcc

# Update title and description
# Title is what appears in the browser tab, similar to title in the index.html file of my React apps
# You can also add more than one path variable which will be shared in links.. ex: /report/4/department/2/...


def title():
    return f'Analysis Home'


def description():
    return f'These are the pages containing the charts and analysis of the data'

# Setting the path for home page here. I call dash.register_page on each of my pages but I don't explicitly set a path for each. In the event you don't set a path, it is autogenerated based on the module name!


# Dash knows to include these files in the pages folder because we called 'dash.register_page within the desired files
dash.register_page(__name__, path='/', title=title, description=description)

# If we want to specify the page path, title, and link name you can do so like this:

# dash.register_page(
#     __name__,
#     path='/analytics-dashboard',
#     title='Our Analytics Dashboard',
#     name='Our Analytics Dashboard'
# )

layout = html.Div(children=[
    html.H1(children='This is the Home page'),
    html.Div(children=''' This is the Home page content '''),
])
