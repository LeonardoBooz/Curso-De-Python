"""
Escreva um algoritimo que leia um número inteiro entre 100 e 999 e imprima
na sáida cada um dos algarismos que compõem o número
"""


num=int(input("Digite um número de 100 á 999: "))
if num < 100 and num > 999:
    print("Número invalido!")
    exit()
for _, e in enumerate(str(num)):
    print(e)