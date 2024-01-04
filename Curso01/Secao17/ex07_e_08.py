class Circulo:
    def __init__(self, raio, area, perimetro):
        self.raio = raio
        if area == 0:
            self.area = self.calcularArea(raio)
        else:
            self.area = area
        if perimetro == 0:
            self.perimetro = self.calcularPerimetro(raio)
        else:
            self.perimetro = perimetro
            
    def calcularArea(self, raio):
        return 3.141516 * raio * raio

    def calcularPerimetro(self, raio):
        return 2 * 3.141516 * raio