import math

class Canvas:
    def __init__(self, canvas):
        """
        Construtor para receber um objeto canvas
        """
        self.canvas = canvas
    
    def desenharLinha(
        self, xInicial, yInicial, xFinal, yFinal,
        corLinha='black', espessuraLinha=1
    ):
        '''
        Desenha um segmento de reta considerando a ligação das coordenadas
        (xInicial, yInicial) e (xFinal, yFinal)
        '''
        self.canvas.create_line(
            xInicial, yInicial, xFinal, yFinal,
            fill=corLinha, width=espessuraLinha
        )
    
    def desenharRetangulo(self, xInicial, yInicial, xFinal, yFinal):
        '''
        Desenha retângulo considerando a ligação das coordenadas
        (xInicial, yInicial) e (xFinal, yFinal)
        '''
        self.canvas.create_rectangle(xInicial, yInicial, xFinal, yFinal)
    
    def desenharRetanguloSolido(
            self, xInicial, yInicial, xFinal, yFinal,
            corFundo, corLinha, espessuraLinha
    ):
        '''
        Desenha retângulo preenchido considerando a ligação das coordenadas
        (xInicial, yInicial) e (xFinal, yFinal)
        '''
        self.canvas.create_rectangle(
            xInicial, yInicial, xFinal, yFinal,
            fill=corFundo, outline=corLinha, width=espessuraLinha
        )
    
    def rotacionaPonto(self, point, angle, center):
        """
        Função para rotacionar um ponto em torno de um centro (point)
        """
        x, y = point
        cx, cy = center
        new_x = cx + (x - cx) * math.cos(angle) - (y - cy) * math.sin(angle)
        new_y = cy + (x - cx) * math.sin(angle) + (y - cy) * math.cos(angle)
        return new_x, new_y

    def graus2rad(self, angle):
        """
        Converte um ângulo em graus para radianos
        """
        return angle*math.pi/180

    def rotacionaPontos(self, sides, rotation_angle, raio, center_x, center_y):
        """
        Aplica a rotação para um conjunto de pontos
        """
        angle = 2 * math.pi / sides
        points = []
        for i in range(sides):
            x = center_x + raio * math.cos(i * angle)
            y = center_y - raio * math.sin(i * angle)
            points.append((x, y))
        rotated_points = [self.rotacionaPonto(point, rotation_angle, (center_x, center_y)) for point in points]
        return rotated_points

    def desenhaPoligonoRegular(self, lados, raio, 
                         centroX, centroY, corLinha='black', 
                         anguloRotacao=0, espessuraLinha=1):
        """
        Desenha um polígono regular considerando o número de lados um centro, raio e ângulo. 
        Possui parâmetros adicionais como cores (linha e fundo), espessura da linha e ângulo de rotação
        """
        self.desenhaPoligonoRegularPreenchido(lados, raio, 
                            centroX, centroY, 
                            corLinha, '', anguloRotacao, espessuraLinha)

    def desenhaCirculo(self, radius, 
                    centroX, centroY, corLinha='black', anguloRotacao=0, espessuraLinha=1):
        """
        Desenha um círculo (apenas circunferência, sem preenchimento) considerando o centro e raio. 
        Possui parâmetros adicionais como cores (linha e fundo) e espessura da linha.
        """
        self.desenhaPoligonoRegular(200, radius, 
                    centroX, centroY, corLinha, anguloRotacao, espessuraLinha)

    def desenhaCirculoPreenchido(self, raio, 
                    centroX, centroY, corLinha='black', corFundo='black', espessuraLinha=1):
        """
        Desenha um círculo sólido considerando o centro e raio. 
        Possui parâmetros adicionais como cores (linha e fundo) e espessura da linha.
        """
        self.desenhaPoligonoRegularPreenchido(200, raio, 
                    centroX, centroY, corLinha, corFundo, 0, espessuraLinha)

    def desenhaPoligonoRegularPreenchido(self, lados, raio, 
                            centroX, centroY, 
                            corLinha='black', corFundo='black', 
                            anguloRotacao=0, espessuraLinha=1):
        """
        Desenha um polígono regular sólido considerando o número de lados um centro, raio e ângulo. 
        Possui parâmetros adicionais como cores (linha e fundo), espessura da linha e ângulo de rotação.
        """
        rotation_angle = self.graus2rad(anguloRotacao)
        angle = 2 * math.pi / lados
        points = []
        for i in range(lados):
            x = centroX + raio * math.cos(i * angle)
            y = centroY - raio * math.sin(i * angle)
            points.append((x, y))
        points = self.rotacionaPontos(lados, rotation_angle, raio, centroX, centroY)
        self.canvas.create_polygon(points, fill=corFundo, outline=corLinha, width=espessuraLinha)

    def desenhaCirculosBaseadoNoHexagono(self, raio, 
                            centroX, centroY, 
                            corLinha='black', 
                            anguloRotacao=0, espessuraLinha=1):
        """
        Desenha um polígono regular sólido considerando o número de lados um centro, raio e ângulo. 
        Possui parâmetros adicionais como cores (linha e fundo), espessura da linha e ângulo de rotação.
        """
        lados = 6
        rotation_angle = self.graus2rad(anguloRotacao)
        angle = 2 * math.pi / lados
        points = []
        for i in range(lados):
            x = centroX + raio * math.cos(i * angle)
            y = centroY - raio * math.sin(i * angle)
            points.append((x, y))
        points = self.rotacionaPontos(lados, rotation_angle, raio, centroX, centroY)
        # Os pontos serão os centros da circunferência
        for ponto in points:
            self.desenhaCirculo(raio/2, ponto[0], ponto[1])
        #self.canvas.create_polygon(points, fill='', outline=corLinha, width=espessuraLinha)

    def desenhaQuadradoTextura(self, raio, 
                            centroX, centroY, 
                            corLinha='black', 
                            anguloRotacao=90, espessuraLinha=1):
        """
        Desenha um polígono regular sólido considerando o número de lados um centro, raio e ângulo. 
        Possui parâmetros adicionais como cores (linha e fundo), espessura da linha e ângulo de rotação.
        """
        lados = 4
        rotation_angle = self.graus2rad(anguloRotacao)
        angle = 2 * math.pi / lados
        points = []
        for i in range(lados):
            x = centroX + raio * math.cos(i * angle)
            y = centroY - raio * math.sin(i * angle)
            points.append((x, y))
        points = self.rotacionaPontos(lados, rotation_angle, raio, centroX, centroY)
        # Os pontos serão os centros da circunferência
        for ponto in points:
            self.desenhaCirculo(raio, ponto[0], ponto[1], espessuraLinha=espessuraLinha)
        self.canvas.create_polygon(points, fill='', outline=corLinha, width=espessuraLinha)


    def desenhaArco(self, centroX, centroY, 
                raio, anguloInicial, anguloArco,
                corLinha='black', 
                corFundo='black', 
                solido=True,
                espessuraLinha=1
    ):
        """
        Desenha um arco considerando um centro, raio e ângulo. 
        Possui parâmetros adicionais como cores (linha e fundo), espessura da linha e se é uma figura sólida ou não.
        """
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
            self.canvas.create_polygon(points, fill=corFundo, outline=corLinha, width=espessuraLinha)
        else:
            for i in range(sides-1):
                self.canvas.create_line(points[i][0], points[i][1], points[(i + 1) % sides][0], points[(i + 1) % sides][1], fill=corLinha, width=espessuraLinha)

