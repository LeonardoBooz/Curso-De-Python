class Pessoa:
    def __init__(self, nome, endereco, telefone):
        self.__nome = nome
        self.__endereco = endereco
        self.__telefone = telefone

    def imprimir(texto):
        print(texto)


pessoa = Pessoa('Alberto', 'Rua Emilio Vaz, 445', '47-69955-5659')
print(pessoa.__dict__)