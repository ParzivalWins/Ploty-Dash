import dash
import dash_html_components as html
import dash_core_components as dcc

#ininitize the app
app = dash.Dash(__name__)

#Define the app
app.layout = html.Div()
#Run the app
if __name__ == '_main_':
    app.run.server(debug=True)


app.layout = html.Div(children=[
                    html.Div(className='row',
                             children=[
                                 html.Div(className='four columns div-user-controls',
                                     children = [
    html.H2('Dash - STOCK PRICES'),
    html.P('''Visualising time series with Plotly - Dash'''),
    html.P('''Pick one or more stocks from the dropdown below.''')
],
                                 html.Div(className='eight columns div-for-charts bg-grey')
                             )