import math
def verifica_quadrado(num):
    if math.sqrt(num) != int(math.sqrt(num)):
        print("Não é um quadrado perfeito!")
    else:
        print("É um quadrado perfeito!!")

verifica_quadrado(25)
