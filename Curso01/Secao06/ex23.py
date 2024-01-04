"""
Faça um algoritimo que leia um número positivo e imprima seus divisores
"""
num=int(input("Digite um número positivo: "))
for e in range(1,10000):
    if num%e == 0:
        print(e)
