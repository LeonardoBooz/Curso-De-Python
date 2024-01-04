"""
 Faça um programa que leia o valor de um produto e imprima o valor com desconto, 
tendo em vista que o desconto foi de 12%
"""


import math

num=float(input("Digite o valor do produto:"))
print(f"Este produto com 12% de desconto, custará: R${round(num-(num*0.12),2)}")