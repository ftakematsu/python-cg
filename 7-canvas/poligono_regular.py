import tkinter as tk
import math

def rotate_point(point, angle, center):
    # Função para rotacionar um ponto em torno de um centro
    x, y = point
    cx, cy = center
    new_x = cx + (x - cx) * math.cos(angle) - (y - cy) * math.sin(angle)
    new_y = cy + (x - cx) * math.sin(angle) + (y - cy) * math.cos(angle)
    return new_x, new_y

def graus2rad(angle):
    return angle*math.pi/180

def rotatedPoints(sides, rotation_angle, raio):
    angle = 2 * math.pi / sides
    points = [];
    for i in range(sides):
        x = center_x + raio * math.cos(i * angle)
        y = center_y - raio * math.sin(i * angle)
        points.append((x, y))
    rotated_points = [rotate_point(point, rotation_angle, (center_x, center_y)) for point in points]
    return rotated_points

def draw_regular_polygon(canvas, sides, radius, 
                         center_x, center_y, line_color='black', 
                         rotation_angle=0):
    draw_filled_polygon(canvas, sides, radius, 
                        center_x, center_y, 
                        line_color, '', rotation_angle)

def draw_circle(canvas, radius, 
                center_x, center_y, line_color='black'):
    draw_regular_polygon(canvas, 200, radius, 
                center_x, center_y, line_color)

def draw_filled_circle(canvas, radius, 
                center_x, center_y, line_color='black', fill_color='black'):
    draw_filled_polygon(canvas, 200, radius, 
                center_x, center_y, line_color, fill_color)

def draw_filled_polygon(canvas, sides, radius, 
                        center_x, center_y, 
                        line_color='black', fill_color='black', 
                        rotation_angle=0):
    rotation_angle = graus2rad(rotation_angle)
    angle = 2 * math.pi / sides
    points = []
    for i in range(sides):
        x = center_x + radius * math.cos(i * angle)
        y = center_y - radius * math.sin(i * angle)
        points.append((x, y))
    points = rotatedPoints(sides, rotation_angle, radius)
    canvas.create_polygon(points, fill=fill_color, outline=line_color, width=5)


def draw_arc(canvas, cx, cy, 
            radius, startAngle, sweep,
            line_color='black', fill_color='black', solid=True):
    n = 200
    #graus2rad(rotation_angle)
    angle = startAngle * math.pi /180
    angleInc = sweep * 2 * math.pi / (180 *n)
    #rotation_angle = rotation_angle*math.pi/180
    points = []
    sides = 100
    for i in range(sides+1):
        x = cx + radius * math.cos(angle)
        y = cy - radius * math.sin(angle)
        angle += angleInc
        points.append((x, y))
    if (solid):
        canvas.create_polygon(points, fill=fill_color, outline=line_color, width=5)
    else:
        for i in range(sides-1):
            canvas.create_line(points[i][0], points[i][1], points[(i + 1) % sides][0], points[(i + 1) % sides][1])



# Cria uma janela
root = tk.Tk()
root.title("Desenho de Polígono Regular")

# Cria um canvas dentro da janela
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

# Parâmetros do polígono regular
num_sides = 4  # Número de lados do polígono
radius = 300   # Raio do polígono
raio2 = 200
center_x = 250 # Coordenada x do centro do polígono
center_y = 250 # Coordenada y do centro do polígono
line_color = 'blue'
fill_color = 'red'

# Chama a função para desenhar o polígono regular no canvas
#draw_regular_polygon(canvas, num_sides, raio2, center_x, center_y, 'blue', 0)
#draw_filled_polygon(canvas, num_sides, radius, center_x, center_y, line_color, 'green', 45)
#draw_filled_polygon(canvas, num_sides, radius*0.70, center_x, center_y, line_color, 'yellow', 0)
#draw_circle(canvas, radius/3, center_x, center_y, 'black')
#draw_filled_circle(canvas, radius/3, center_x, center_y, 'blue', 'blue')
draw_arc(canvas, center_x, center_y, 100, 0, 180, 'black', 'red', True)


# Inicia o loop principal da aplicação
root.mainloop()
