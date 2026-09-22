from dash import Dash, html, dcc
from pages.home import create_home_layout
from callbacks.iris_callbacks import register_callbacks
import dash_bootstrap_components as dbc


app = Dash(
    __name__,
    external_stylesheets=[
        dbc.themes.FLATLY
    ],
    suppress_callback_exceptions=True
)

app.layout = html.Div([

    # Navbar
    dbc.Navbar(
        dbc.Container(
            [
                dbc.NavbarBrand(
                    [
                        html.I(
                            className="bi bi-flower1 me-2"
                        ),
                        "Iris Explorer"
                    ],
                    className="fw-bold fs-4"
                ),

                html.Span(
                    "Interactive Data Analysis",
                    className="text-white-50"
                ),
            ],
            fluid=True,
            className="px-4"
        ),
        color="primary",
        dark=True,
        className="shadow-sm"
    ),

    # Landing page
    html.Div(
        id="main-div",
        children=[

            dbc.Container(
                dbc.Row(
                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(
                                [

                                    html.Div(
                                        [
                                            html.H1(
                                                "Explore the Iris Dataset",
                                                className="display-5 fw-bold mb-3"
                                            ),

                                            html.P(
                                                (
                                                    "Analyze the classic Iris "
                                                    "dataset using interactive "
                                                    "filters and visualizations."
                                                ),
                                                className="lead text-muted mb-4"
                                            ),

                                            dbc.Button(
                                                [
                                                    "Load Dataset",
                                                    html.Span(
                                                        " →",
                                                        className="ms-2"
                                                    )
                                                ],
                                                id="load-data-button",
                                                color="primary",
                                                size="lg",
                                                className="px-4"
                                            )

                                        ],
                                        className="text-center"
                                    )

                                ],
                                className="p-5"
                            ),
                            className="shadow border-0"
                        ),
                        width=12,
                        md=10,
                        lg=8,
                        xl=7
                    ),
                    justify="center"
                ),
                className="py-5"
            )

        ]
    )
])


register_callbacks(app)


if __name__ == "__main__":
    app.run(debug=False)