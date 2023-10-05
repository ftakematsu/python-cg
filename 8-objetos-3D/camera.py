import math
from introcs import Point3
from introcs import Vector3
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Camera:
    def __init__(self) -> None:
        self.eye = Point3(0,0,0)
        self.u = Vector3()
        self.v = Vector3()
        self.n = Vector3()
        self.viewAngle = 0
        self.aspect = 0
        self.nearDist = 0
        self.farDist = 0

    def setShape(self, vAngle, asp, nr, fr):
        self.viewAngle = vAngle
        self.aspect = asp
        self.nearDist = nr
        self.farDist = fr
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        # Parametros da projeção perspectiva da visualização 3D
        gluPerspective(self.viewAngle, self.aspect, self.nearDist, self.farDist)
        glMatrixMode(GL_MODELVIEW)

    def setModelViewMatrix(self):
        # Instancia uma array de 16 posições
        m = [0]*16
        # Converte o eye em vector
        eVec = Vector3(self.eye.x, self.eye.y, self.eye.z)
        m[0] =  self.u.x
        m[4] =  self.u.y
        m[8]  =  self.u.z
        m[12] = -eVec.dot(self.u)
        m[1] =  self.v.x
        m[5] =  self.v.y
        m[9]  =  self.v.z
        m[13] = -eVec.dot(self.v)
        m[2] =  self.n.x
        m[6] =  self.n.y
        m[10] =  self.n.z
        m[14] = -eVec.dot(self.n)
        m[3] =  0
        m[7] =  0
        m[11] =  0
        m[15] = 1.0
        glMatrixMode(GL_MODELVIEW)
        glLoadMatrixf(m)

    def set(self, eye: Point3, look: Point3, up: Vector3) -> None:
        # create a modelview matrix and send it to OpenGL
        self.eye = eye # store the given eye position
        self.n = Vector3(eye.x - look.x, eye.y - look.y, eye.z - look.z) # make n
        self.u = Vector3(up.cross(self.n).x, up.cross(self.n).y, up.cross(self.n).z) # make u = up X n
        self.n.normalize()
        self.u.normalize() # make them unit length
        self.v = Vector3(self.n.cross(self.u).x, self.n.cross(self.u).y, self.n.cross(self.u).z)  # make v =  n X u
        self.setModelViewMatrix() # tell OpenGL 
    
    def slide(self, delU, delV, delN) -> None:
        self.eye.x += delU * self.u.x + delV * self.v.x + delN * self.n.x
        self.eye.y += delU * self.u.y + delV * self.v.y + delN * self.n.y
        self.eye.z += delU * self.u.z + delV * self.v.z + delN * self.n.z
        self.setModelViewMatrix()

    def roll(self, angle) -> None:
        cs = math.cos(math.pi/180.0 * angle)
        sn = math.sin(math.pi/180.0 * angle)
        t: Vector3  = self.u
        self.u = Vector3(cs*t.x - sn*self.v.x, cs*t.y - sn*self.v.y, cs*t.z - sn*self.v.z)
        self.v = Vector3(sn*t.x + cs*self.v.x, sn*t.y + cs*self.v.y, sn*t.z + cs*self.v.z)
        self.setModelViewMatrix()
        
    def pitch(self, angle) -> None:
        cs = math.cos(math.pi/180.0 * angle)
        sn = math.sin(math.pi/180.0 * angle)
        t: Vector3  = self.v
        self.v = Vector3(cs*t.x - sn*self.n.x, cs*t.y - sn*self.n.y, cs*t.z - sn*self.n.z)
        self.n = Vector3(sn*t.x + cs*self.n.x, sn*t.y + cs*self.n.y, sn*t.z + cs*self.n.z)
        self.setModelViewMatrix()
    
    def yaw(self, angle) -> None:
        cs = math.cos(math.pi/180.0 * angle)
        sn = math.sin(math.pi/180.0 * angle)
        t: Vector3  = self.n
        self.n = Vector3(cs*t.x - sn*self.u.x, cs*t.y - sn*self.u.y, cs*t.z - sn*self.u.z)
        self.u = Vector3(sn*t.x + cs*self.u.x, sn*t.y + cs*self.u.y, sn*t.z + cs*self.u.z)
        self.setModelViewMatrix()
    
    def rotate(self, axis: Vector3, angle) -> None:
        pass


