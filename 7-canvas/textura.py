import tkinter as tk
from canvas import Canvas # Importação da classe externa

# Cria uma janela
root = tk.Tk()
root.title("Textura")

# Cria um canvas dentro da janela (instância)
tkCanvas = tk.Canvas(root, width=800, height=800)
tkCanvas.pack()

# Instância do objeto da classe Canvas
canvas = Canvas(tkCanvas)

canvas.desenhaQuadradoTextura(100, 400, 400, espessuraLinha=2)

# Inicia o loop principal da aplicação
root.mainloop()
