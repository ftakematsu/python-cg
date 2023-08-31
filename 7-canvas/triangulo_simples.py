import tkinter as tk

def draw_triangle(canvas):
    x1, y1 = 100, 100
    x2, y2 = 200, 100
    x3, y3 = 150, 50
    canvas.create_line(x1, y1, x2, y2)
    canvas.create_line(x2, y2, x3, y3)
    canvas.create_line(x3, y3, x1, y1)

def draw_line(canvas):
    x1, y1 = 0, 0
    x2, y2 = 250, 250
    canvas.create_line(x1,y1, x2,y2)

# Cria uma janela
root = tk.Tk()
root.title("Desenho de Triângulo")

# Cria um canvas dentro da janela
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

# Chama a função para desenhar o triângulo no canvas
draw_triangle(canvas)
draw_line(canvas)

# Inicia o loop principal da aplicação
root.mainloop()