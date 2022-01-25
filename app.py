import dash
from dash.dependencies import Input, Output
from dash import html
from dash import dcc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# first tab = plotly NFL stats
df = pd.read_csv(r"C:\Users\mkhou\OneDrive\Desktop\final-project\data\stats.csv")
fig1 = px.scatter_3d(df, x='Player', y='TD', z='INT', color='Player')



# third tab = solar system planets in plotly 3d
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']
planet_colors = ['rgb(135, 135, 125)', 'rgb(210, 50, 0)', 'rgb(50, 90, 255)',
                 'rgb(178, 0, 0)', 'rgb(230, 140, 30)', 'rgb(235, 205, 130)',
                 'rgb(55, 255, 217)', 'rgb(38, 0, 171)', 'rgb(0, 0, 0)']
distance_from_sun = [57.9, 108.2, 149.6, 227.9, 778.6, 1433.5, 2872.5, 4495.1, 5906.4]
density = [5427, 5243, 5514, 3933, 1326, 687, 1271, 1638, 2095]
gravity = [3.7, 8.9, 9.8, 3.7, 23.1, 9.0, 8.7, 11.0, 0.7]
planet_diameter = [4879, 12104, 12756, 6792, 142984, 120536, 51118, 49528, 2370]
# Create trace, sizing bubbles by planet diameter
fig2 = go.Figure(data=go.Scatter3d(
    x = distance_from_sun,
    y = density,
    z = gravity,
    text = planets,
    mode = 'markers',
    marker = dict(
        sizemode = 'diameter',
        sizeref = 750, # info on sizeref: https://plotly.com/python/reference/scatter/#scatter-marker-sizeref
        size = planet_diameter,
        color = planet_colors,
        )
))
fig2.update_layout(width=800, height=800, title = 'Planets in our star system!',
                  scene = dict(xaxis=dict(title='Distance from Sun', titlefont_color='white'),
                               yaxis=dict(title='Density', titlefont_color='white'),
                               zaxis=dict(title='Gravity', titlefont_color='white'),
                               bgcolor = 'rgb(20, 24, 54)'
                           ))



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
        dcc.Tab(label='The solar system in 3d!', value='tab-2-example-graph'),
        dcc.Tab(label='Download a cool image', value='tab-3-example-graph'),
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
            html.H3('Planets!'),
            dcc.Graph(figure=fig2)
        ])



    elif tab == 'tab-3-example-graph':
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