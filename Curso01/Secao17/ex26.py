class Microondas:
    def __init__(self, ligado=False, porta_fechada=True) -> None:
        self.ligado = ligado
        self.porta = porta_fechada

    def imprimir():
        print(Microondas.__dict__)

    def ligar(self):
        if self.ligado == True:
            self.ligado = False
        else:
            if self.porta_fechada == True:
                self.ligado = True
            else:
                print('Feche a porta primeiro')
        
    def porta_fecha(self):
        if self.porta_fechada == True:
            self.porta_fechada = False
        else:
            self.porta_fechada = True

    