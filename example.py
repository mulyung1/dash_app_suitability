from dash_extensions.javascript import assign
from dash import Dash
from dash_leaflet import Map, TileLayer

eventHandlers = dict(
    click=assign("function(e, ctx){console.log(`You clicked at ${e.latlng}.`)}"),
)
app = Dash(__name__)
app.layout = Map(children=[TileLayer()], eventHandlers=eventHandlers,
                 style={'height': '100vh'}, center=[-1.24613, 38.232422], zoom=8)

if __name__ == '__main__':
    app.run_server(port=8888, debug=True)