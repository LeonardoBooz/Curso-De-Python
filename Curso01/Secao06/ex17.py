"""
Faça um programa que leia um número inteiro positivo N e calcule a soma dos
n primeiros números naturais
"""


lista=[]
num=int(input('Digite um número: '))

for e in range(0, num+1):
    lista.append(e)
print(sum(lista))
