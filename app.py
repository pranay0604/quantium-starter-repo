import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

df = pd.read_csv('data/formatted_output.csv')

df['date'] = pd.to_datetime(df['date'])

df = df.sort_values('date')

fig = px.line(
    df,
    x='date',
    y='sales',
    color='region',
    title='Pink Morsel Sales Over Time',
    labels={'date':"Date", "sales":"Total Sales"}
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
    text="Price Increase (15 Jan 2021)",
    showarrow=False,
    yanchor="bottom"
)

app = dash.Dash(__name__)

app.layout = html.Div(
    style={"textAlign":"center", "padding":"40px"},
    children=[
        html.H1("Soul Foods - Pink Morsel Sales Visualiser"),
        html.P(
            "This dashboard shows Pink Morsel sales over time."
            "The red line marks the price increase on 15 January 2021."
        ),
        dcc.Graph(figure=fig)
    ]
)

if __name__ == "__main__":
    app.run(debug=True)


