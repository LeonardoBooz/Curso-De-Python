"""
Escreva um programa que leia um número inteiro maior do que zero e devolva,
na tela, a soma de todos os seus algarismos. Se o número lido for maior do que zero,
o programa terminará com a mensagem 'número invalido'
"""

num=input("Digite qualquer número inteiro maior que 0: ")
if int(num) < 1:
    print("Número invalido!")
    exit() 
total=0
for e in num:
    print(e)
    total += int(e)
print(f"A soma dos numeros de {num} é {total}")