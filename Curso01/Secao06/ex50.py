"""
Chico tem 1.5 metro e cresce 2 centimetros por ano, enquanto Zé tem 1.10 metros
e cresce 3 centimetros por ano. Escreva um programa que calcule e imprima quantos
anos seão necessários para que Zé seja maior que Chico.
"""


chico=150
ze=110

for e in range(1, 10000):
    chico+=2
    ze+=3
    if ze > chico:
        break
print(ze, chico)