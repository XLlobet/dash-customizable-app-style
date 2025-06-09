from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")
setup(
    name="dash-customizable-app-style",
    version="0.0.6",
    install_requires=[
        "dash>=3.0.3",
        "dash-bootstrap-components==2.0.3",
    ],
    entry_points={"dash_hooks": ["dash_customizable_app_style = dash_customizable_app_style"]},
    packages=["dash_customizable_app_style"],
    author="X.Llobet",
    author_email="llbt.nvs.x@gmail.com",
    description="Customizable background color, text color and font family for Dash applications",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/XLlobet/dash-customizable-app-style",
),