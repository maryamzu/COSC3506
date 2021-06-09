import flask
from flask import request
import json

messages = [{"sender":"Paul", "text":"hello world"}, {}, {}]

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/messages/', methods=['GET'])
def getMessages():
    return json.dumps(messages)

@app.route('/people/', methods = ['GET'])
def getPeople():
    s = "Group members"
    return json.dumps(s)

app.run() #host = 0.0.0.0