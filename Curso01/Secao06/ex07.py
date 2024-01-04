"""
Faça um programa que leia 10 inteiros positivos, ignorando não positivos, e imprima sua média.
"""
num=[]
for e in range(1,11):
    numero=int(input(f"Digite um número {e}/10: "))
    if numero >= 0:
        num.append(numero)
print(f'Total={sum(num)} e media={sum(num)/10}')