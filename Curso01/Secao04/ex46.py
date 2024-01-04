"""
Faça um programa que leia um número inteiro positivo de trÊs digitos(de 0 a 999).
Gere outro número formado pelos digitos invertidos do número lido.
"""


num=input("digite um número de três digitos: ")
numero=int(str(num)[::-1])
print(numero)