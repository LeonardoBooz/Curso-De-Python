"""
Faça um programa que leia dois vetores de 10 elementos. Crie um vetor que seja a união
entre os 2 vetores anteriores, ou seja, que contém os números dos dois vetores
"""
tupla= 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
tupla2=tupla[::-1]
tupla3=tupla+tupla2
print(set(tupla3))