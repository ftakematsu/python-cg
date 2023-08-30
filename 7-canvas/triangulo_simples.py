import tkinter as tk

def draw_triangle(canvas):
    x1, y1 = 100, 100
    x2, y2 = 200, 100
    x3, y3 = 150, 50
    
    canvas.create_line(x1, y1, x2, y2)
    canvas.create_line(x2, y2, x3, y3)
    canvas.create_line(x3, y3, x1, y1)

# Cria uma janela
root = tk.Tk()
root.title("Desenho de Triângulo")

# Cria um canvas dentro da janela
canvas = tk.Canvas(root, width=300, height=200)
canvas.pack()

# Chama a função para desenhar o triângulo no canvas
draw_triangle(canvas)

# Inicia o loop principal da aplicação
root.mainloop()