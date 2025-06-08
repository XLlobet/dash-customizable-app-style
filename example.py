from dash import html, Dash
import dash_bootstrap_components as dbc
import dash_customizable_app_style as style_plugin

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
    ]
)

if __name__ == "__main__":
    app.run(debug=True)