import json
from sceneObjects import SceneObject


import math
import pygame as pg
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


from pynput.mouse import Controller

mouse = Controller()


class SceneClass:
    def __init__(self,sceneObjects,sceneMap):
        self.sceneObjects = sceneObjects
        self.sceneMap = sceneMap
        self.positions = []



    def playScene(self,animationFile,fps,loop):

        pg.init()
        display = (800, 600)
        pg.display.set_mode(display, DOUBLEBUF | OPENGL)
        clock = pg.time.Clock() 

        gluPerspective(45, (display[0] / display[1]), 0.1, 100.0)

        glTranslatef(0.0, 0, -20)

        # Load positions from the file
        self.positions = self.load_positions_from_file(animationFile)

        # Extract unique time frames
        unique_time_frames = sorted(set(entry['time'] for entry in self.positions))

        # Iterate over each time frame
        for x in range(loop):
            for time_frame in unique_time_frames:
                # Iterate over each object at the current time frame
                for entry in self.positions:
                    # print(f"Entry: {entry}, Current Time Frame: {time_frame}")
                    if entry['time'] == time_frame:
                        object_key = entry['object']
                        # print(f"Matched Object Key: {object_key}")

                        # Extract x, y, and z positions
                        x_position = entry['position']['x']
                        y_position = entry['position']['y']
                        z_position = entry['position']['z']

                        # print(f"Object Positions - X: {x_position}, Y: {y_position}, Z: {z_position}")

                        # Update the object's position using translateObject
                        self.changeObjectPosition(object_key, x_position, y_position, z_position)
                        # self.translateObject(object_key, x_position, y_position, z_position)

                clock.tick(fps)  # Adjust the frame rate (e.g., 30 frames per second)

                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        pg.quit()
                        quit()

                glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
                # glRotatef(1,mouse.position[0],mouse.position[1],0)
                # glRotatef(1,1,1,1)
                # Drawing the updated scene
                self.drawScene()

                pg.display.flip()
                pg.time.wait(10)  # Adjust the wait time if needed
    def load_positions_from_file(self, file_path):
        with open(file_path, 'r') as file:
            positions = json.load(file)
        return positions

    def translateObject(self,key,x=0,y=0,z=0):
        if key in self.sceneMap:
            self.sceneMap[key].translate(x,y,z)

    def changeObjectPositionTime(self, key, time):
        # Load positions from the file if not done already
        if not self.positions:
            self.positions = self.load_positions_from_file('positions.txt')

        # Find the position entry for the given key and time
        position_entry = next((item for item in self.positions if item['object'] == key and item['time'] == time), None)
        if position_entry is not None:
            # Extract the position data
            x = position_entry['position']['x']
            y = position_entry['position']['y']
            z = position_entry['position']['z']
            # Use the transform method to change object position
            self.sceneMap[key].transform(x, y, z)

    def changeObjectPosition(self,key,x=0,y=0,z=0):
        if key in self.sceneMap:
            self.sceneMap[key].transform(x,y,z)

    def rotateObject(self,key,rotation):
        self.sceneMap[key].rotation = rotation

    def addObject(self,key,object):
        self.sceneMap[key] = object

    def removeObject(self,key):
        self.sceneObjects.pop(key)


    def drawScene(self):
        for object in self.sceneMap.values():
            object.draw()
        return

    