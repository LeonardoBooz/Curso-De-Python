"""
Faça um programa que leia um conjunto não determinado de valores, um de cada vez, e escreva
para cada um dos valores lidos, o quadrado,  cubo e a raiz quadrada. Finalize a entrada
de dados com um valor negativo ou zero.
"""
import math

cont=False
while cont == False:
    numero=int(input("Digite um número:"))
    if numero <= 0:
        cont=True
    else:
        print(f"Valor ao quadrado {numero**2} valor ao cubo {numero**3} e a raiz quadrada {math.sqrt(numero)}")