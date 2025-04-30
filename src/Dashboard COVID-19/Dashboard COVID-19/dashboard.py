import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.graph_objects as go

import pandas as pd
import json

# Centro do mapa
CENTER_LAT, CENTER_LON = -14.272572694355336, -51.25567404158474

# =======================
# Carregamento de Dados
# =======================
df_states = pd.read_csv("df_states.csv")
df_brasil = pd.read_csv("df_brasil.csv")

token = open(".mapbox_token").read()
brazil_states = json.load(open("geojson/brazil_geo.json", "r"))

df_states_ = df_states[df_states["data"] == "2020-05-13"]
select_columns = {
    "casosAcumulado": "Casos Acumulados", 
    "casosNovos": "Novos Casos", 
    "obitosAcumulado": "Óbitos Totais",
    "obitosNovos": "Óbitos por dia"
}

# =======================
# Inicialização do App
# =======================
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

# =======================
# Gráfico Mapa
# =======================
fig = go.Figure(go.Choropleth(
    z=df_states_["casosNovos"],
    hoverinfo="location+z",
    locationmode="USA-states",
    locations=df_states_["estado"],
    colorscale="Viridis",  # Exemplo de colorscale
    colorbar_title="Casos Novos",
    showscale=True  # Adicionando a barra de cores
))


fig.update_geos(
    visible=True,
    fitbounds="locations",
    projection_type="mercator"
)

fig.update_layout(
    geo=dict(
        lakecolor='rgb(255, 255, 255)',
    ),
    mapbox_style="carto-darkmatter",
    paper_bgcolor="#242424",
    autosize=True,
    margin=go.layout.Margin(l=0, r=0, t=0, b=0),
    showlegend=False,
)

# =======================
# Gráfico Inicial (RO)
# =======================
df_data = df_states[df_states["estado"] == "RO"]
fig2 = go.Figure(layout={"template": "plotly_dark"})
fig2.add_trace(go.Scatter(x=df_data["data"], y=df_data["casosAcumulado"]))
fig2.update_layout(
    paper_bgcolor="#242424",
    plot_bgcolor="#242424",
    autosize=True,
    margin=dict(l=10, r=10, b=10, t=10)
)

