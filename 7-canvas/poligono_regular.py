import tkinter as tk
from canvas import Canvas # Importação da classe externa

# Cria uma janela
root = tk.Tk()
root.title("Canvas")

# Cria um canvas dentro da janela (instância)
tkCanvas = tk.Canvas(root, width=500, height=500)
tkCanvas.pack()

# Instância do objeto da classe Canvas
canvas = Canvas(tkCanvas)

# Parâmetros do polígono regular
num_sides = 5  # Número de lados do polígono
radius = 300   # Raio do polígono
raio2 = 200
center_x = 250 # Coordenada x do centro do polígono
center_y = 250 # Coordenada y do centro do polígono
line_color = 'blue'
fill_color = 'red'

canvas.desenharLinha(10,10, 200,300, 'yellow', 10)
canvas.desenharRetanguloSolido(10,10, 200,300, '', 'red', 7)
canvas.desenhaPoligonoRegularPreenchido(num_sides, radius*0.70, center_x, center_y, line_color, 'yellow', 0)
canvas.desenhaCirculo(raio2, center_x, center_y, 'black')
canvas.desenhaArco(center_x, center_y, 100, 0, 180, 'black', 'red', True)

# Inicia o loop principal da aplicação
root.mainloop()
