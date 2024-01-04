"""
Faça um programa para verificar se um determinado número inteiro é divisível
por 3 ou 5, mas não simultaneamente pelos dois.
"""

from random import randint

for _ in range(randint(0,1000)):
    num=randint(0,100)
    if num%3 == 0 and num%5 != 0:
        print(f"{num} É divisivel por 3")
    if num%3 != 0 and num%5 != 0:
        print(f"{num} É divisivel por 5")
