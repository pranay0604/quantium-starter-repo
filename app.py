import pandas as pd
import dash
from dash import dcc, html, Input, Output
import plotly.express as px

df = pd.read_csv('data/formatted_output.csv')
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

app = dash.Dash(__name__)

app.layout = html.Div(
    style={
            "fontFamily": "Arial",
            "backgroundColor": "f4f6f8",
            "padding":"40px"
        },
    children=[
            html.H1(
                "Soul Foods - Pink Morsel Sales Dashboard",
                style={"textAlign":"center", "color":"2c3e50"}
            ),
            html.P(
            "Explore Pink Morsel sales across regions and observe the impact of the "
            "price increase on 15 January 2021.",
            style={
                "textAlign":"center",
                "fontSize":"16px",
                "color":"34495e",
                "marginBottom":"30px"
                }
            ),
            html.Div(
                style={
                "width":"300px",
                "margin":"0 auto",
                "padding":"20px",
                "backgroundColor":"white",
                "borderRadius":"8px",
                "boxShadow":"0px 4px 10px rgba(0,0,0,0.1)"
                },
            children=[
                html.Label(
                    "Select Region :",
                    style={"fontWeight":"bold"}
                ),
                dcc.RadioItems(
                    id="region-filter",
                    options=[
                        {"label":"All","value":"all"},
                        {"label":"North","value":"north"},
                        {"label":"East","value":"east"},
                        {"label":"South","value":"south"},
                        {"label":"West","value":"west"},
                    ],
                    value="all",
                    labelStyle={"display":"block","margin":"5px 0"},
                ),
            ]
        ),

        html.Br(),

        html.Div(
            style={
                "backgroundColor":"white",
                "padding":"20px",
                "borderRadius":"8px",
                "boxShadow":"0px 4px 10px rgba(0,0,0,0.1)"
            },
            children=[
                dcc.Graph(id="Sales-Line-Chart")
            ]
        )
    ]
)

@app.callback(
    Output("Sales-Line-Chart","figure"),
    Input("region-filter","value")
)

def update_chart(selected_region):
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == selected_region]

    fig = px.line(
        filtered_df,
        x="date",
        y="sales",
        color="region" if selected_region == "all" else None,
        labels={
            "date":"Date",
            "sales":"Total Sales"
        },
        title="Pink Morsel Sales Over Time"
    )

    fig.add_shape(
        type="line",
        x0="2021-01-15",
        x1="2021-01-15",
        y0=0,
        y1=1,
        xref="x",
        yref="paper",
        line=dict(color="red", dash="dash")
    )

    fig.add_annotation(
        x="2021-01-15",
        y=1,
        xref="x",
        yref="paper",
        text="Price Increase (15 January 2021)",
        showarrow=False,
        yanchor="bottom"
    )

    return fig

if __name__ == "__main__":
    app.run()


