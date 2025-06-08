# Dash Customizable Style App Plugin Using Dash Hooks

Components for Dash applications using Dash Hooks to dinamically change the background color, the text color and the font family styles of your Dash apps. You can check out this project on PyPi at: https://pypi.org/project/

## Installation

```bash
pip install 
```

## Usage

```python
from dash import html, Dash
import dash_bootstrap_components as dbc
import dash_customizable_app_style as style_plugin

# Initialize the app
app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create an App layout
app.layout = html.Div(

    # Set an ID called 'main_container' to the component you want an exchangeable background color
    id       = "main_container",
    children = [

        # Register the app style selectors
        style_plugin.customize_app_selectors(),

        # Rest of your app code...
    ])
```

## Install requirements

```bash
pip install -r requirements.txt
```

## Example

Run the included example:

```bash
python example.py
```
