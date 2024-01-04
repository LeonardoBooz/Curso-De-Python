"""
Faça um programa que leia dez conjuntos de dois valores, o primeiro representando
o número do aluno e o segundo representado a sua altura em metros. Encontre o aluno
mais baixo e o mais alto. Mostre o número do aluno mais baixo e o mais alto,
juntamente com suas alturas.
"""
from random import randint
conjuntos=[]
lista=[]
for e in range(10):
    conjuntos.append({'numero' : e+1, 
                      'altura' : randint(110, 215)})
for e in conjuntos:
    altura=e['altura']
    lista.append(altura)
print(f'O aluno mais alto é {lista.index(max(lista))}: {max(lista)/100}m\n'+
      f'e o mais baixo é o {lista.index(min(lista))}: {min(lista)/100}m')