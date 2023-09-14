import tkinter as tk
from canvas import Canvas # Importação da classe externa

# Cria uma janela
root = tk.Tk()
root.title("7 Circulos")

# Cria um canvas dentro da janela (instância)
tkCanvas = tk.Canvas(root, width=800, height=800)
tkCanvas.pack()

# Instância do objeto da classe Canvas
canvas = Canvas(tkCanvas)

# Criar o desenho - rosto
canvas.desenhaCirculosBaseadoNoHexagono(200, 400, 400)

# Inicia o loop principal da aplicação
root.mainloop()
