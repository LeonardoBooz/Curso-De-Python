class Televisao:
    def __init__(self, canal, volume):
        self.__canal = canal
        self.__volume = volume
    
    def set_canal(self, canal):
        self.__canal = canal
    
    def set_volume(self, volume):
        self.__volume= volume

    def get_canal(self):
        return self.__canal
    
    def get_volume(self):
        return self.__volume


class ControleRemoto:
    def __init__(self) -> None:
        self.tl = Televisao
        pass

    def passar_canal(self, n):
        self.tl.set_canal = self.tl.get_canal + n
    
    def definir_canal(self, canal):
        self.tl.set_canal = canal

    def mexer_volume(self, n):
        self.tl.set_canal = self.tl.get_canal + n
    
    
