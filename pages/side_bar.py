import dash
from dash import html
import dash_bootstrap_components as dbc


# dash.page_registry is accessed within the sidebar function. If dash.page_registry was not within a function the app wouldn't work because 'dash.page_registry wouldn't  be ready when the page loads'

def sidebar():
    return html.Div(
        dbc.Nav(
            [
                dbc.NavLink(
                    [
                        html.Div(page["name"], className="ms-2"),
                    ],
                    href=page["path"],
                    active="exact",
                )
                for page in dash.page_registry.values()
                if page["path"].startswith("/topic")
            ],
            vertical=True,
            pills=True,
            className="bg-light",
        )
    )
