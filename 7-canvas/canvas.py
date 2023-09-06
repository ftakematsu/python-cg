import math

class Canvas:
    def __init__(self, canvas):
        """
        Construtor para receber um objeto canvas
        """
        self.canvas = canvas
    
    def desenharLinha(
        self, xInicial, yInicial, xFinal, yFinal,
        corLinha='black', comprimentoLinha=1
    ):
        '''
        Desenha um segmento de reta considerando a ligação das coordenadas
        (xInicial, yInicial) e (xFinal, yFinal)
        '''
        self.canvas.create_line(
            xInicial, yInicial, xFinal, yFinal,
            fill=corLinha, width=comprimentoLinha
        )
    
    def desenharRetangulo(self, xInicial, yInicial, xFinal, yFinal):
        '''
        Desenha retângulo considerando a ligação das coordenadas
        (xInicial, yInicial) e (xFinal, yFinal)
        '''
        self.canvas.create_rectangle(xInicial, yInicial, xFinal, yFinal)
    
    def desenharRetanguloSolido(
            self, xInicial, yInicial, xFinal, yFinal,
            corFundo, corLinha, comprimentoLinha
    ):
        '''
        Desenha retângulo preenchido considerando a ligação das coordenadas
        (xInicial, yInicial) e (xFinal, yFinal)
        '''
        self.canvas.create_rectangle(
            xInicial, yInicial, xFinal, yFinal,
            fill=corFundo, outline=corLinha, width=comprimentoLinha
        )
    
    def rotacionaPonto(self, point, angle, center):
        # Função para rotacionar um ponto em torno de um centro
        x, y = point
        cx, cy = center
        new_x = cx + (x - cx) * math.cos(angle) - (y - cy) * math.sin(angle)
        new_y = cy + (x - cx) * math.sin(angle) + (y - cy) * math.cos(angle)
        return new_x, new_y

    def graus2rad(self, angle):
        return angle*math.pi/180

    def rotacionaPontos(self, sides, rotation_angle, raio, center_x, center_y):
        angle = 2 * math.pi / sides
        points = [];
        for i in range(sides):
            x = center_x + raio * math.cos(i * angle)
            y = center_y - raio * math.sin(i * angle)
            points.append((x, y))
        rotated_points = [self.rotacionaPonto(point, rotation_angle, (center_x, center_y)) for point in points]
        return rotated_points

    def desenhaPoligonoRegular(self, sides, radius, 
                         center_x, center_y, line_color='black', 
                         rotation_angle=0):
        self.desenhaPoligonoRegularPreenchido(sides, radius, 
                            center_x, center_y, 
                            line_color, '', rotation_angle)

    def desenhaCirculo(self, radius, 
                    center_x, center_y, line_color='black'):
        self.desenhaPoligonoRegular(200, radius, 
                    center_x, center_y, line_color)

    def desenhaCirculoPreenchido(self, raio, 
                    centroX, centroY, corLinha='black', corFundo='black', comprimentoLinha=1):
        self.desenhaPoligonoRegularPreenchido(200, raio, 
                    centroX, centroY, corLinha, corFundo, 0, comprimentoLinha)

    def desenhaPoligonoRegularPreenchido(self, sides, raio, 
                            centroX, centroY, 
                            corLinha='black', corFundo='black', 
                            anguloRotacao=0, comprimentoLinha=1):
        rotation_angle = self.graus2rad(anguloRotacao)
        angle = 2 * math.pi / sides
        points = []
        for i in range(sides):
            x = centroX + raio * math.cos(i * angle)
            y = centroY - raio * math.sin(i * angle)
            points.append((x, y))
        points = self.rotacionaPontos(sides, rotation_angle, raio, centroX, centroY)
        self.canvas.create_polygon(points, fill=corFundo, outline=corLinha, width=comprimentoLinha)

    def desenhaArco(self, centroX, centroY, 
                raio, anguloInicial, anguloArco,
                corLinha='black', 
                corFundo='black', 
                solido=True,
                comprimentoLinha=1
    ):
        n = 200
        #graus2rad(rotation_angle)
        angle = anguloInicial * math.pi /180
        angleInc = anguloArco * 2 * math.pi / (180 *n)
        #rotation_angle = rotation_angle*math.pi/180
        points = []
        sides = 100
        for i in range(sides+1):
            x = centroX + raio * math.cos(angle)
            y = centroY - raio * math.sin(angle)
            angle += angleInc
            points.append((x, y))
        if (solido):
            self.canvas.create_polygon(points, fill=corFundo, outline=corLinha, width=comprimentoLinha)
        else:
            for i in range(sides-1):
                self.canvas.create_line(points[i][0], points[i][1], points[(i + 1) % sides][0], points[(i + 1) % sides][1], fill=corLinha, width=comprimentoLinha)

