from dash import html, Dash, dcc
import dash_bootstrap_components as dbc
import dash_customizable_app_style as style_plugin
import dash_ag_grid as dag
import plotly.express as px
import pandas as pd

# Importing dataset for the example
df                  = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

grid = dag.AgGrid(
    id={"type": "grid", "index": "grid_name"},
    rowData=df.to_dict("records"),
    columnDefs=[{"field": i, 'filter': True, 'sortable': True} for i in df.columns],
    dashGridOptions={"pagination": True},
    columnSize="sizeToFit"
)

# Creating sample figures
line_figure         = px.line(df, x='year', y='pop')
histofram_figure    = px.histogram(df, x='year', y='pop')

# Initialize the app
app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# App layout
app.layout = html.Div(
    id       = "main_container",
    style    = {"minHeight": "100vh"},
    children = [

        # Rregister hooks
        style_plugin.customize_app_selectors(),

        # Informative text
        html.H1("Dash App with Background Color Plugin"),
        html.P("Use the color picker above to change the background color."),

        grid,

        # To be able to also update Figure's background color, text color
        # and font family, use a pattern-matching ID for them as following.
        dcc.Graph(id={"type": "graph", "index": "line"}, figure=line_figure),
        dcc.Graph(id={"type": "graph", "index": "histogram"}, figure=histofram_figure)
    ]
)

# To update Figures from an @app.callback

# @app.callback(
#    Output({"type": "graph", "index": "line"}, "figure"),
#    Rest of your callback....


if __name__ == "__main__":
    app.run(debug=True)