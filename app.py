from flask import Flask, Response, make_response
from flask import request
from user_class import User
from mongohandler_class import MongoHandler
import os
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    return "Hello World!"

@app.route("/login", methods=['POST'])
def login():
    username = request.args.get('username')
    password = request.args.get('password')
    print "Username: " + str(username)
    print "Password: " + str(password)
    return make_response("Simple tagged Response")
#def get_host_ip():

if __name__ == "__main__":
    app.run(host='192.168.43.125')
