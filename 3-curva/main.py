import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

def init():
    glClearColor(1.0, 1.0, 1.0, 0.0)  # Define a cor de fundo 
    glPointSize(4.0) # Define a espessura do ponto
    glLineWidth(2.0) # Define a espessura da linha

def setWindow(left,right,bottom,top):
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(left,right,bottom,top)

def setViewport(left, right, bottom, top):
    glViewport(left, bottom, right-left, top-bottom)

def drawPoints():
    #glBegin(GL_POINTS)
    #glBegin(GL_POLYGON)
    #glBegin(GL_LINES)
    #glBegin(GL_QUADS)
    glPointSize(4.0) # Espessura do ponto
    glBegin(GL_POINTS)
    glColor3f(0.0, 0.0, 1.0)  # Define a cor do quadrado (vermelho)
    glVertex2f(-0.5, -0.5)   # Define o canto inferior esquerdo
    glVertex2f(0.5, -0.5)    # Define o canto inferior direito
    glVertex2f(0.5, 0.5)     # Define o canto superior direito
    glVertex2f(-0.5, 0.5)    # Define o canto superior esquerdo
    glEnd()

def plotSin():
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_LINE_STRIP)
    x=-4.0
    while (x<4.0):
        y = math.sin(math.pi * x) / (math.pi * x)
        glVertex2f(x, y)
        x += 0.1
    glEnd()
    glFlush()

def draw():
    #drawPoints()
    plotSin()


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption('Computação Gráfica')
    init()
    setWindow(-5.0, 5.0, -0.3, 1.0)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT)
        draw()
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
