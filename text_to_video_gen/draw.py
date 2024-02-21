import math
import pygame as pg
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *





class CustomDraw:
        
    def draw_obj(self,edges,vertices,x,y,z):
        objectColor = (0.8, 0.2, 0.2)
        glColor3fv(objectColor)
        glBegin(GL_LINES)
        for edge in edges:
            for vertex in edge:
                rotated = (vertices[vertex][0]+x,vertices[vertex][1]+y,vertices[vertex][2]+z)
                glVertex3fv(rotated)
        glEnd()

    def draw_shadow_cube(self,objectVertices):
        glColor3f(0, 0, 0)  # Color the shadow black
        glBegin(GL_QUADS)
        for vertex in objectVertices:
            glVertex3fv(vertex)
        glEnd()
        pass

    def generate_sphere_vertices(self,radius, num_latitude, num_longitude):
        vertices = []
        for i in range(num_latitude + 1):
            theta = (i / num_latitude) * math.pi
            for j in range(num_longitude):
                phi = (j / num_longitude) * (2 * math.pi)
                x = radius * math.sin(theta) * math.cos(phi)
                y = radius * math.cos(theta)
                z = radius * math.sin(theta) * math.sin(phi)
                vertices.append((x, y, z))
        return vertices