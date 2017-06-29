from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    return "Hello World!"

@app.route("/login/", methods=['GET', 'POST'])
def login():
    username = request.args.get('username')
    password = request.args.get('password')
