from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/api/test",  methods=['POST', 'OPTIONS'])
def apitest():
    print(request.json)
    return jsonify({"ok": "Hello World!"})