"""
Leia um número real. Se o número for positivo imprima a a raiz quadrada.
Do contrário, imprima o número ao quadrado.
"""


import math

num=int(input("Usuário insira qualquer número: "))
if num > -1:
    print(f"A raiz de {num} é {math.sqrt(num)}")
else:
    print(f"O número digitado elevado ao quadrado: {num**2}")