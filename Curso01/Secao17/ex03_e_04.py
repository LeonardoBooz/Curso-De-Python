class Quadrado:
    def __init__(self, lado, area=0, perimetro=0):
        self.lado = lado
        if area == 0:
            self.area = Quadrado.calcular_area(lado)
        else:
            self.area = area
        if perimetro == 0:
            self.perimetro = Quadrado.calcular_perimetro(lado)
        else:
            self.perimetro = perimetro

    def calcular_area(lado):
        return lado * lado

    def calcular_perimetro(lado):
        return 4 * lado
    
print(Quadrado(4, area=16, perimetro=19).__dict__)
