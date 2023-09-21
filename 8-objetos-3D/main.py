import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from mesh import *

DIM = 800.00
screenHeight = 500

# Intensidades da luz
lightIntensity = [0.7, 0.7, 0.7, 1.0]
lightPosition = [2.0, 6.0, 3.0, 0.0]



def init():
    glClearColor(1.0, 1.0, 1.0, 0.0)  # Define a cor de fundo 
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_NORMALIZE)
    glMatrixMode(GL_PROJECTION)
    glOrtho( -DIM, DIM, -DIM, DIM, -DIM, DIM )
    glClear(GL_COLOR_BUFFER_BIT)

"""
v 1 1 1
v 2 5 10
v 10 3 -1
v 2 10 -1
f 1 2 3
f 1 2 4
f 1 3 4
f 2 4 3
"""


vertices = [
    [10, 10, 10],
    [20, 50, 100],
    [100, 30, -10],
    [20, 100, -10]
]

faces = [
    [1, 2, 3],
    [1, 2, 4],
    [1, 3, 4],
    [2, 4, 3]
]

mesh = Mesh()

def initMeshObject():
    for vertex in vertices:
        mesh.addVertice(vertex[0], vertex[1], vertex[2])
        print(f"vert {vertex[0]} {vertex[1]} {vertex[2]}")
    for face in faces:
        print(f"Adding face {len(face)}: {face}")
        mesh.addFace(face, len(face))
    mesh.calculaNormal()
    mesh.printVertices()
    mesh.printFaces()
    mesh.printNormals()

def drawObject3D():
    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glBegin(GL_POLYGON)
    """
    glVertex3f(50, 50, 50)
    glVertex3f(100, 250, 500)
    glVertex3f(500, 150, -50)
    glVertex3f(100, 500, -50)
    """
    for vertex in vertices:
        glVertex3f(vertex[0], vertex[1], vertex[2])
    glEnd()

def draw():
    #glLightfv(GL_LIGHT0, GL_POSITION, lightPosition)
    #glLightfv(GL_LIGHT0, GL_DIFFUSE, lightIntensity)
    mesh.draw()

def main():
    pygame.init()
    display = (800, 800)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    #gluPerspective(45, display[0]/display[1], 1.1, 1.0)

    glTranslatef(0.0, 0.0, -5)
    init()
    initMeshObject()
    glScalef(3, 3, 3)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        #glTranslatef(0, 0, -10)
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw()
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
