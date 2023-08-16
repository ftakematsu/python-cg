import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Ponto2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Representa o objeto
objeto = []

def criarObjeto():
    objeto.append(Ponto2D(150, 150))
    objeto.append(Ponto2D(150, 300))
    objeto.append(Ponto2D(300, 150))

def draw():
    glBegin(GL_LINE_LOOP)
    glColor3f(0.0, 0.0, 1.0)  # Define a cor do quadrado (vermelho)
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

        glClear(GL_COLOR_BUFFER_BIT)
        draw()
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
