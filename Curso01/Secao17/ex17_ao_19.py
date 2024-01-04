class Eletro:
    def __init__(self, ligada = False):
        self.ligada = ligada

    def imprimir(self):
        print(self.ligada)

    def ligar(self):
        if self.ligada == True:
            self.ligada = False
        else:
            self.ligada = True