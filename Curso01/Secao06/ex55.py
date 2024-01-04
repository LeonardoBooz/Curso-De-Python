"""Escreva um programa que leia um inteiro não negativo n e imprima a soma do n primeros número primos"""

num=int(input("Digite um número inteiro maior do que 1: "))
for e in range(1, num):
    if e/e==0:
        print(f"{e} é primo")
        