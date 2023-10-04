import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from mesh import *
from config import *
import os

# Representa o diretório do projeto
ROOT_DIR = os.path.abspath(os.curdir)

# Arquivo .obj
globalObjFile = "Peixe.obj"

# Objeto Mesh
mesh = Mesh()

# Textura
texture = Texture()

# Luz
light = Light()

# Camera
view = View()

DIM = 700.00
screenHeight = 400



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

vertices = []
faces = []

def readObjFile(file):
    vertices = []
    faces = []
    filePathName = ROOT_DIR + "\\8-objetos-3D\\objects\\" + file
    print("Lendo o arquivo: " + filePathName)
    # Leitura do arquivo
    with open(filePathName) as f:
        for line in f:
            # Remove os espaços desnecessários da string
            linhasSplit = line.split()
            if (linhasSplit[0]=='v'):
                linhasSplit.pop(0) # Remover o primeiro item
                #print("Adicionando vertice")
                vet = list(map(lambda x:float(x), linhasSplit))
                #print(vet)
                vertices.append(vet)
            elif (linhasSplit[0]=='f'):
                linhasSplit.pop(0) # Remove o primeiro item
                #print("Adicionando face")
                vet = list(map(lambda x:int(x), linhasSplit))
                #print(vet)
                faces.append(vet)
            # v.pop(0)
            # list(map(lambda x:int(x), v))
    return (vertices, faces)

def initMeshObject(objFile):
    (vertices, faces) = readObjFile(objFile)
    for vertex in vertices:
        mesh.addVertice(vertex[0], vertex[1], vertex[2])
    for face in faces:
        mesh.addFace(face, len(face))
    mesh.calculaNormal()
    #mesh.printVertices()
    #mesh.printFaces()
    #mesh.printNormals()

def drawObject3D():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glBegin(GL_POLYGON)
    for vertex in vertices:
        glVertex3f(vertex[0], vertex[1], vertex[2])
    glEnd()

def draw():
    #defineTextura()
    # Configurações de textura e iluminação
    light.projetaLuz()
    view.projetaCamera()
    # Desenho do objeto
    mesh.draw()

'''
Programa principal
'''
def main():
    global globalObjFile
    pygame.init()
    display = (DIM, DIM)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    #gluPerspective(45, display[0]/display[1], 1.1, 1.0)
    #glTranslatef(0.0, 0.0, -5)
    init()
    initMeshObject(globalObjFile)
    #glScalef(6, 6, 6)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t:
                    texture.transformaTexturaPadrao()
                if event.key == pygame.K_o:
                    texture.transformaOuro()
                if event.key == pygame.K_p:
                    texture.transformaPrata()
                if event.key == pygame.K_KP_PLUS:
                    light.aumenta()
                if event.key == pygame.K_KP_MINUS:
                    light.diminui()
                if event.key == pygame.K_KP_MULTIPLY:
                    light.posicaoX(1)
                if event.key == pygame.K_KP_DIVIDE:
                    light.posicaoX(-1)
        #camera.slide(1,0,1)
        #glRotatef(1, 3, 1, 1)
        #glTranslatef(0, 0, 0)
        draw()
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
