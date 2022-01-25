import dash
from dash.dependencies import Input, Output
from dash import html
from dash import dcc
import pandas as pd
import plotly.express as px


# first tab info
df = pd.read_csv(r"C:\Users\mkhou\OneDrive\Desktop\final-project\data\stats.csv")
fig1 = px.scatter_3d(df, x='Player', y='TD', z='INT', color='Player')


# layout stuff
myheading1 = 'Final Project... it is pretty good'
tabtitle = 'final project'
sourceurl = 'https://www.nfl.com/stats/player-stats/'
githublink = '{insert github link here}'
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
image1 = 'nagini.jpg'

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle
app.config['suppress_callback_exceptions'] = True


# app layout
app.layout = html.Div([
    html.H1(myheading1, style={'text-align': 'center'}),
    html.Img(src=app.get_asset_url(image1)),
    dcc.Tabs(id="tabs-example-graph", value='tab-1-example-graph', children=[
        dcc.Tab(label='Plotly in 3d!', value='tab-1-example-graph'),
        dcc.Tab(label='Download an image', value='tab-2-example-graph'),

    ]),

    html.Div(id='tabs-content-example-graph'),
    html.Div([
        html.A('Code on Github', href=githublink),
        html.Br(),
        html.A("Data Source for NFL Stats", href=sourceurl),
    ])
])


# app callback
@app.callback(Output('tabs-content-example-graph', 'children'),
              Input('tabs-example-graph', 'value'))
def render_content(tab):
    if tab == 'tab-1-example-graph':
        return html.Div([
            html.H3('NFL QB stats for 2021'),
            dcc.Graph(figure=fig1)
        ])

    elif tab == 'tab-2-example-graph':
        return html.Div([
            html.Button("Download Image", id="btn_image"), dcc.Download(id="download-image")
        ])
@app.callback(
    Output("download-image", "data"),
    Input("btn_image", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    return dcc.send_file(r"C:\Users\mkhou\OneDrive\Desktop\final-project\assets\dragon.png")



# run app
if __name__ == '__main__':
    app.run_server(debug=True)