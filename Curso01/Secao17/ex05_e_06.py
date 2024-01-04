class Retangulo:
    def __init__(self, comprimento, largura, area = 0, perimetro = 0):
        self.comprimento = comprimento
        self.largura = largura
        if area == 0:
            self.area = Retangulo.calcular_area(comprimento, largura)
        else:
            self.area = area
        if perimetro == 0:
            self.perimetro = Retangulo.calcular_perimetro(comprimento, largura)
        else:
            self.perimetro = perimetro

    def calcular_area(comprimento, largura):
        return comprimento * largura

    def calcular_perimetro(comprimento, largura):
        return (2 * comprimento) + (2 * largura)
    
ret = Retangulo(25, 15)
ter = Retangulo(25, 15, 50, 60)

print(ret.__dict__)
print(ter.__dict__)