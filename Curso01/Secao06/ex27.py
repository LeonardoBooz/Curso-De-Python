"""
Em matemática, o número harmônico designado por H(n) define-se como sendo a soma da série
harmônica. Faça um programa que leia um valor n inteiro e positivo e apresente o valor de H(n)
"""

num=int(input("Digite um número inteiro positivo: "))
h=1
for e in range(1, num +1):
    h+=1/e
print(h)