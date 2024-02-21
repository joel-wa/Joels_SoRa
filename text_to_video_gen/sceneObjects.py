from draw import CustomDraw

class SceneObject:
    def __init__(self,name,position,edges,vertices):
        self.name = name
        self.position = position
        self.edges = edges
        self.vertices = vertices
        self.x =0
        self.y =0
        self.z =0

    def draw(self):
        cd = CustomDraw()
        return cd.draw_obj(self.edges,self.vertices,self.x,self.y,self.z)
    
    def translate(self,x=0,y=0,z=0):
        self.x +=x
        self.y +=y
        self.z +=z
        