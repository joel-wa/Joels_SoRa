import math
import pygame as pg
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


from draw import CustomDraw

draw = CustomDraw()

cubeVertices = ((1, 1, 1), (1, 1, -1), (1, -1, -1), (1, -1, 1), (-1, 1, 1), (-1, -1, -1), (-1, -1, 1), (-1, 1, -1))
cubeEdges = ((0, 1), (0, 3), (0, 4), (1, 2), (1, 7), (2, 5), (2, 3), (3, 6), (4, 6), (4, 7), (5, 6), (5, 7))
cubeQuads = ((0, 3, 6, 4), (2, 5, 6, 3), (1, 2, 5, 7), (1, 0, 4, 7), (7, 4, 6, 5), (2, 3, 0, 1))



pyramidVertices = ((1, 1, -1), (1, 1, 1), (-1, 1, 1), (-1, 1, -1), (0, -1, 0))
pyramidEdges = ((0, 1), (1, 2), (2, 3), (3, 0), (0, 4), (1, 4), (2, 4), (3, 4))


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




# sphere = SceneObject("sphere",0,sphere_edges,sv)


# scene.addObject("triangle",sphere)


carVertices = (
    (1, 0, 0),      # Vertex 0 - Front right
    (1, 0, -1),     # Vertex 1 - Front left
    (-1, 0, -1),    # Vertex 2 - Back left
    (-1, 0, 0),     # Vertex 3 - Back right
    (1, 0.5, 0),    # Vertex 4 - Roof front right
    (1, 0.5, -1),   # Vertex 5 - Roof front left
    (-1, 0.5, -1),  # Vertex 6 - Roof back left
    (-1, 0.5, 0),   # Vertex 7 - Roof back right

    (0.6, 0.6, 0.25),    # Vertex 8 - Cube bottom front right
    (0.6, 0.6, -0.25),   # Vertex 9 - Cube bottom front left
    (-0.6, 0.6, -0.25),  # Vertex 10 - Cube bottom back left
    (-0.6, 0.6, 0.25),   # Vertex 11 - Cube bottom back right
    (0.6, 0.75, 0.25),   # Vertex 12 - Cube top front right
    (0.6, 0.75, -0.25),  # Vertex 13 - Cube top front left
    (-0.6, 0.75, -0.25), # Vertex 14 - Cube top back left
    (-0.6, 0.75, 0.25)   # Vertex 15 - Cube top back right
)

carEdges = (
    (0, 1), (1, 2), (2, 3), (3, 0),  # Bottom of the car
    (0, 4), (1, 5), (2, 6), (3, 7),  # Connect bottom to roof
    (4, 5), (5, 6), (6, 7), (7, 4),  # Roof
    # (0, 8), (1, 9), (2, 10), (3, 11), # Connect bottom to cube
    # (4, 12), (5, 13), (6, 14), (7, 15), # Connect roof to cube
    (8, 9), (9, 10), (10, 11), (11, 8),  # Cube bottom
    (12, 13), (13, 14), (14, 15), (15, 12),  # Cube top
    (8, 12), (9, 13), (10, 14), (11, 15)  # Connect cube bottom to top
)







cube_x_position = 0.0
pyramid_x_position = 0.0

angles = (0,0,0)

depth = 7

import math


def rotate_point(point, angles):
    global depth
    x, y, z = point
    angle_x, angle_y, angle_z = math.radians(angles[0]), math.radians(angles[1]), math.radians(angles[2])

    # Rotate around X-axis
    new_y_x = y * math.cos(angle_x) - z * math.sin(angle_x)
    new_z_x = y * math.sin(angle_x) + z * math.cos(angle_x)

    # Rotate around Y-axis
    new_x_y = x * math.cos(angle_y) + z * math.sin(angle_y)
    new_z_y = -x * math.sin(angle_y) + z * math.cos(angle_y)

    # Rotate around Z-axis
    new_x_z = x * math.cos(angle_z) - y * math.sin(angle_z)
    new_y_z = x * math.sin(angle_z) + y * math.cos(angle_z)

    # Apply perspective scaling based on distance from viewer
     # Adjust this value based on your scene
    scale_factor = depth / (depth + new_z_y)

    return new_x_y * scale_factor, new_y_x * scale_factor, new_z_x * scale_factor



# def rotate_point(point, angles):
#     x, y, z = point
#     angle_x, angle_y, angle_z = math.radians(angles[0]), math.radians(angles[1]), math.radians(angles[2])

#     # Apply rotation around X-axis
#     new_y_x = y * math.cos(angle_x) - z * math.sin(angle_x)
#     new_z_x = y * math.sin(angle_x) + z * math.cos(angle_x)

#     # Apply rotation around Y-axis
#     new_x_y = x * math.cos(angle_y) + z * math.sin(angle_y)
#     new_z_y = -x * math.sin(angle_y) + z * math.cos(angle_y)

#     # Apply rotation around Z-axis
#     new_x_z = x * math.cos(angle_z) - y * math.sin(angle_z)
#     new_y_z = x * math.sin(angle_z) + y * math.cos(angle_z)

#     # Combine the results
#     new_x = new_x_y + new_x_z
#     new_y = new_y_x + new_y_z
#     new_z = new_z_x + new_z_y

#     # Normalize the vector
#     length = math.sqrt(new_x**2 + new_y**2 + new_z**2)
#     new_x /= length
#     new_y /= length
#     new_z /= length

#     return new_x, new_y, new_z



def draw_pyramid():
    global angles  # Assuming angles is a global variable or some way to store the rotation angles

    glBegin(GL_LINES)
    for edge in pyramidEdges:
        for vertex in edge:
            rotated_vertex = rotate_point(pyramidVertices[vertex], angles)
            glVertex3fv(rotated_vertex)
    glEnd()

    # Update angles for continuous rotation
    angles = (angles[0], angles[1]+1, angles[2]+1)



def wireCube():
    glBegin(GL_LINES)
    for cubeEdge in cubeEdges:
        for cubeVertex in cubeEdge:
            glVertex3fv((cubeVertices[cubeVertex][0], cubeVertices[cubeVertex][1],
                         cubeVertices[cubeVertex][2]))
    glEnd()



def draw_obj(edges,vertices):
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            rotated = vertices[vertex]
            glVertex3fv(rotated)
    glEnd()

    # angles = (angles[0], angles[1], angles[2])


# def draw_obj(edges, vertices):
#     glBegin(GL_LINES)
#     for edge in edges:
#         for vertex in edge:
#             glVertex3fv(vertices[vertex])
#     glEnd()



def main():
    global cube_x_position, pyramid_x_position

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

        # glRotatef(1,0.5,0,0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        cube_x_position += 0.03  # Move the cube to the right
        pyramid_x_position -= 0.03  # Move the pyramid to the left

        # glPushMatrix()
        # wireCube()
        #draw cube
        # draw_obj(cubeEdges,cubeVertices)
        # wireCube()
        # draw_pyramid()
        draw_obj(sphere_edges,sv)
        # glPopMatrix()
        
        #draw pyramid
        # draw_obj(carEdges,carVertices)
        # draw_obj(cubeEdges,cubeVertices)
        # draw_car()

        pg.display.flip()
        pg.time.wait(10)

if __name__ == "__main__":
    print(f"Edges: {sphere_edges}")
    print(f"Vert: {sv}")
    main()
