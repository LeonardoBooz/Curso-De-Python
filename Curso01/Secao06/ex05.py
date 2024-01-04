"""
Faça um programa que peça ao usuário para digitar 110 valores e some-os
"""
num=[]
for e in range(1,11):
    num.append(int(input(f"Digite um número {e}/10: ")))
print(f'Total={sum(num)}')