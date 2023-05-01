import dash
from dash import html


def title(asset_id=None, dept_id=None):
    return f'Asset analysis: {asset_id} {dept_id}'


def description(asset_id=None, dept_id=None):
    return f'This is the analysis of report {asset_id} from department {dept_id}'


dash.register_page(__name__, path_template="/asset/<asset_id>/department/<dept_id>",
                   title=title, description=description)

# Note I'm using dash.html.Div instead of the usual html.Div on other pages


def layout(asset_id=None, dept_id=None):
    return dash.html.Div(
        f"The user requested asset ID: {asset_id} from dept: {dept_id}."
    )
