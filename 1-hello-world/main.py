import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw():
    glBegin(GL_LINE_LOOP)
    #glBegin(GL_LINES)
    #glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 1.0)  # Define a cor do quadrado (vermelho)
    glVertex2f(-0.5, -0.5)   # Define o canto inferior esquerdo
    glVertex2f(0.5, -0.5)    # Define o canto inferior direito
    glVertex2f(0.5, 0.5)     # Define o canto superior direito
    glVertex2f(-0.5, 0.5)    # Define o canto superior esquerdo
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluOrtho2D(-1, 1, -1, 1)  # Define a projeção ortogonal

    glClearColor(1.0, 1.0, 1.0, 0.0)  # Define a cor de fundo 

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
