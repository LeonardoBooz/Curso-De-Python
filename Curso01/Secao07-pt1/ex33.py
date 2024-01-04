"""
Faça um programa que leia um vetor de 15 posições e o compacte, ou seja, elimine as
posições com valor zero. Para isso, todos os elementos á frente do valor de zero, deve ser movidos
uma posição para trás no vetor.
"""


from random import randint

lista=[]
for e in range(0, 15):
    lista.append(randint(0,1))
print(lista)
for e in range(len(lista)):
    for e in lista:
        if e == 0:
            lista.remove(e)
print(lista)