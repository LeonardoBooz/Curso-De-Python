class Elevador:

    def __init__(self, quantidade_andares, andar, capacidade, qnt_pessoas):
        self.__qquantidade_andares = quantidade_andares
        self.__andar = andar
        self.__capacidade = capacidade
        self.__qnt_pessoas = qnt_pessoas
        
    def entra(self, quant):
        if (self.__qnt_pessoas + quant) > self.__capacidade:
            return f'Quantidade de pessoas excedeu a capacidade em { self.__capacidade - self.__qnt_pessoas + quant}'
        else:
            self.__qnt_pessoas += quant
            return f'Entraram {quant}'
    
    def sai(self, quant):
        if (self.__qnt_pessoas - quant) < 0:
            return f'Haviam apenas {self.__qnt_pessoas}'
        elif self.__qnt_pessoas == 0:
            return 'Não tem nínguem no elevador'
        else:
            self.__qnt_pessoas -= quant
            return f'Sairam {quant}'
        
    def sobe(self):
        if self.__qquantidade_andares > self.__andar:
            self.__andar +=1
            return 'O elevador esta subindo'
        else:
            print("O elevador já esta no ultimo andar")
    
    def desce(self):
        if self.__andar > 0:
            self.__andar -=1
            return 'O elevador esta descendo'
        else:
            print("O elevador já esta no no terreo, não é possível descer mais")


elv = Elevador(10, 0, 5, 0)
from time import sleep
while True:
    print('PAINEL DO ELEVADOR')
    print('===================')
    opc = input('(1)Sobe\n(2)Desce\n(3)Entra Pessoa\n(4)Sai Pessoa')
    if opc == '1':
        print('Você escolheu a opção "Sobe"')
        print(elv.sobe())
        sleep(2)

    elif opc == '2':
        print('Você escolheu a opção "Desce"')
        print(elv.desce())
        sleep(2)

    elif opc == '3':
        print('Você escolheu a opção "Entra Pessoa"')
        quant = int(input('Quantas pessoas vão entrar?'))
        print(elv.entra(quant))
        sleep(2)

    elif opc == '4':
        print('Você escolheu a opção "Sai Pessoa"')
        quant = int(input('Quantas pessoas vão sair?'))
        print(elv.sai(quant))
        sleep(2)
        
    else:
        print('Opção inválida. Tente novamente.')