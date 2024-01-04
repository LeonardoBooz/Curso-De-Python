"""
Escreva um programa que leia um número inteiro positivo n e em seguida imprima n, 
linhas de comando triangulo de floyd. Para m=6, tempos
"""
num=21
numero=0
for e in range(1, num):
    print()
    for _ in range(e):
        numero+=1
        print(numero, end='')
        if num == numero:
            exit()
