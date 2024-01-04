"""
Faça um programa que receba três números e mostre-os em ordem crescente.
"""

lista_dados=[]

for e in range(3):
    num=int(input("Digite um número:"))
    lista_dados.append(num)
lista_dados.sort()
for f in lista_dados:
    print(f)