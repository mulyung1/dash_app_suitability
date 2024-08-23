'''this code prints to the js console coordinates of clicked location on a leaflet map'''

from dash_extensions.javascript import assign
from dash import Dash
from dash_leaflet import Map, TileLayer

#define an event handler to print out coordinates
eventHandlers = dict(
    click=assign("function(e, ctx){console.log(`You clicked at ${e.latlng}.`)}"),
)

#initialise app
app = Dash(__name__)

#create a Leaflet map with a TileLayer and attach the eventHandlers.
app.layout = Map(children=[TileLayer()], eventHandlers=eventHandlers,
                 style={'height': '100vh'}, center=[-1.24613, 38.232422], zoom=8)

if __name__ == '__main__':
    app.run_server(port=8888, debug=True)