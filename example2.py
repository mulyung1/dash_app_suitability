from dash_extensions.javascript import assign
from dash import Dash, Output, Input, html
from dash_leaflet import Map, TileLayer

# Define eventHandlers with JavaScript function to send latitude and longitude on click
eventHandlers = dict(
    click=assign("function(e, ctx) { ctx.setProps({data: 'You clicked at Latitude: ' + e.latlng.lat + ', Longitude: ' + e.latlng.lng}); }")
)

# Initialize the Dash app
app = Dash(__name__)
app.layout = html.Div([
    Map(children=[TileLayer()], eventHandlers=eventHandlers,
        style={'height': '50vh'}, center=[56, 10], zoom=6, id='map'),
    html.Div(id="log")  # Div to display the latitude and longitude
])

# Define the callback to update the log Div with latitude and longitude
@app.callback(Output("log", "children"), Input("map", "data"))
def log(message):
    return message

if __name__ == '__main__':
    app.run_server(port=2050, debug=True)
