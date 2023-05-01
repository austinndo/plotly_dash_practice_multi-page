import dash
from dash import html

dash.register_page(__name__)


def layout(report_id=None, department_id=None, **other_unknown_query_strings):
    return html.Div(
        children=[
            html.H1(children='This is our Archive page'),

            html.Div(children=f'''
	        This is report: {report_id}.\n
			This is department: {department_id}.
	    '''),

        ])

# When you navigate to "http://127.0.0.1:8050/archive?report_id=3" we will display f'This is report: 3'
