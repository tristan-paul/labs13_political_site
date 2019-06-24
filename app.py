import os
import dash
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
        dcc.Input(id='Year', placeholder='2008', type='text'),
        dcc.Input(id='Type', placeholder='4th Quarter', type='text'),
        dcc.Input(id='RegistrantName', placeholder='Ogilvy Government Relations', type='text'),
        dcc.Input(id='GeneralDescription', placeholder='Lobbying', type='text'),
        dcc.Input(id='ClientName', placeholder='At&t', type='text'),
        dcc.Input(id='SelfFiler', placeholder='0', type='text'),
        dcc.Input(id='IsStateOrLocalGov', placeholder='0', type='text'),
        dcc.Input(id='ClientCountry', placeholder='Other', type='text'),
        dcc.Input(id='ClientState', placeholder='Outside US', type='text'),
        html.Button('predict', id='button'),
        html.Div(id='Amount')
    ])
])

#callback - button
@app.callback(
Output('button-clicks', 'children'),
[Input('button', 'n_clicks')]
)

#callbacks - makes the input into variables
@app.callback(
    Output(component_id="Amount", component_property='children'),
    [Input('button', 'n_clicks')],
    state = [State(component_id='Year', component_property='value'),
     State(component_id='Type', component_property='value'),
     State(component_id='RegistrantName', component_property='value'),
     State(component_id='GeneralDescription', component_property='value'),
     State(component_id='ClientName', component_property='value'),
     State(component_id='SelfFiler', component_property='value'),
     State(component_id='IsStateOrLocalGov', component_property='value'),
     State(component_id='ClientCountry', component_property='value'),
     State(component_id='ClientState', component_property='value')]
)


#function that runs model on callback variables
def predict_cost(n_clicks, Year, Type, RegistrantName,
                 GeneralDescription, ClientName, SelfFiler,
                 IsStateOrLocalGov, ClientCountry, ClientState):
    cost = model.predict(int(Year),
                         str(Type),
                         str(RegistrantName),
                         str(GeneralDescription),
                         str(ClientName),
                         int(SelfFiler),
                         int(IsStateOrLocalGov),
                         str(ClientCountry),
                         str(ClientState)
                        )
    return "that would cost $'{}'".format(cost)


#load model
if __name__ == '__main__':
    model = joblib.load('./model.joblib')
    app.run_server(debug=True)
