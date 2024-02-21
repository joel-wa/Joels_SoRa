import json


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


