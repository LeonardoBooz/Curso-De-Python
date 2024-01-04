"""
Faça um programa que leia 10 números e escreva o menor valor lido e o maior valor lido
"""
num=[]
for e in range(1,11):
    num.append(int(input(f"Digite um número {e}/10: ")))
print(f'O maior valor é, {max(num)}, e o menor é, {min(num)}')