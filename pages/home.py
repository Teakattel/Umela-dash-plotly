from dash import html, dcc, dash_table


def create_home_layout(df):

    return html.Div([

        # First row: text + graph
        html.Div([

            html.Div(
                id="iris-info",
                children=[
                    html.H2(
                        "Iris Dataset",
                        className="fw-bold mb-2"
                    ),
                    html.P(
                        "Data loaded successfully.",
                        className="text-muted mb-0"
                    )
                ],
                style={
                    "display": "none",
                    "flex": "1"
                },
                className="card p-4 shadow-sm border-0"
            ),

            html.Div(
                id="graph-container",
                children=[
                    dcc.Graph(id="iris-graph")
                ],
                style={
                    "display": "none",
                    "flex": "2"
                },
                className="card p-3 shadow-sm border-0"
            ),

        ], style={
            "display": "flex",
            "gap": "20px",
        }, className="mb-4"),

        # Second row: filters
        html.Div(
            id="filters-container",
            children=[

                html.H3(
                    "Filters",
                    className="fw-bold mb-4"
                ),

                html.Div([
                    html.Label(
                        "Sepal Length",
                        className="fw-semibold mb-2"
                    ),

                    dcc.RangeSlider(
                        id="sepal-length-slider",
                        min=df["sepal_length"].min(),
                        max=df["sepal_length"].max(),
                        value=[
                            df["sepal_length"].min(),
                            df["sepal_length"].max()
                        ],
                        step=0.1,
                        tooltip={
                            "placement": "bottom",
                            "always_visible": True
                        },
                    ),
                ], className="mb-4"),

                html.Div([
                    html.Label(
                        "Sepal Width",
                        className="fw-semibold mb-2"
                    ),

                    dcc.RangeSlider(
                        id="sepal-width-slider",
                        min=df["sepal_width"].min(),
                        max=df["sepal_width"].max(),
                        value=[
                            df["sepal_width"].min(),
                            df["sepal_width"].max()
                        ],
                        step=0.1,
                        tooltip={
                            "placement": "bottom",
                            "always_visible": True
                        },
                    ),
                ], className="mb-4"),

                html.Div([
                    html.Label(
                        "Petal Length",
                        className="fw-semibold mb-2"
                    ),

                    dcc.RangeSlider(
                        id="petal-length-slider",
                        min=df["petal_length"].min(),
                        max=df["petal_length"].max(),
                        value=[
                            df["petal_length"].min(),
                            df["petal_length"].max()
                        ],
                        step=0.1,
                        tooltip={
                            "placement": "bottom",
                            "always_visible": True
                        },
                    ),
                ], className="mb-4"),

                html.Div([
                    html.Label(
                        "Petal Width",
                        className="fw-semibold mb-2"
                    ),

                    dcc.RangeSlider(
                        id="petal-width-slider",
                        min=df["petal_width"].min(),
                        max=df["petal_width"].max(),
                        value=[
                            df["petal_width"].min(),
                            df["petal_width"].max()
                        ],
                        step=0.1,
                        tooltip={
                            "placement": "bottom",
                            "always_visible": True
                        },
                    ),
                ], className="mb-4"),

                html.Button(
                    "Render",
                    id="render-button",
                    n_clicks=0,
                    style={
                        "margin-top": "20px"
                    },
                    className="btn btn-primary px-4"
                ),

            ]
        , className="card p-4 shadow-sm border-0 mb-4"),

        # Third row: table
        html.Div(
            id="table-container",
            children=[
                dash_table.DataTable(
                    id="iris-table",
                    data=[],
                    page_size=10
                )
            ],
            style={"display": "none"},
            className="card p-4 shadow-sm border-0"
        ),

    ], className="container-fluid py-4")