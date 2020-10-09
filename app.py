import dash
import dash_html_components as html

#ininitize the app
app = dash.Dash(__name__)

#Define the app
app.layout = html.Div()
#Run the app
if __name__ == '_main_':
    app.run.server(debug=True)