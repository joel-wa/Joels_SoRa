import json
from scene import SceneClass
from sceneObjects import SceneObject
from util import UtilClass
from draw import CustomDraw

from pynput.mouse import Controller

mouse = Controller()

import math
import pygame as pg
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *



#First request the AI to generate the vertices of the objects in the given scene.
#save it to a file.
util = UtilClass()
scene = SceneClass([],{})
draw = CustomDraw()


num_latitude = 20
num_longitude = 40

sv = draw.generate_sphere_vertices(2,num_latitude,num_longitude)

sphere_edges = []
for i in range(num_latitude):
    for j in range(num_longitude):
        current = i * num_longitude + j
        next_row = (i + 1) % (num_latitude + 1) * num_longitude + j
        next_col = i * num_longitude + (j + 1) % num_longitude
        sphere_edges.extend([(current, next_row), (current, next_col)])




sphere = SceneObject("sphere",0,sphere_edges,sv)


scene.addObject("triangle",sphere)
# scene.addObject("cube",so)
# scene.addObject("gun",gun)

# obj = util.read_object_data(r"objectFiles\gunobj.txt")
# scene.addObject(obj.name,obj)

# obj util.read_object_data("")

def load(file_path):
        
    with open(file_path, 'r') as file:
        loaded_positions = json.load(file)
        return loaded_positions


if __name__ == "__main__":
    # main()
    scene.playScene(r"animationFiles\triangleAnim.txt",20,30)
    # scene.playScene("positions.txt",40,10)






# scene.transformObject("sphere",mouse.position[0]/30 -20,-mouse.position[1]/20 +20)
# scene.transformObject("sphere",-10)
    
