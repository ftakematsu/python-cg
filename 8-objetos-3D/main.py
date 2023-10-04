import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from mesh import *
from camera import *
import os

# Representa o diretório do projeto
ROOT_DIR = os.path.abspath(os.curdir)

# Arquivo .obj
globalObjFile = "tetraedro.obj"

# Objeto Mesh
mesh = Mesh()

# Camera
camera = Camera()

DIM = 500.00
screenHeight = 400

# Intensidades da luz
lightIntensity = [0.7, 0.7, 0.7, 1.0]
lightPosition = [2.0, 6.0, 3.0, 0.0]

def defineTextura():
    mat_ambient = [0.0,0.0,0.7,1.0]
    mat_diffuse = [0.6,0.6,0.6,1.0]
    mat_specular = [1.0,1.0,1.0,1.0]
    mat_shininess = [50.0]
    glMaterialfv(GL_FRONT,GL_AMBIENT,mat_ambient)
    glMaterialfv(GL_FRONT,GL_DIFFUSE,mat_diffuse)
    glMaterialfv(GL_FRONT,GL_SPECULAR,mat_specular)
    glMaterialfv(GL_FRONT,GL_SHININESS,mat_shininess)

def defineTexturaOuro():
    mat_ambient = [0.24725, 0.1995, 0.0745, 1.0]
    mat_diffuse = [0.75164, 0.60648, 0.22648, 1.0]
    mat_specular = [0.628281, 0.555802, 0.366065, 1.0]
    mat_shininess = [51.2]
    glMaterialfv(GL_FRONT,GL_AMBIENT,mat_ambient)
    glMaterialfv(GL_FRONT,GL_DIFFUSE,mat_diffuse)
    glMaterialfv(GL_FRONT,GL_SPECULAR,mat_specular)
    glMaterialfv(GL_FRONT,GL_SHININESS,mat_shininess)



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

def definirObjetoSimples():
    vertices = [
        [0, 0, 0],
        [10, 0, 0],
        [10, 10, 10],
        [0, 10, 10]
    ]
    faces = [
        [1, 2, 3, 4]
    ]
    return (vertices, faces)

def definirTetraetro():
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
    return (vertices, faces)

def definirCubo():
    vertices = [
        [-40, -40, 40],
        [40, -40, 40],
        [40, 40, 40],
        [-40, 40, 40],
        [-40 ,-40, -40],
        [40, -40, -40],
        [40, 40, -40],
        [-40 ,40 ,-40]
    ]
    faces = [
        [1 ,2, 3, 4],
        [6, 5, 8, 7],
        [4, 3, 7, 8],
        [2, 1, 5, 6],
        [5, 1, 4, 8],
        [2, 6, 7, 3]
    ]
    return (vertices, faces)

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
    #(vertices, faces) = definirCubo()
    #(vertices, faces) = definirTetraetro()
    #(vertices, faces) = definirObjetoSimples()
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
    eye = Point3(50,50,50)
    lo = Point3(0,0,0)
    up = Vector3(0,1,1)
    # Configurações da câmera
    camera.set(eye,lo,up)
    camera.setShape(30, 1, 10, 100.0)
    camera.slide(0,0,2)
    # Configurações de textura e iluminação
    defineTexturaOuro()
    glLightfv(GL_LIGHT0, GL_POSITION, lightPosition)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, lightIntensity)
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
    glScalef(6, 6, 6)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print("LEFT")
                if event.key == pygame.K_RIGHT:
                    print("RIGHT")
        #camera.slide(1,0,1)
        #glRotatef(1, 3, 1, 1)
        #glTranslatef(0, 0, 0)
        draw()
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
