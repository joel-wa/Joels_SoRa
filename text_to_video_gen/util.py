import json
import os
from scene import SceneObject

class UtilClass:
                            
    def read_shape_data(self,file_path):
        with open(file_path, 'r') as file:
            content = file.read()

        edges_text = content.split("*")[0].strip()
        vertices_text = content.split("*")[1].strip()
        
        # print(edges_text)
        # print(vertices_text)
        vertices = eval(vertices_text)
        edges = eval(edges_text)

        return vertices, edges
    
    def readTimeFrameFromFile(self,file_path):
        with open(file_path, 'r') as file:
            return [json.loads(line) for line in file]
        

        
    def read_object_data(self,file_path):
        with open(file_path, 'r') as file:
            data = file.read()

        # Evaluate the data as Python code to get the variables
        obj_variables = {}
        exec(data, globals(), obj_variables)
        
        # Create a SceneObject using the obtained variables
        scene_object = SceneObject(obj_variables['objectName'],0, obj_variables['objectEdges'], obj_variables['objectVertices'])
    
        return scene_object
    

    def write_dict_to_txt(self,dictionary, file_path):
        file_path = os.path.join("./buffer",file_path)
        with open(file_path, 'w') as file:

            # print(dictionary)
            t = f"{dictionary}"
            file.write(t)


