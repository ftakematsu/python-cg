import tkinter as tk
import math

def rotate_point(point, angle, center):
    # Função para rotacionar um ponto em torno de um centro
    x, y = point
    cx, cy = center
    new_x = cx + (x - cx) * math.cos(angle) - (y - cy) * math.sin(angle)
    new_y = cy + (x - cx) * math.sin(angle) + (y - cy) * math.cos(angle)
    return new_x, new_y

def rotatedPoints(sides, rotation_angle):
    angle = 2 * math.pi / sides
    points = [];
    for i in range(sides):
        x = center_x + radius * math.cos(i * angle)
        y = center_y - radius * math.sin(i * angle)
        points.append((x, y))
    rotated_points = [rotate_point(point, rotation_angle, (center_x, center_y)) for point in points]
    return rotated_points

def draw_regular_polygon(canvas, sides, radius, center_x, center_y, line_color='black', rotation_angle=0):
    rotation_angle = rotation_angle*math.pi/180
    angle = 2 * math.pi / sides
    points = []
    for i in range(sides):
        x = center_x + radius * math.cos(i * angle)
        y = center_y - radius * math.sin(i * angle)
        points.append((x, y))
    points = rotatedPoints(sides, rotation_angle)
    canvas.create_polygon(points, fill='', outline=line_color, width=1)

def draw_filled_polygon(canvas, sides, radius, center_x, center_y, line_color='black', fill_color='black', rotation_angle=0):
    rotation_angle = rotation_angle*math.pi/180
    angle = 2 * math.pi / sides
    points = []
    for i in range(sides):
        x = center_x + radius * math.cos(i * angle)
        y = center_y - radius * math.sin(i * angle)
        points.append((x, y))
    points = rotatedPoints(sides, rotation_angle)
    canvas.create_polygon(points, fill=fill_color, outline=line_color, width=1)


# Cria uma janela
root = tk.Tk()
root.title("Desenho de Polígono Regular")

# Cria um canvas dentro da janela
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

# Parâmetros do polígono regular
num_sides = 6  # Número de lados do polígono
radius = 100   # Raio do polígono
center_x = 250 # Coordenada x do centro do polígono
center_y = 250 # Coordenada y do centro do polígono
fill_color = 'red'

# Chama a função para desenhar o polígono regular no canvas
draw_regular_polygon(canvas, num_sides, radius, center_x, center_y, 'blue', 0)
#draw_filled_polygon(canvas, num_sides, radius, center_x, center_y, fill_color)


# Inicia o loop principal da aplicação
root.mainloop()
