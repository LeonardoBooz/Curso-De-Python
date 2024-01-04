"""
Escreva um algoritmo que leia certa quantidade de números e imprima o maior deles e quantas
vezes o maior número foi lido. A quantidade de números a serem lidos deve ser fornecida pelo 
usuário.
"""


from random import randint
qnt=0

num=int(input("Digite a quantidade de vezes que deseja: "))
lista=[]
for e in range (num):
    lista.append(randint(0,10))
for e in lista:
    if e == max(lista):
        qnt+=1
print(f"O maior número é {max(lista)}, aparece {qnt} vezes")