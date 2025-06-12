from dash import html, Dash, dcc, Input, Output
import dash_bootstrap_components as dbc
import dash_customizable_app_style as style_plugin
import dash_ag_grid as dag
import plotly.express as px
import pandas as pd

# Importing dataset for the example
df                  = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

grid = dag.AgGrid(
    # To be able to also update AgGrid's background color, text color
    # and font family, use a pattern-matching ID for them as following.
    id              = {"type": "grid", "index": "grid_name"},
    rowData         = df.to_dict("records"),
    columnDefs      = [{"field": i, 'filter': True, 'sortable': True} for i in df.columns],
    dashGridOptions = {"pagination": True},
    columnSize      = "sizeToFit"
)

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

        dcc.Dropdown(
            id='country',
            options= sorted(set(list(df['country']))),
            value='United States'
        ),

        # To be able to also update Figure's background color, text color
        # and font family, use a dcc.Store and a pattern-matching ID for 
        # them as following.
        dcc.Store(id={"type": "figure-store", "index": "line"}),
        dcc.Graph(id={"type": "graph", "index": "line"}),

        dcc.Store(id={"type": "figure-store", "index": "histogram"}),
        dcc.Graph(id={"type": "graph", "index": "histogram"})
    ]
)

# To update Figures from an @app.callback
@app.callback(
    Output({"type": "figure-store", "index": "line"}, "data"),
    Output({"type": "figure-store", "index": "histogram"}, "data"),
    Input('country', 'value')
)
def update_line(country: str):

    new_df: pd.DataFrame    = df[df['country'] == country]
    line_fig                = px.line(new_df, x='year', y='pop', title=country)
    histo_fig               = px.histogram(new_df, x='year', y='pop', title=country)

    return line_fig.to_dict(), histo_fig.to_dict()


if __name__ == "__main__":
    app.run(debug=True)