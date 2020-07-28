# General libraries
import pandas as pd
import numpy as np
import json
import pprint

# Import dash
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

# Plotting libraries
import geopandas as gpd
import matplotlib.pyplot as plt
import folium


def map_graph():
    data = gpd.read_file("data/dengue-clusters-geojson.geojson")
    kw = {"location": [1.3521, 103.8198], "zoom_start": 12}
    m = folium.Map(**kw)
    folium.GeoJson(data).add_to(m)
    m.save("dengue-cluster.html")
    return m


map_graph()

analysistab = dbc.Card(
    [
        dbc.CardBody(
            [
                # Overview
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.Card(
                                [
                                    dbc.CardHeader(
                                        html.H6(
                                            id="label_info1",
                                            children=["location country"],
                                        )
                                    ),
                                    dbc.CardBody(html.H4(id="location_country")),
                                ],
                                color="info",
                            )
                        ),
                        dbc.Col(
                            dbc.Card(
                                [
                                    dbc.CardHeader(
                                        html.H6(id="label_info2", children=["date"])
                                    ),
                                    dbc.CardBody(html.H4(id="date")),
                                ],
                                color="info",
                            )
                        ),
                        dbc.Col(
                            dbc.Card(
                                [
                                    dbc.CardHeader(
                                        html.H6(
                                            id="label_info3", children=["Total cases"]
                                        )
                                    ),
                                    dbc.CardBody(html.H4(id="total_cases")),
                                ],
                                color="warning",
                            )
                        ),
                        dbc.Col(
                            dbc.Card(
                                [
                                    dbc.CardHeader(
                                        html.H6(
                                            id="label_info4", children=["New cases"]
                                        )
                                    ),
                                    dbc.CardBody(html.H4(id="new_cases")),
                                ],
                                color="warning",
                            )
                        ),
                        dbc.Col(
                            dbc.Card(
                                [
                                    dbc.CardHeader(
                                        html.H6(
                                            id="label_info5", children=["total deaths"]
                                        )
                                    ),
                                    dbc.CardBody(html.H4(id="total_deaths")),
                                ],
                                color="danger",
                            )
                        ),
                        dbc.Col(
                            dbc.Card(
                                [
                                    dbc.CardHeader(
                                        html.H6(
                                            id="label_info6", children=["New deaths"]
                                        )
                                    ),
                                    dbc.CardBody(html.H4(id="new_deaths")),
                                ],
                                color="danger",
                            )
                        ),
                        dbc.Col(
                            dbc.Card(
                                [
                                    dbc.CardHeader(
                                        html.H6(
                                            id="label_info7", children=["total tests"]
                                        )
                                    ),
                                    dbc.CardBody(html.H4(id="total_tests")),
                                ],
                                color="success",
                            )
                        ),
                        dbc.Col(
                            dbc.Card(
                                [
                                    dbc.CardHeader(
                                        html.H6(
                                            id="label_info8", children=["New tests"]
                                        )
                                    ),
                                    dbc.CardBody(html.H4(id="new_tests")),
                                ],
                                color="success",
                            )
                        ),
                    ]
                ),
                html.Br(),
                ## Graphs
                # Dengue cluster
                html.Iframe(
                    id="dengue-map",
                    srcDoc=open("dengue-cluster.html", "r").read(),
                    width="100%",
                    height="500",
                ),
                html.Br(),
                #
                dbc.Spinner(
                    color="primary",
                    type="grow",
                    children=[dcc.Graph(id="graph_treemap_continent")],
                ),
                html.Br(),
                #
                dbc.Spinner(
                    color="primary",
                    type="grow",
                    children=[dcc.Graph(id="graph_bar_continent")],
                ),
                html.Br(),
                #
                dbc.Spinner(
                    color="primary",
                    type="grow",
                    children=[dcc.Graph(id="graph_line_continent")],
                ),
                html.Br(),
                #
                dbc.Spinner(
                    color="primary",
                    type="grow",
                    children=[dcc.Graph(id="graph_area_continent")],
                ),
                html.Br(),
                #
                dbc.Spinner(
                    color="primary",
                    type="grow",
                    children=[dcc.Graph(id="graph_compare_country")],
                ),
                html.Br(),
                # #
                # html.H6(
                #     id="label_not_translated",
                #     children=[
                #         "If any text in this dashboard is untranslated, type or copy paste it here this to translate!"
                #     ],
                # ),
                # dcc.Input(id="input_text", type="text", placeholder=""),
                # html.Button("Translate", id="submit-val"),
                # dbc.Spinner(
                #     color="primary", type="grow", children=[html.Div(id="output_text")]
                # ),
            ]
        )
    ]
)

