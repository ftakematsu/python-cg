import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import os
from enum import Enum

ROOT_DIR = os.path.abspath(os.curdir)

def setWindow(left,right,bottom,top):
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(left,right,bottom,top)

def setViewport(left, right, bottom, top):
    glViewport(left, bottom, right-left, top-bottom)

class Modo(Enum):
    DESENHO = 1
    REMOVER = 2
    EDITAR = 3

class RGB:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Poligono:
    pontos = []
    def __init__(self):
        pass
    def add(self, ponto: Ponto):
        self.pontos.append(ponto)
    def draw(self):
        pass

class Tela:
    ponto = 1.0
    linha = 1.0
    fundo = RGB(1.0, 1.0, 1.0)
    cor = RGB(0.0, 0.0, 0.0)
    def __init__(self, px, py, title):
        self.pX = px
        self.pY = py
        self.title = title
        pygame.init()
        display = (self.pX, self.pY)
        pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
        pygame.display.set_caption(self.title)
        glClearColor(self.fundo.red, self.fundo.green, self.fundo.blue, 0.0)  # Define a cor de fundo 
        glPointSize(self.ponto)
        glLineWidth(self.linha)
        setWindow(0.0, self.pX, 0.0, self.pY)
        glColor3f(self.cor.red, self.cor.green, self.cor.blue)
    def draw(self):
        pass

def main():
    tela = Tela(500, 500, "Editor de polígonos")
    while True: # Looping para capturar eventos
        # Iteração sobre uma lista de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Evento ao tentar fechar a janela
                print("Saindo...")
                pygame.quit() # Fecha a janela
                quit() # Encerra o processo
            if event.type == pygame.MOUSEBUTTONDOWN: # Botão do mouse clicado
                (posX, posY) = pygame.mouse.get_pos()
                print("Voce clicou em: " + str((posX, posY)))
        glClear(GL_COLOR_BUFFER_BIT)
        tela.draw()
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
