class tv:
    def __init__(self, ligado=False, canal=1, volume=20, numero_canais=222, volume_maximo=100):
        self.ligado = ligado
        self.canal = canal
        self.volume = volume
        self.numero_canais = numero_canais
        self.volume_maximo = volume_maximo
    
    def imprimir():
        print(tv.__dict__)

    def ligar(self):
        if self.ligado == True:
            self.ligado = False
        else:
            self.ligado = True
    
    def canal_acima(self):
        if self.canal >= 1 and self.canal < self.numero_canais:
            self.canal += 1
        else:
            self.canal = 1

    def canal_abaixo(self):
        if self.canal > 1 and self.canal <= self.numero_canais:
            self.canal -= 1
        else:
            self.canal = self.numero_canais

    def volume_acima(self):
        if self.volume >= 0 and self.volume < self.volume_maximo:
            self.volume += 1

    def volume_abaixo(self):
        if self.volume > 0 and self.volume <= self.volume_maximo:
            self.volume -= 1
