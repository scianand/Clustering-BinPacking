from bottle import Bottle, route, run, request, response, BaseRequest
from TestJson import listbhejo, calculate, count
import json
from pandas import DataFrame
app = Bottle()
BaseRequest.MEMFILE_MAX = 1024000000


def processData(data):
    df = DataFrame(data)
    bins = calculate(df)
    return bins


@app.hook('after_request')
def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/api/test', method=['OPTIONS', 'POST'])
def apitest():
    if request.method == 'POST':
        data = request.json
        print(type(data))
        print("ready to send data !")
        return {'hello': processData(data)}
    else:
        return 'ok'


app.run(port=5000, debug=True)
