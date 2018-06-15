from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

def processData(data):
    for d in data:
        d['test'] = "Cool"
    return data


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/api/test',  methods=['POST', 'OPTIONS'])
def apitest():
    if request.method == 'POST':
        data = request.json
        print(type(data))
        return jsonify({'ok': processData(data)})
    else:
        return 'ok'
