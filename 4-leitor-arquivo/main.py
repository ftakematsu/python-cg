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
    modo = 0 # Modo 0: primeiro desenho, Modo 1: não é o primeiro
    with open(fileName) as f:
        for line in f:
            # Separa a string por espaço
            linhaAux = line.strip().split(' ')
            #print(linhaAux)
            if (len(linhaAux)==1): # Se a lista for tamanho 1
                if (modo==0):
                    glBegin(GL_LINE_STRIP)
                    modo=1
                else:
                    glEnd() # Importante para indicar o fim de uma sequência de linhas
                    glBegin(GL_LINE_STRIP) # Inicia a próxima figura
            elif (len(linhaAux)==2): # Indica ser uma coordenada xy
                glVertex2f(float(linhaAux[0]), float(linhaAux[1]))
    glEnd() # Finaliza o desenho de forma geral
    glFlush() # Sempre faz uma atualização da tela


def draw():
    setWindow(0.0, 640.0, 0.0, 480.0)
    glColor3f(0.0, 0.0, 0.0)
    readFile("C:\\Users\\senai\\Documents\\python-cg\\4-leitor-arquivo\\dino.dat")


def main():
    pygame.init()
    display = (800, 800)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption('Computação Gráfica')
    #readFile("C:\\Users\\senai\\Documents\\python-cg\\4-leitor-arquivo\\exemplo.dat")
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
