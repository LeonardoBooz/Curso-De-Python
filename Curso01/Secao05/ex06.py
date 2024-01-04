"""
Escreva um programa que, dados dois números inteiros, mostre na tela o maior deles,
assim como a diferença existente entre ambos.
"""


lista=[]

for _ in range(2):
    num=int(input("Digite algum número: "))
    lista.append(num)
if lista[0] > lista[1]:
    print(f"O maior é o {lista[0]} e possue {lista[0]-lista[1]} números a mais que o {lista[1]}")
else:
    print(f"O maior é o {lista[1]} e possue {lista[1]-lista[0]} números a mais que o {lista[0]}")