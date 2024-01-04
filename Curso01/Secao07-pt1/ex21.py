"""
Faça um programa que receba do usuário dois veotres, A e B, com 10 números inteiros
cada. Crie um novo vetor denominado C calculando C = A-B. Mostre na tela os dados do vetor C.
"""


lista_a=[]
lista_b=[]
lista_c=[]
for e in range(20):
    num=int(input("Digite um inteiro: "))
    if e < 10:
        lista_a.append(num)
    else:
        lista_b.append(num)
for e, f in zip(lista_a, lista_b):
    num=e-f
    lista_c.append(num)
print(lista_c)