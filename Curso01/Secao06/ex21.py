"""
Faça um programa que receba dois números. Calcule e mostre:
    a soma dos números pares desse intervalo de números, incluindo os números digitados
    a multiplicação dos números impares desse intervalo, incluindo os digitados.
"""

num=int(input("Digite o nº1: "))
num2=int(input("Digite o nº1: "))
lista=[]
somar_par=0
multiplicacao_impar=0

for e in range(num, num2+1):
    if e%2==0:
        somar_par+=e
    else:
        multiplicacao_impar+=e
print(somar_par, multiplicacao_impar)