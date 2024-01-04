"""
Leia um número fornecido pelo usuário. Se esse número for positivo, calcule 
a raiz quadrada do número. Se o número for negativo, mostre uma mensagem dizendo
 que o número é invalido
"""

import math

num=int(input("Usuário insira qualquer número apartir de zero: "))
if num > -1:
    print(f"A raiz de {num} é {math.sqrt(num)}")
else:
    print("Digite um número válido!")