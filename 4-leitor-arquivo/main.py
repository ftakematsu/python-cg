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

'''
Leitor do arquivo
'''
def readFile(fileName):
    pass

def draw():
    setWindow(0.0, 640.0, 0.0, 480.0)
    readFile("exemplo.dat")


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
