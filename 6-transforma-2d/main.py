import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import random

class Ponto2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Representa o objeto
objeto = []
novoR = 0
novoG = 0
novoB = 1

def criarObjeto():
    objeto.append(Ponto2D(150, 150))
    objeto.append(Ponto2D(150, 300))
    objeto.append(Ponto2D(300, 150))

def centroMassa():
    cm = Ponto2D(0,0)
    somax = 0
    somay = 0
    cont = 0
    for p in objeto: 
        somax += p.x
        somay += p.y
        cont+=1
    cm.x = somax/cont
    cm.y = somay/cont
    return cm

def translacao(dX, dY):
    for p in objeto:
        p.x = p.x + dX
        p.y = p.y + dY

def escala(eX, eY):
    cm = centroMassa() # Define o centro de massa
    translacao(-cm.x, -cm.y) # Translada o objeto para origem
    # Aplica a escala
    for p in objeto:
        p.x = p.x*eX
        p.y = p.y*eY
    # Translada de volta para o local original
    translacao(cm.x, cm.y)

def rotacao(angulo):
    cm = centroMassa()
    translacao(-cm.x, -cm.y)
    # Convertendo graus para radianos
    rad = angulo*(math.pi/180)
    for p in objeto:
        novox = p.x*math.cos(rad) - p.y*math.sin(rad)
        novoy = p.x*math.sin(rad) + p.y*math.cos(rad)
        p.x = novox
        p.y = novoy
    translacao(cm.x, cm.y)

def draw():
    glBegin(GL_LINE_LOOP)
    glColor3f(novoR, novoG, novoB)  # Define a cor do quadrado (vermelho)
    for p in objeto:
        glVertex2f(p.x, p.y)
    glEnd()

def main():
    pygame.init()
    display = (700, 700)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption('Transformações 2D')
    gluOrtho2D(0, 500, 0, 500)  # Define a projeção ortogonal
    glClearColor(1.0, 1.0, 1.0, 0.0)  # Define a cor de fundo 
    criarObjeto()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t:
                    translacao(5, 5)
                elif event.key == pygame.K_e:
                    escala(1.1, 1.1)
                elif event.key == pygame.K_r or event.key == pygame.K_o:
                    rotacao(10)
                elif event.key == pygame.K_p:
                    rotacao(-10)
                elif event.key == pygame.K_q:
                    escala(1.1, 1)
                elif event.key == pygame.K_w:
                    escala(1, 1.1)
                elif event.key == pygame.K_f:
                    escala(0.9, 1)
                elif event.key == pygame.K_g:
                    escala(1, 0.9)
                elif event.key == pygame.K_UP:
                    translacao(0, 5)
                elif event.key == pygame.K_DOWN:
                    translacao(0, -5)
                elif event.key == pygame.K_LEFT:
                    translacao(-5, 0)
                elif event.key == pygame.K_RIGHT:
                    translacao(5, 0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("Click")
                novoR = random.random()
                novoG = random.random()
                novoB = random.random()

        glClear(GL_COLOR_BUFFER_BIT)
        draw()
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
