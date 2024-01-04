"""
Faça um programa que receba um número inteiro maior do que 1, e verifiqye se o númeo
fornecido  é primo ou não.
"""

num=int(input("Digite um número inteiro maior do que 1: "))
if num%num==0:
    print(f"{num} é primo")