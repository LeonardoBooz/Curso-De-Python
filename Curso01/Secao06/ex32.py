'''
Faça um programa que simula o lançamento de dois dados, d1 e d2, n vezes, e tem como saída
o número de cada dado e relação entre eles(>,<,=) de cada lançamento.
'''


from random import randint
num=int(input("Digite quantas jogadas: "))

for e in range(1, num+1):
    d1=randint(1,6)
    d2=randint(1,6)
    if d1 > d2:
        print(f"{d1} é maior que {d2}")
    elif d1 < d2:
        print(f"{d2} é maior que {d1}")
    else:
        print(f"{d1} é igual a {d2}")
