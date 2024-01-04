"""
Elabore um programa que faça uma leitura de vários números inteiros, até que se digite um
número negativo. O programa tem que retornar o maior e o menor número lido.
"""
lista=[]
num=0
cont=False
while cont == False:
    num=int(input("Digite um número:"))
    lista.append(num)
    if num < 0:
        cont=True
print(max(lista), min(lista))