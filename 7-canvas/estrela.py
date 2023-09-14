import tkinter as tk
from canvas import Canvas # Importação da classe externa

# Cria uma janela
root = tk.Tk()
root.title("Estrela")

# Cria um canvas dentro da janela (instância)
tkCanvas = tk.Canvas(root, width=800, height=800)
tkCanvas.pack()

# Instância do objeto da classe Canvas
canvas = Canvas(tkCanvas)

# Desenha um pentagono
canvas.desenhaPoligonoRegular(5, 250, 400, 400, 
                              corLinha='black', 
                              anguloRotacao=-90,
                              espessuraLinha=2)

canvas.desenhaCirculo(250, 400, 400,
                        corLinha='black', 
                        anguloRotacao=-90,
                        espessuraLinha=2)

# Inicia o loop principal da aplicação
root.mainloop()
