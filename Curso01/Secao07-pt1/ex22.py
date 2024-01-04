"""
Faça um programa que leia dois vetores de 10 posições e calcule outro vetor
contendo, nas posições pares os valores do primeiro e nas posições impares os
valores do segundo.
"""
vetor_a='a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'
vetor_b='b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'
vetor_c=[]
for a, b in zip(vetor_a, vetor_b):
    vetor_c.append(a)
    vetor_c.append(b)
print(vetor_c)