# =======================
# Layout
# =======================
app.layout = dbc.Container(
    children=[
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.Img(id="logo", src=app.get_asset_url("logo_dark.png"), height=50),
                    html.H5("Evolução COVID-19"),
                    dbc.Button("BRASIL", color="primary", id="location-button", size="lg")
                ], style={"background-color": "#1E1E1E", "margin": "-25px", "padding": "25px"}),

                html.P("Informe a data na qual deseja obter informações:", style={"margin-top": "40px"}),
                html.Div(
                    className="div-for-dropdown",
                    id="div-test",
                    children=[
                        dcc.DatePickerSingle(
                            id="date-picker",
                            min_date_allowed=df_states.groupby("estado")["data"].min().max(),
                            max_date_allowed=df_states.groupby("estado")["data"].max().min(),
                            initial_visible_month=df_states.groupby("estado")["data"].min().max(),
                            date=df_states.groupby("estado")["data"].max().min(),
                            display_format="MMMM D, YYYY",
                            style={"border": "0px solid black"},
                        )
                    ]
                ),

                dbc.Row([
                    dbc.Col(dbc.Card(dbc.CardBody([
                        html.Span("Casos recuperados", className="card-text"),
                        html.H3(id="casos-recuperados-text", style={"color": "#adfc92"}),
                        html.Span("Em acompanhamento", className="card-text"),
                        html.H5(id="em-acompanhamento-text"),
                    ]), color="light", outline=True,
                        style={"margin-top": "10px", "box-shadow": "0 4px 4px rgba(0,0,0,0.15), 0 4px 20px rgba(0,0,0,0.19)", "color": "#FFFFFF"}), md=4),

                    dbc.Col(dbc.Card(dbc.CardBody([
                        html.Span("Casos confirmados totais", className="card-text"),
                        html.H3(id="casos-confirmados-text", style={"color": "#389fd6"}),
                        html.Span("Novos casos na data", className="card-text"),
                        html.H5(id="novos-casos-text"),
                    ]), color="light", outline=True,
                        style={"margin-top": "10px", "box-shadow": "0 4px 4px rgba(0,0,0,0.15), 0 4px 20px rgba(0,0,0,0.19)", "color": "#FFFFFF"}), md=4),

                    dbc.Col(dbc.Card(dbc.CardBody([
                        html.Span("Óbitos confirmados", className="card-text"),
                        html.H3(id="obitos-text", style={"color": "#DF2935"}),
                        html.Span("Óbitos na data", className="card-text"),
                        html.H5(id="obitos-na-data-text"),
                    ]), color="light", outline=True,
                        style={"margin-top": "10px", "box-shadow": "0 4px 4px rgba(0,0,0,0.15), 0 4px 20px rgba(0,0,0,0.19)", "color": "#FFFFFF"}), md=4),
                ]),

                html.Div([
                    html.P("Selecione que tipo de dado deseja visualizar:", style={"margin-top": "25px"}),
                    dcc.Dropdown(
                        id="location-dropdown",
                        options=[{"label": j, "value": i} for i, j in select_columns.items()],
                        value="casosNovos",
                        style={"margin-top": "10px"}
                    ),
                    dcc.Graph(id="line-graph", figure=fig2, style={"background-color": "#242424"}),
                ])
            ], md=5, style={"padding": "25px", "background-color": "#242424"}),

            dbc.Col([
                dcc.Loading(
                    id="loading-1",
                    type="default",
                    children=[
                        dcc.Graph(id="choropleth-map", figure=fig, style={'height': '100vh', 'margin-right': '10px'})
                    ]
                )
            ], md=7),
        ], className="g-0")
    ],
    fluid=True
)

# =======================
# Callbacks
# =======================

@app.callback(
    [
        Output("casos-recuperados-text", "children"),
        Output("em-acompanhamento-text", "children"),
        Output("casos-confirmados-text", "children"),
        Output("novos-casos-text", "children"),
        Output("obitos-text", "children"),
        Output("obitos-na-data-text", "children"),
    ],
    [Input("date-picker", "date"), Input("location-button", "children")]
)
def display_status(date, location):
    df_data_on_date = df_brasil[df_brasil["data"] == date] if location == "BRASIL" else \
                      df_states[(df_states["estado"] == location) & (df_states["data"] == date)]

    def format_value(val):
        return "-" if pd.isna(val) else f'{int(val):,}'.replace(",", ".")

    return (
        format_value(df_data_on_date["Recuperadosnovos"].values[0]),
        format_value(df_data_on_date["emAcompanhamentoNovos"].values[0]),
        format_value(df_data_on_date["casosAcumulado"].values[0]),
        format_value(df_data_on_date["casosNovos"].values[0]),
        format_value(df_data_on_date["obitosAcumulado"].values[0]),
        format_value(df_data_on_date["obitosNovos"].values[0]),
    )


@app.callback(
    Output("line-graph", "figure"),
    [Input("location-dropdown", "value"), Input("location-button", "children")]
)
def plot_line_graph(plot_type, location):
    df_data_on_location = df_brasil.copy() if location == "BRASIL" else \
                          df_states[df_states["estado"] == location]

    fig2 = go.Figure(layout={"template": "plotly_dark"})
    if plot_type in ["casosNovos", "obitosNovos"]:
        fig2.add_trace(go.Bar(x=df_data_on_location["data"], y=df_data_on_location[plot_type]))
    else:
        fig2.add_trace(go.Scatter(x=df_data_on_location["data"], y=df_data_on_location[plot_type]))

    fig2.update_layout(
        paper_bgcolor="#242424",
        plot_bgcolor="#242424",
        autosize=True,
        margin=dict(l=10, r=10, b=10, t=10)
    )
    return fig2


# =======================
# Run
# =======================
if __name__ == "__main__":
    app.run(debug=True)

