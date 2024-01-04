"""
Ler um número inteiro. Se o número lido for negativo, escreva a mensage
'Número invalido'. Se o número for positivo, calcular o logaritimo deste número.
"""

import math

num=int(input("Digite um número inteiro: "))
if num >= 0:
    print(math.log10(num))
else:
    print("Número invalido")