"""
Faça um programa que leia um número inteiro positivo impar N e imprima todos os números impares
de 0 até N em ordem decrescente.
"""
num=int(input('Digite um número: '))
if num%2==1:
    for e in range(num, -1, -2):
        print(e)
else:
    print("Digite um número válido")