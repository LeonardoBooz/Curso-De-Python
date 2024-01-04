"""
Faça um programa que leia um número e, se caso ele seja positivo, calcule e mostre:
    o número digitado ao quadrado
    a raiz quadrada do número digitado
"""


import math

num=int(input("Usuário insira qualquer número: "))
if num > -1:
    print(f"A raiz de {num} é {math.sqrt(num)}")
    print(f"O número digitado elevado ao quadrado: {num**2}")
else:
    print("Digite um número válido!")