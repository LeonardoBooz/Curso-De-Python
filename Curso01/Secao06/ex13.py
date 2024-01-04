"""
Faça um programa que leia um número inteiro positivo par N e imprima todos os números pares
de 0 até N em ordem crescente.
"""
num=int(input('Digite um número: '))
if num%2==0:
    for e in range(0, num+1, 2):
        print(e)
else:
    print("Digite um número válido")