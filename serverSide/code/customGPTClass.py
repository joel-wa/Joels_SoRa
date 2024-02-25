import ast
import json
import math
import openai


class CustomGPT:

    # def __init__(self):
    #     self.apiKey = apiKey

    def chatAI(self,user_prompt,system_prompt,functions =[]):
        
        response = openai.ChatCompletion.create(
        model="gpt-4-turbo-preview",
        messages = [{"role":"system","content":system_prompt},{"role": "user", "content": user_prompt}],
        functions=functions,
        function_call="auto",  # auto is default, but we'll be explicit
        )
        response_message = (response["choices"][0]["message"])
        print(response)
        
        return response_message



    
class CustomFunctions:
    createObjectFunction = {'name': 'createObject', 'description': 'function to create a 3d object from a given prompt where and all values are integers', 'parameters': {'type': 'object', 'properties': {'objectName': {'type': 'string', 'description': 'the name of the object'}, 'objectVertices': {'type': 'string', 'description': 'the ordered tuples of vertices of the object in 3d space. Must be in python format'}, 'objectEdges': {'type': 'string', 'description': 'the ordered tuples of thee edges details of the object in space. Must be in python tuple format.'}}}, 'required': ['objectName', 'objectVertices', 'objectEdges']}



    def createObject(self,json_data):
        data = json.loads(json_data)

        objectName = data["objectName"]
        edges = self.convert_string_to_tuple(data["objectEdges"])
        verts = self.convert_string_to_tuple(data["objectVertices"])
        # print("edges are")


        objectMap = {
            "objectName":objectName,
            "objectEdges":edges,
            "objectVertices":verts,
        }

        return objectMap
    

    def getSceneObjects(self,json_data):
        data = json.loads(json_data)

        objectList = data["objectList"]
        objLists = objectList.split(",")
        print(objLists)
        return objLists


    def convert_string_to_tuple(self,input_string):
        # Remove the outer square brackets and split the string into pairs
        pairs_str = input_string.strip('[]')
        pairs_list = pairs_str.split('), ')
        print("input is")
        print(input_string)

        mainTuple = ()
        for pair in pairs_list:
            pair=pair.split(",")
            
            pair[0] = pair[0].split("(")[1]
            # print(pair)
            lists = []
            customTuple = ()
            for value in pair:
                value = value.strip(")")

                v = int(value)
                # v = math.ceil(v)
                # print(v)
                lists.append(v)
                customTuple = customTuple + (v,)
            # print(customTuple)
            mainTuple = mainTuple + (customTuple,)

        print(mainTuple)
        return mainTuple