"""Faça um programa que calcule o maior número palindromo feito apartir do produto de
dois números de 3 digitos.
"""


produto=0
lista=[]
for num1 in range(100, 1000):
    for num2 in range(100, 1000):
        produto=num1*num2
        if str(produto) == str(produto)[::-1]:
            lista.append(produto)
print(max(lista))
