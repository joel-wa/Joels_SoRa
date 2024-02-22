import json
import re
from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os



# Create the Flask app
app = Flask(__name__)


CORS(app)


@app.route("/",methods = ["POST","GET"])
def testServer():
    output = "Server Hi"
    return output,201


@app.route("/generateVideo",methods = ["POST","GET"])
def generateVideo():
    if(request.method == "POST"):
        data = request.get_json()
    else:
        data = "A video of a ball rolling"
    output = "Recieved"
    return output,201



@app.route("/object", methods= ["POST","GET"])
def createObject():
    if(request.method == "POST"):
        data = request.get_json()
    else:
        print("Input your prompt")
        data = input()
    output = f"Create a 3d object of {data}"
    return output,201





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)