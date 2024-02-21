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


# scene.addObject("cube",so)
# scene.addObject("gun",gun)

obj = util.read_object_data(r"objectFiles\objectFile.txt")
scene.addObject(obj.name,obj)

# obj util.read_object_data("")


if __name__ == "__main__":
    # main()
    # scene.playScene(r"animationFiles\triangleAnim.txt",20,30)
    scene.playScene(r"animationFiles\positions.txt",40,10)






# scene.transformObject("sphere",mouse.position[0]/30 -20,-mouse.position[1]/20 +20)
# scene.transformObject("sphere",-10)
    
