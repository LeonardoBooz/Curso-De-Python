"""
Faça um program que leia um número inteiro N e depois imprima os N primeiros
números naturais ímpares
"""
num=int(input("Digite um número inteiro: "))
for e in range(1, num, 2):
    print(e)