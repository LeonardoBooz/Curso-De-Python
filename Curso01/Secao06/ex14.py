"""
Faça um programa que leia um número inteiro positivo par N e imprima todos os números pares
de 0 até N em ordem decrescente.
"""
num=int(input('Digite um número: '))
if num%2==0:
    for e in range(num, 0, -2):
        print(e)
else:
    print("Digite um número válido")