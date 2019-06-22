import os
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from sklearn.externals import joblib

#stylesheet - placeholder from Dash tutorial
css = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=css)
server = app.server

#the webpage formatting
app.layout = html.Div(children=[

    #input field populated by default with first row
    html.Div(children=[
        html.Label('enter values'),
        dcc.Input(id='Year', placeholder='1999', type='text'),
        dcc.Input(id='Type', placeholder='REGISTRATION', type='text'),
        dcc.Input(id='RegistrantName', placeholder='MCLEOD WATKINSON & MILLER', type='text'),
        dcc.Input(id='GeneralDescription', placeholder='Lobbying and government affairs', type='text'),
        dcc.Input(id='ClientName', placeholder='CALIFORNIA AVOCADO COMMISSION', type='text'),
        dcc.Input(id='SelfFiler', placeholder='False', type='text'),
        dcc.Input(id='IsStateOrLocalGov', placeholder='False', type='text'),
        dcc.Input(id='ClientCountry', placeholder='USA', type='text'),
        dcc.Input(id='ClientState', placeholder='CA', type='text'),
        html.div(id='Amount')
    ])
])

#callbacks - makes the input into variables
@app.callback(
    Output(component_id="Amount"),
    [Input(component_id='Year'),
     Input(component_id='Type'),
     Input(component_id='RegistrantName'),
     Input(component_id='GeneralDescription'),
     Input(component_id='ClientName'),
     Input(component_id='SelfFiler'),
     Input(component_id='IsStateOrLocalGov'),
     Input(component_id='ClientCountry'),
     Input(component_id='ClientState')]
)


#function that runs model on callback variables
def predict_cost(Year, Type, RegistrantName, GeneralDescription,
                 ClientName, SelfFiler, IsStateOrLocalGov,
                 ClientCountry, ClientState):
    cost = model.predict(float(Year),
                         str(Type),
                         str(RegistrantName),
                         str(GeneralDescription),
                         str(ClientName),
                         bool(SelfFiler),
                         bool(IsStateOrLocalGov),
                         str(ClientCountry),
                         str(ClientState)
                        )
    return "that would cost $'{}'".format(cost)


#load model
if __name__ == '__main__':
    model = joblib.load('./model.joblib')
    app.run_server(debug=True)
