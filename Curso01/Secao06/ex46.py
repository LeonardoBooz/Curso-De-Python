"""
Faça um programa que gera um número aleatório de 1 a 1000. O usuário deve tentar
acertar qual número foi gerado, cada tentativa o programa deverá informar se o 
chute é menor ou maior que o número gerado. O programa acaba quano o usuário acertar
o número gerado. O programa deve informar em quantas tentativas o número foi descoberto.
"""


from random import randint

numero=randint(1, 1000)
cont=False
qnt_tentativas=0
while cont == False:
    qnt_tentativas+=1
    print(f'O ultimo número é {str(numero)[len(str(numero))-1]}')
    tentativa=int(input("Tente acertar o número gerado aleatóriamente de 1 á 1000!!!\n"))
    if tentativa < numero:
        diferenca=numero-tentativa
    else:
        diferenca=tentativa-numero
    if tentativa == numero:
        print("Parabéns, você acertou!!")
        cont=True
    elif diferenca <= 100:
        print("Esta muito quente!")
    elif diferenca > 100 and diferenca <= 300:
        print("Esta quente!")
    elif diferenca > 300 and diferenca <= 500:
        print("Esta frio!")
    elif diferenca > 500 and diferenca <= 700:
        print("Esta muito frio!")
    else:
        print("Nem perto!")
print(f"O número era {numero} e você tentou {qnt_tentativas} vezes")