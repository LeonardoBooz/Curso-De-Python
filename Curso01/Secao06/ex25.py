"""
Faça um programa que some todos os números naturais abaixo de 1000 que são multiplus
de 3 ou 5.
"""
total_3=0
total_5=0
for e in range (1000):
    if e*3 < 1000:
       total_3+=e
    if e*5 < 1000:
       total_5+=e
print(total_3, total_5)