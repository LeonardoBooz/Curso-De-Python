"""
Faça um programa que leia um número inteiro positivo impar N e imprima todos os números impares
de 0 até N em ordem crescente.
"""
num=int(input('Digite um número: '))
if num%2==1:
    for e in range(1, num+2, 2):
        print(e)
else:
    print("Digite um número válido")