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

    def transformaTexturaPadrao(self): 
        self.mat_ambient = [0.0,0.0,0.7,1.0]
        self.mat_diffuse = [0.6,0.6,0.6,1.0]
        self.mat_specular = [1.0,1.0,1.0,1.0]
        self.mat_shininess = [50.0]
        self.set()

    def transformaOuro(self):
        self.mat_ambient = [0.24725, 0.1995, 0.0745, 1.0]
        self.mat_diffuse = [0.75164, 0.60648, 0.22648, 1.0]
        self.mat_specular = [0.628281, 0.555802, 0.366065, 1.0]
        self.mat_shininess = [51.2]
        self.set()

    def transformaPrata(self):
        self.mat_ambient = [0.19225, 0.19225, 0.19225, 1.0]
        self.mat_diffuse = [0.50754, 0.50754, 0.50754, 1.0]
        self.mat_specular = [0.508273, 0.508273, 0.508273, 1.0]
        self.mat_shininess = [51.2]
        self.set()


class Light:
    def __init__(self) -> None:
        self.intensity = 0.5
        self.posX = 2.0
        # Intensidades da luz

    def aumenta(self):
        self.intensity += 0.1
    
    def diminui(self):
        self.intensity -= 0.1
    
    def posicaoX(self, valor):
        self.posX += valor

    def projetaLuz(self):
        self.lightIntensity = [self.intensity, self.intensity, self.intensity, 1.0]
        self.lightPosition = [self.posX, 6.0, 3.0, 0.0]
        glLightfv(GL_LIGHT0, GL_POSITION, self.lightPosition)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, self.lightIntensity)


class View:
    def __init__(self) -> None:
        self.camera: Camera = Camera()
        # Distância do olho (camera) com relação ao objeto
        # Quanto maior - mais distante, quanto menor - mais perto
        self.eye = Point3(500, 500, 500) 
        self.lo = Point3(0, 0, 0)
        self.up = Vector3(0, 1, 1)
        
        # Configurações da câmera
    def projetaCamera(self):
        #self.eye = Point3(self.eye.x, self.eye.y, self.eye.z)
        #self.lo = Point3(self.lo.x, self.lo.y, self.lo.z)
        self.camera.set(self.eye, self.lo, self.up)
        self.camera.setShape(10, 1, 10, 2000.0)
    
    def slide(self):
        self.camera.slide(1, 1, 1)

    def roll(self):
        self.camera.roll(1)
    
    def pitch(self):
        self.camera.pitch(1)

    def yaw(self):
        self.camera.yaw(1)

        

    
