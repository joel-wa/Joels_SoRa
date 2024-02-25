import ast
import json
from customGPTClass import CustomFunctions
import os


class GPTParser:

    def parseResponse(self,response_message):
        output = f"Parsed: {response_message}"
        cf = CustomFunctions()


        if response_message.get("function_call"):
            function_name = response_message['function_call']['name']
            function_args = response_message["function_call"]["arguments"]
            
            

            if(function_name == "createObject"):
                output = cf.createObject(function_args)
                fileName = output["objectName"]
                self.write_dict_to_txt(output,f"{fileName}.txt")
            elif (function_name == "sceneObjects"):
                output = cf.getSceneObjects(function_args)

        return f"{output}"
    
    
    def write_dict_to_txt(self,dictionary, file_path):
        
        file_path = os.path.join("./tempFiles",file_path)
        with open(file_path, 'w') as file:

            # print(dictionary)
            t = f"{dictionary}"
            file.write(t)
    
