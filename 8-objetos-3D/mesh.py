from introcs import Point3
from introcs import Vector3
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Um índice de um vértice e seu vetor normal
class VertexID:
    def __init__(self, vi, ni) -> None:
        self.vertIndex = vi
        self.normIndex = ni

# Face contendo o conjunto de íncice e vértices
class Face:
    def __init__(self) -> None:
        self.nVerts = 0
        self.vert = [VertexID(0,0)]*1000
    def printFace(self) -> str:
        for n in range(self.nVerts):
            print(f"vertIndex[{n}]={self.vert[n].vertIndex} normIndex={self.vert[n].normIndex}") # 
        

class Mesh:
    def __init__(self) -> None:
        self.numVerts = 0
        self.numNormals = 0
        self.numFaces = 0
        self.pt = [Point3(0,0,0)]*50000 # Vertices - pontos (x,y,z)
        self.face = [Face()]*50000 # Faces - objetos Face
        self.norm = [Vector3(0,0,0)]*50000 # Normal - Vetor de normais
    
    def printVertices(self):
        print(f"Vertices: {self.numVerts}")
        for i in range(self.numVerts):
            print(self.pt[i])
    
    def printFaces(self):
        print(f"Faces: {self.numFaces}")
        for i in range(self.numFaces):
            print(f"\nFace {i}:")
            self.face[i].printFace()
        print()
    
    def printNormals(self):
        print(f"Normals: {self.numNormals}")
        for i in range(self.numNormals):
            print(self.norm[i])

    def addVertice(self, x, y, z):
        self.pt[self.numVerts] = Point3(x, y, z)
        self.numVerts += 1
    
    def addFace(self, fac, qtd):
        # print(f"FACE {self.numFaces}")
        self.face[self.numFaces] = Face()
        for f in range(qtd):
            # print(f"Adicionando em {f}: {fac[f]}")
            self.face[self.numFaces].vert[f] = VertexID(0, 0)
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
        # print(f"Calculando normal para {self.numFaces} faces")
        for f in range(self.numFaces):
            for v in range(3):
                vert_face[v] = Point3()
                vert_face[v] = self.getVertFace(f, v)
                # print(f"VertFace {v}: {vert_face[v]}")
            # Calcula V2-V1
            for v in range(2):
                a[v][0] = vert_face[v+1].x - vert_face[v].x
                a[v][1] = vert_face[v+1].y - vert_face[v].y
                a[v][2] = vert_face[v+1].z - vert_face[v].z
            # Calculando a normal através da determinante da matriz
            xn = a[0][1]*a[1][2] - a[0][2]*a[1][1]
            yn = a[0][2]*a[1][0] - a[0][0]*a[1][2]
            zn = a[0][0]*a[1][1] - a[0][1]*a[1][0]
            self.norm[self.numNormals] = Vector3()
            self.norm[self.numNormals].x = xn
            self.norm[self.numNormals].y = yn
            self.norm[self.numNormals].z = zn
            #print(f"Normal calculado para {self.numNormals}: {xn} {yn} {zn}")
            self.numNormals+=1
        # Associando normais ao vertice
        for f in range(self.numNormals):
            for v in range(self.face[f].nVerts):
                #print(f"Adicionando Normal Index em {v}: {f}")
                self.face[f].vert[v] = VertexID(self.face[f].vert[v].vertIndex, f)
                #self.face[f].vert[v].normIndex = f
        
    def draw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        #print(f"QTD FACES: {self.numFaces}")
        for f in range(self.numFaces):
            glBegin(GL_POLYGON)
            #print(f"\n* FACE {f}")
            for v in range(self.face[f].nVerts):
                normalIndex = self.face[f].vert[v].normIndex
                vertexIndex = self.face[f].vert[v].vertIndex-1
                glNormal3f(self.norm[normalIndex].x, self.norm[normalIndex].y, self.norm[normalIndex].z )
                glVertex3f(self.pt[vertexIndex].x, self.pt[vertexIndex].y, self.pt[vertexIndex].z )
            glEnd()
            glFlush()
