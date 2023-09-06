import tkinter as tk
from canvas import Canvas # Importação da classe externa

# Cria uma janela
root = tk.Tk()
root.title("Emoji")

# Cria um canvas dentro da janela (instância)
tkCanvas = tk.Canvas(root, width=800, height=800)
tkCanvas.pack()

# Instância do objeto da classe Canvas
canvas = Canvas(tkCanvas)

# Criar o desenho
canvas.desenhaCirculoPreenchido(
    raio=300, centroX=400, centroY=400,
    corLinha='black', corFundo='yellow',
    comprimentoLinha=2
)

canvas.desenhaCirculoPreenchido(
    raio=50, centroX=300, centroY=300,
    corLinha='black', corFundo='black',
    comprimentoLinha=2
)

canvas.desenhaCirculoPreenchido(
    raio=50, centroX=500, centroY=300,
    corLinha='black', corFundo='black',
    comprimentoLinha=2
)

canvas.desenhaArco(
    centroX=400, centroY=450, 
    raio=150, anguloInicial=180, anguloArco=180,
    corLinha='black', 
    corFundo='red', 
    solido=True,
    comprimentoLinha=2
)

# Inicia o loop principal da aplicação
root.mainloop()
