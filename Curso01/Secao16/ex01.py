class Pessoa:
    def __init__(self, nome, idade, altura):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura

    
    def set_nome(self, nome):
        self.__nome = nome
    
    def set_idade(self, idade):
        self.__idade = idade

    def set_altura(self, altura):
        self.__altura = altura
    
    def get_nome(self):
        return self.__nome
    
    def get_idade(self):
        return self.__idade

    def get_altura(self):
        return self.__altura
    