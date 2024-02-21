import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

objectVertices = (
    (-1, 1, 1),
    (1, 1, 1),
    (1, -1, 1),
    (-1, -1, 1),
    (-1, 1, -1),
    (1, 1, -1),
    (1, -1, -1),
    (-1, -1, -1)
)

light_position = (0, 40, 50)
light_diffuse = [0.9, 0.9, 0.9, 1.0]  # Increased light intensity

rotation_speed = 0.2  # Adjust the rotation speed

def draw_cube():
    glBegin(GL_QUADS)
    for vertex in objectVertices:
        glVertex3fv(vertex)
    glEnd()

def draw_shadow_cube():
    glBegin(GL_QUADS)
    for vertex in objectVertices:
        glVertex3fv(vertex)
    glEnd()

def draw_floor():
    glBegin(GL_QUADS)
    glVertex3f(-10, -1, -10)
    glVertex3f(-10, -1, 10)
    glVertex3f(10, -1, 10)
    glVertex3f(10, -1, -10)
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_STENCIL_TEST)

    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)  # Set the diffuse component

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Get relative mouse movement
        rel_x, rel_y = pygame.mouse.get_rel()

        # Rotate the scene based on mouse movement
        glRotatef(rel_x * rotation_speed, 0, 1, 0)
        glRotatef(rel_y * rotation_speed, 1, 0, 0)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT | GL_STENCIL_BUFFER_BIT)

        # Draw floor to stencil buffer
        glEnable(GL_STENCIL_TEST)
        glStencilFunc(GL_ALWAYS, 1, 1)
        glStencilOp(GL_KEEP, GL_KEEP, GL_REPLACE)
        draw_floor()

        # Draw actual cube
        glStencilFunc(GL_EQUAL, 1, 1)
        glStencilOp(GL_KEEP, GL_KEEP, GL_KEEP)
        draw_cube()

        # Draw shadow cube
        glStencilFunc(GL_EQUAL, 0, 1)
        glStencilOp(GL_KEEP, GL_KEEP, GL_KEEP)
        draw_shadow_cube()

        glDisable(GL_STENCIL_TEST)

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
