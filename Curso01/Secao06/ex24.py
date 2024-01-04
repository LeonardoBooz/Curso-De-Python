"""
Escreva um programa que leia um número inteiro e calcule a soma de todos os divisores
deste número, com exceção dele próprio. Ex: a soma dos divisores do número 66 é 
1+2+3+6+11+22+33=78
"""
num=int(input("Digite um número positivo: "))
soma=0
for e in range(1,10000):
    if num%e == 0 and num != e:
        soma+=e
print(soma)