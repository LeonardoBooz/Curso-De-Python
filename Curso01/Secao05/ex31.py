"""
Faça um programa que receba a altura e o peso de uma pessoa. De acordo com
a tabela a seguir, verifique e mostre qual a classificação dessa pessoa.
"""

altura=float(input("Insira sua altura: "))
peso=float(input("Insira seu peso: "))

if altura < 1.2:
    if peso > 0 and peso <= 60:
        print("Sua classificação é A")
    elif peso > 60 and peso <= 90:
        print("Sua classificação é D")
    elif peso > 90:
        print("Sua classificação é D")
    else:
        print("Peso invalido!")
if altura >= 1.2 and altura <= 1.7:
    if peso > 0 and peso <= 60:
        print("Sua classificação é B")
    elif peso > 60 and peso <= 90:
        print("Sua classificação é E")
    elif peso > 90:
        print("Sua classificação é H")
    else:
        print("Peso invalido!")
if altura > 1.7:
    if peso > 0 and peso <= 60:
        print("Sua classificação é C")
    elif peso > 60 and peso <= 90:
        print("Sua classificação é F")
    elif peso > 90:
        print("Sua classificação é I")
    else:
        print("Peso invalido!")