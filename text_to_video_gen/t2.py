from scene import SceneClass
from sceneObjects import SceneObject
from util import UtilClass
from draw import CustomDraw


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

a,b = util.read_shape_data(r"C:\Users\RanVic\OneDrive\Documents\GitHub\Joels_SoRa\sphere.txt")

so  = SceneObject("cube",0,a,b)

print(a)
print(b)

# scene.addObject("cube",so)



num_latitude = 10
num_longitude = 10

sv = draw.generate_sphere_vertices(2,num_latitude,num_longitude)

sphere_edges = []
for i in range(num_latitude):
    for j in range(num_longitude):
        current = i * num_longitude + j
        next_row = (i + 1) % (num_latitude + 1) * num_longitude + j
        next_col = i * num_longitude + (j + 1) % num_longitude
        sphere_edges.extend([(current, next_row), (current, next_col)])


sphere = SceneObject("sphere",0,sphere_edges,sv)

scene.addObject("sphere",sphere)
scene.addObject("cube",so)

# scene.removeObject("cube")
movement = [-1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,-0.5,0,0,0,0,0,0,0,0,0,0,0,0,0.5,0,0,0,0,0,0,0,0,0,0]
mi =0

def main():
    global cube_x_position, pyramid_x_position,mi,movement

    pg.init()
    display = (800, 600)
    pg.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

    glTranslatef(0.0, 0, -10)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
        
        if mi == len(movement)-1:
            mi = 0
        else:
            mi +=1

        # glRotatef(1,0.5,0,0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)


        scene.translateObject("sphere",0.05)
        scene.translateObject("cube",-0.05)

        
        scene.drawScene()
        pg.display.flip()
        pg.time.wait(10)

if __name__ == "__main__":
    main()