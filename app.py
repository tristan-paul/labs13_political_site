import os
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from sklearn.externals import joblib
import json


#stylesheet - placeholder from Dash tutorial
css = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=css)
server = app.server


#load model
if __name__ == '__main__':
    model = joblib.load('./model.joblib')
    app.run_server(debug=True)

model = joblib.load('./model.joblib')

#the webpage formatting
app.layout = html.Div(children=[

    #input field populated by default with first row
    html.Div(children=[
        html.Label('enter values'),
        dcc.Input(id='Year', placeholder='2008', type='text'),
        dcc.Input(id='Type', placeholder='4th Quarter', type='text'),
        dcc.Input(id='RegistrantName', placeholder='Ogilvy Government Relations', type='text'),
        dcc.Input(id='GeneralDescription', placeholder='Lobbying', type='text'),
        dcc.Input(id='ClientName', placeholder='At&t', type='text'),
        dcc.Input(id='SelfFiler', placeholder='0', type='text'),
        dcc.Input(id='IsStateOrLocalGov', placeholder='0', type='text'),
        dcc.Input(id='ClientCountry', placeholder='Other', type='text'),
        dcc.Input(id='ClientState', placeholder='Outside US', type='text'),
    ]),

    #button to finalize input
    html.Button('predict', id='button', n_clicks=0),

    #storage for input as json
    html.Div(id='hidden-json', style={'display': 'none'}),

    #where result prints
    html.Div(id='Result')
])


#callback - button click; stores request as json
@app.callback(
    Output('hidden-json', 'children'),
    [Input('button', 'n_clicks')],
    state = [State('Year', 'value'),
     State('Type', 'value'),
     State('RegistrantName', 'value'),
     State('GeneralDescription', 'value'),
     State('ClientName', 'value'),
     State('SelfFiler', 'value'),
     State('IsStateOrLocalGov', 'value'),
     State('ClientCountry', 'value'),
     State('ClientState', 'value')]
)
def getjson(n_clicks, Year, Type, RegistrantName,
            GeneralDescription, ClientName, SelfFiler,
            IsStateOrLocalGov, ClientCountry, ClientState):
    x = {
        "Year": Year,
        "Type": Type,
        "RegistrantName": RegistrantName,
        "GeneralDescription": GeneralDescription,
        "ClientName": ClientName,
        "SelfFiler": SelfFiler,
        "IsStateOrLocalGov": IsStateOrLocalGov,
        "ClientCountry": ClientCountry,
        "ClientState": ClientState
    }
    request = json.dumps(x)
    return request


#callback - predict on json div
@app.callback(
    Output("Result", 'children'),
    [Input('hidden-json', 'children')]
)
def predict_cost(req):
    cost = model.predict(req)
    return "To have an effect, the client would pay $'{}'".format(cost)

