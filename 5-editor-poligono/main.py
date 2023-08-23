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
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

class Poligono:
    def __init__(self):
        self.pontos = []
    def add(self, ponto: Ponto):
        self.pontos.append(ponto)
    def draw(self):
        #glBegin(GL_LINE_LOOP)
        glBegin(GL_LINE_STRIP)
        for ponto in self.pontos:
            #print("Ponto: " + str(ponto))
            glVertex2d(ponto.x, ponto.y)
        glEnd()
        glFlush()
    def printData(self):
        for ponto in self.pontos:
            print(str(ponto))

class Tela:
    ponto = 1.0
    linha = 1.0
    fundo = RGB(1.0, 1.0, 1.0)
    cor = RGB(0.0, 0.0, 0.0)
    poligonos = [] # Lista de objetos Poligono
    polAtual = 0 # Índice do polígono atual
    qtdPoligonos = 1 # Quantidade total de poligonos
    def __init__(self, px, py, title):
        self.pX = px # Largura da janela
        self.pY = py # Altura da janela
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
        self.poligonos.append(Poligono())

    def proximoPoligono(self):
        self.polAtual += 1
        if (self.polAtual==self.qtdPoligonos):
            self.poligonos.append(Poligono())
            self.qtdPoligonos+=1

    def poligonoAnterior(self):
        # Para validação, apenas se valor >0
        if (self.polAtual>0):
            self.polAtual-=1

    def addPonto(self, ponto: Ponto):
        # Conversão da dimensão das coordenadas matriciais
        # para a dimensão do plano Cartesiano
        ponto.y = self.pY - ponto.y
        self.poligonos[self.polAtual].add(ponto)

    def draw(self):
        # Criar uma repetição while para desenhar cada polígono da lista
        i=0
        while (i<self.qtdPoligonos):
            if (i==self.polAtual):
                glLineWidth(3.0)
            else:
                glLineWidth(1.0)
            self.poligonos[i].draw()
            i+=1 # Incremento para evitar looping infinito

    def printData(self):
        i=0
        while (i<self.qtdPoligonos):
            print(f"Poligono {i}")
            self.poligonos[i].printData()
            i+=1


def main():
    tela = Tela(900, 900, "Editor de polígonos")
    while True: # Looping para capturar eventos
        # Iteração sobre uma lista de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Evento ao tentar fechar a janela
                print("Saindo...")
                pygame.quit() # Fecha a janela
                quit() # Encerra o processo
            if event.type == pygame.MOUSEBUTTONDOWN: # Botão do mouse clicado
                (posX, posY) = pygame.mouse.get_pos()
                #print("Voce clicou em: " + str((posX, posY)))
                # Adicionando a região do pixel x,y como coordenada
                tela.addPonto(Ponto(posX, posY))
            # Eventos relacionados a teclado
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    tela.printData()
                if event.key == pygame.K_RIGHT:
                    tela.proximoPoligono()
                    print("Proximo: " )
                    print(str(tela.polAtual))
                elif event.key == pygame.K_LEFT:
                    tela.poligonoAnterior()
                    print("Anterior: " )
                    print(str(tela.polAtual))

        glClear(GL_COLOR_BUFFER_BIT)
        tela.draw()
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
