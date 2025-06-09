# Dash Customizable Style App Plugin Using Dash Hooks

Background color, text color and font family selectors to cusotmize your Dash apps using Dash Hooks.

## Usage

```python
from dash import html, Dash
import dash_bootstrap_components as dbc
import dash_customizable_app_style as style_plugin

# Initialize the Dash app
app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create the Dash App layout
app.layout = html.Div(

    # Set an ID called 'main_container' to the component you want an exchangeable background color, text color and font family
    id       = "main_container",
    children = [

        # Register the app style selectors
        style_plugin.customize_app_selectors(),

        # To be able to also update Figure's background color, text color
        # and font family, use a pattern-matching ID for them as following.
        dcc.Graph(id={"type": "graph", "index": "line"}, figure=your_line_figure_here),
        dcc.Graph(id={"type": "graph", "index": "histogram"}, figure=your_histogram_figure_here)

        # Rest of your app code...
    ])

# To update Figures from an @app.callback
@app.callback(
    Output({"type": "graph", "index": "line"}, "figure"),
    #    Rest of your callback....
```

## Install requirements

```bash
pip install dash
pip install dash-bootstrap-components
```
