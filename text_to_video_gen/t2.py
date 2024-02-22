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
import os



sceneObjectFile = "scene2.txt"
animationFile = "positions.txt"
animationFPS = 60
loop = 100

#First request the AI to generate the vertices of the objects in the given scene.
#save it to a file.
util = UtilClass()
scene = SceneClass([],{})
draw = CustomDraw()


# objectFile_path = os.path.join("./objectFiles","objectFile.txt")


#Below is the old implementation to add single objects from single files to a scene.
# obj = util.read_object_data(r"objectFiles\square pyramid.txt")
# obj = util.read_object_data(r"objectFiles\objectFile.txt")

# obj = util.read_object_data(objectFile_path)
# scene.addObject(obj.name,obj)


#New Implementation: Just state the location of the file containing the objects you want in the scene
#and they will be loaded into the scene automatically.
sceneObectFilePath = os.path.join("./objectFiles",sceneObjectFile)

scene.addAllObjects(sceneObectFilePath)


if __name__ == "__main__":
    animationFile_path = os.path.join("./animationFiles",animationFile)
    
    scene.playScene(animationFile_path, animationFPS,loop)