import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

'''
Definir os parâmetros de configuração inicial da tela e do desenho.
'''
def init():
    glClearColor(0.92, 0.92, 0.92, 0.0)  # Define a cor de fundo 
    glPointSize(4.0) # Define a espessura do ponto
    glLineWidth(2.0) # Define a espessura da linha

'''
Projeção ortogonal: mapeamento da área do plano
cartesiano XY na janela.
'''
def setWindow(left,right,bottom,top):
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(left,right,bottom,top)

'''
View Port: define a subjanela de visualização.
'''
def setViewport(left, right, bottom, top):
    glViewport(left, bottom, right-left, top-bottom)

'''
Demonstração de desenho de alguns pontos.
'''
def drawPoints():
    setWindow(-10, 10, -10, 10)
    glPointSize(8.0) # Espessura do ponto
    glBegin(GL_POINTS)
    glColor3f(0.0, 0.0, 0.0)  # Define a cor do quadrado (vermelho)
    glVertex2f(0, 0)
    glVertex2f(-5, 8)
    glVertex2f(-2, -2)
    glVertex2f(10, 10)
    glVertex2f(25, 30) # Ponto fora da área (não visível)
    glEnd()

def plotParabola():
    setWindow(-10, 10, -1, 100)
    glColor3f(1.0, 0.0, 0.0)
    #glBegin(GL_POINTS)
    glBegin(GL_LINE_STRIP)
    x = -10
    while (x<=10):
        y = x**2
        glVertex2f(x,y)
        x+=0.1
    glEnd()


def plotSin():
    setWindow(-5.0, 5.0, -0.3, 1.0)
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
    drawPoints()
    #plotParabola()
    setViewport(0, 500, 0, 500)
    plotSin()
    setViewport(0, 150, 0, 150)
    plotSin()
    setViewport(160, 310, 0, 150)
    plotSin()
    setViewport(400, 500, 400, 500)
    plotParabola()


def main():
    pygame.init()
    display = (500, 500)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption('Plotagem da curva')
    init()
    #setWindow(-5.0, 5.0, -0.3, 1.0)
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
