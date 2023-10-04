from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from camera import *

class Texture:
    def __init__(self):
        self.mat_ambient = [0.0,0.0,0.7,1.0]
        self.mat_diffuse = [0.6,0.6,0.6,1.0]
        self.mat_specular = [1.0,1.0,1.0,1.0]
        self.mat_shininess = [50.0]
    
    def set(self):
        glMaterialfv(GL_FRONT,GL_AMBIENT, self.mat_ambient)
        glMaterialfv(GL_FRONT,GL_DIFFUSE, self.mat_diffuse)
        glMaterialfv(GL_FRONT,GL_SPECULAR, self.mat_specular)
        glMaterialfv(GL_FRONT,GL_SHININESS, self.mat_shininess)

    def defineTexturaPadrao(self): 
        self.mat_ambient = [0.0,0.0,0.7,1.0]
        self.mat_diffuse = [0.6,0.6,0.6,1.0]
        self.mat_specular = [1.0,1.0,1.0,1.0]
        self.mat_shininess = [50.0]
        self.set()

    def defineTexturaOuro(self):
        self.mat_ambient = [0.24725, 0.1995, 0.0745, 1.0]
        self.mat_diffuse = [0.75164, 0.60648, 0.22648, 1.0]
        self.mat_specular = [0.628281, 0.555802, 0.366065, 1.0]
        self.mat_shininess = [51.2]
        self.set()


class Light:
    def __init__(self) -> None:
        # Intensidades da luz
        self.lightIntensity = [0.7, 0.7, 0.7, 1.0]
        self.lightPosition = [2.0, 6.0, 3.0, 0.0]
    
    def projetaLuz(self):
        glLightfv(GL_LIGHT0, GL_POSITION, self.lightPosition)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, self.lightIntensity)


class View:
    def __init__(self) -> None:
        self.camera: Camera = Camera()
        self.eye = Point3(50, 50, 50)
        self.lo = Point3(0, 0, 0)
        self.up = Vector3(0, 1, 1)
        # Configurações da câmera
    def projetaCamera(self):
        self.camera.set(self.eye, self.lo, self.up)
        self.camera.setShape(30, 1, 10, 100.0)
        #self.camera.slide(0, 0, 2)

    
