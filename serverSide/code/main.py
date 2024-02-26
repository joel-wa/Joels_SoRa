import json
import re
from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os
from customGPTClass import CustomGPT,CustomFunctions
from gptParser import GPTParser
from util import CustomUtil



util =CustomUtil()


openai.api_key = util.openAIToken()

gpt = CustomGPT()
gptFunctions = CustomFunctions()
gptParser = GPTParser()


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
        data = "a square pyramid"


    systemPrompt= "Create a 3d object details of the given object making sure all values are whole numbers and not decimals "

    #check if object is in buffer
    if(util.checkObjectBuffer(data)):
        print(f"Obejct in buffer {data}")
        with open(f"./tempFiles/{data}.txt",mode="r") as file:
            info = file.read()
        return info,201
    else:
        print("Not in buffer")


    functions = util.loadAllFunctionFromSchema(["serverSide\gptFunctions\objectSchema.csv"])

    output = gpt.chatAI(data,systemPrompt,functions)

    value = gptParser.parseResponse(output)
    return f"{value}",201



@app.route("/sceneObjects",methods = ["POST","GET"])
def getSceneObjects():
    if(request.method == "POST"):
        data = request.get_json()
    else:
        # print("Input your prompt")
        data = "a ball rolling "
    systemPrompt = "You will be given a scene, extract the various objects needed for the scene.Eg, for 'A ball rolling', we will get 'Ball,Floor'"
    
    functions = util.loadAllFunctionFromSchema(["serverSide\gptFunctions\sceneObjectGeneratorSchema.csv"])

    output = gpt.chatAI(data,systemPrompt,functions)
    value = gptParser.parseResponse(output)
    return f"{value}",201

 

@app.route("/animate",methods = ["POST","GET"])
def animateScene():
    if(request.method == "POST"):
        data = request.get_json()
    else:
        data = "Objects:Ball,Floor, Animation: A ball rolling"

    systemPrompt = "Given the following objects, create an animation script for the objects to match the animation"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)