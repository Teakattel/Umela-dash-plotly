from dash import Input, Output, State, html
import pandas as pd
import plotly.express as px
from backend.data_service import load_iris_data
from pages.home import create_home_layout

def register_callbacks(app):

    @app.callback(
        Output("main-div", "children"),
        Input("load-data-button", "n_clicks"),
        prevent_initial_call=True
    )
    def load_data(n_clicks):
        df = load_iris_data()
        return (
            create_home_layout(df),
        )


    @app.callback(
        Output("iris-table", "data"),
        Output("table-container", "style"),

        Output("iris-info", "children"),
        Output("iris-info", "style"),

        Output("iris-graph", "figure"),
        Output("graph-container", "style"),

        Input("render-button", "n_clicks"),

        State("sepal-length-slider", "value"),
        State("sepal-width-slider", "value"),
        State("petal-length-slider", "value"),
        State("petal-width-slider", "value"),

        prevent_initial_call=True
    )
    def filter_iris(
        n_clicks,
        sepal_length_range,
        sepal_width_range,
        petal_length_range,
        petal_width_range
    ):

        # Load the data
        df = load_iris_data()

        # Filter the data
        filtered_df = df[
            (df["sepal_length"].between(*sepal_length_range)) &
            (df["sepal_width"].between(*sepal_width_range)) &
            (df["petal_length"].between(*petal_length_range)) &
            (df["petal_width"].between(*petal_width_range))
        ]

        # Count each species
        class_counts = (
            filtered_df["species"]
            .value_counts()
            .reindex(
                ["setosa", "versicolor", "virginica"],
                fill_value=0
            )
            .reset_index()
        )

        class_counts.columns = ["species", "count"]

        # Calculate percentage of each class
        if len(filtered_df) > 0:
            class_counts["percentage"] = (
                class_counts["count"] / len(filtered_df) * 100
            )
        else:
            class_counts["percentage"] = 0

        # Information displayed on the left
        info = [
            html.H2("Iris Dataset"),

            html.P(
                f"Total samples: {len(df)}"
            ),

            html.P(
                f"Filtered samples: {len(filtered_df)}"
            ),

            html.H4("Class distribution"),

            html.P(
                f"Setosa: {class_counts.loc[class_counts['species'] == 'setosa', 'percentage'].iloc[0]:.1f}%"
            ),

            html.P(
                f"Versicolor: {class_counts.loc[class_counts['species'] == 'versicolor', 'percentage'].iloc[0]:.1f}%"
            ),

            html.P(
                f"Virginica: {class_counts.loc[class_counts['species'] == 'virginica', 'percentage'].iloc[0]:.1f}%"
            ),
        ]

        # Create bar chart
        fig = px.bar(
            class_counts,
            x="species",
            y="count",
            color="species",
            text="count",
            title="Iris Classes After Filtering",
            labels={
                "species": "Species",
                "count": "Number of Samples"
            }
        )

        fig.update_traces(
            textposition="outside"
        )

        fig.update_layout(
            xaxis={
                "categoryorder": "array",
                "categoryarray": [
                    "setosa",
                    "versicolor",
                    "virginica"
                ]
            }
        )

        return (
            filtered_df.to_dict("records"),
            {"display": "block"},

            info,
            {"display": "block", "flex": "1"},

            fig,
            {"display": "block", "flex": "2"}
        )