import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

DIM = 800.00
screenHeight = 500

# Intensidades da luz
lightIntensity = [0.7, 0.7, 0.7, 1.0]
lightPosition = [2.0, 6.0, 3.0, 0.0]

class Point3:
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y 
        self.z = z

class Vector3:
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y 
        self.z = z
    def set(self, x, y, z) -> None:
        self.x = x
        self.y = y 
        self.z = z

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

# Um índice de um vértice e seu vetor normal
class VertexID:
    def __init__(self) -> None:
        self.vertIndex = 0
        self.normIndex = 0

# Face contendo o conjunto de íncice e vértices
class Face:
    def __init__(self) -> None:
        self.nVerts = 0
        self.vert = [VertexID]*1000

class Mesh:
    def __init__(self) -> None:
        self.nVerts = 0
        self.numVerts = 0
        self.numNormals = 0
        self.numFaces = 0
        self.pt = [Point3(0,0,0)]*50000 # Vertices - pontos (x,y,z)
        self.face = [Face()]*50000 # Faces - objetos Face
        self.norm = [Vector3(0,0,0)]*50000 # Normal - Vetor de normais
    def addVertice(self, x, y, z):
        self.pt[self.numVerts] = Point3(x, y, z)
        self.numVerts += 1
    def addFace(self, fac, qtd):
        for f in range(qtd):
            self.face[self.numFaces].vert[f].vertIndex = fac[f]
        self.face[self.numFaces].nVerts = qtd
        self.numFaces += 1
    def getVertFace(self, f, v) -> Point3:
        vertice = Point3(0,0,0)
        ind_v = self.face[f].vert[v].vertIndex-1
        vertice.x = self.pt[ind_v].x
        vertice.y = self.pt[ind_v].y
        vertice.z = self.pt[ind_v].z
        return vertice
    def calculaNormal(self):
        a = [
            [0,0,0],
            [0,0,0],
            [0,0,0]
        ]
        vert_face = [Point3(0,0,0)]*100
        print(self.numFaces)
        for f in range(self.numFaces):
            # Vertice de cada face
            for v in range(3):
                vert_face[v] = self.getVertFace(f, v)
            # v2-v1
            for v in range(2):
                a[v][0] = vert_face[v+1].x - vert_face[v].x
                a[v][1] = vert_face[v+1].y - vert_face[v].y
                a[v][2] = vert_face[v+1].z - vert_face[v].z    
            # Matriz para calcular a determinante
            xn = a[0][1]*a[1][2] - a[0][2]*a[1][1]
            yn = a[0][2]*a[1][0] - a[0][0]*a[1][2]
            zn = a[0][0]*a[1][1] - a[0][1]*a[1][0]
            self.norm[self.numNormals].set(xn, yn, zn)
            self.numNormals += 1
        for f in range(self.numNormals):
            for v in range(self.face[f].nVerts):
                self.face[f].vert[v].normIndex = f
    def draw(self):
        glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        for f in range(self.numFaces):
            glBegin(GL_POLYGON)
            for v in range(self.face[f].nVerts):
                indexNormal = self.face[f].vert[v].normIndex
                indexVertice = self.face[f].vert[v].vertIndex-1
                glNormal3f (self.norm[indexNormal].x, self.norm[indexNormal].y, self.norm[indexNormal].z)
                glVertex3f (self.pt[indexVertice].x, self.pt[indexVertice].y, self.pt[indexVertice].z)
                # print((self.pt[indexVertice].x, self.pt[indexVertice].y, self.pt[indexVertice].z))
            glEnd()
            glFlush()

globalVertices = [
    [1, 1, 1],
    [2, 5, 10],
    [10, 3, -1],
    [2, 10, -1]
]

globalFaces = [
    [1, 2, 3],
    [1, 2, 4],
    [1, 3, 4],
    [2, 4, 3]
]

mesh = Mesh()

def initMeshObject():
    for vertex in globalVertices:
        mesh.addVertice(vertex[0], vertex[1], vertex[2])
        print(mesh.nVerts)
        for i in range(mesh.nVerts):
            print(mesh.pt[i])
    for face in globalFaces:
        mesh.addFace(face, len(face))
    mesh.calculaNormal()

def drawObject3D():
    
    glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glBegin(GL_POLYGON)
    """
    glVertex3f(50, 50, 50)
    glVertex3f(100, 250, 500)
    glVertex3f(500, 150, -50)
    glVertex3f(100, 500, -50)
    """
    for vertex in globalVertices:
        glVertex3f(vertex[0], vertex[1], vertex[2])
    glEnd()

def draw():
    glLightfv(GL_LIGHT0, GL_POSITION, lightPosition)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, lightIntensity)
    drawObject3D()

def main():
    pygame.init()
    display = (800, 800)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    #gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

    glTranslatef(0.0, 0.0, -5)
    init()
    initMeshObject()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        mesh.draw()
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
