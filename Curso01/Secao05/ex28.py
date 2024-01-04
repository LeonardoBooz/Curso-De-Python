"""
Faça um programa que leia três números inteiros positivos e efetue 
o cálculo de uma das seguintes médias de acordo com um valor númerico digitado 
pelo usuário
"""


import math


def opcao_media(opc, lista_dados):
    if opc == 1: 
        print(f'Média Geometrica {pow((lista_dados[0]*lista_dados[1]*lista_dados[2]), 1/3)}')
    elif opc == 2:
        print(f'Média Ponderada {(lista_dados[0]+2*lista_dados[1]+3*lista_dados[2])/6}')
    elif opc == 3:
        print(f'Média Harmônica {3/((1/lista_dados[0])+(1/lista_dados[1])+(1/lista_dados[2]))}')
    else:
        print(f'Média Aritmética {(lista_dados[0]+lista_dados[1]+lista_dados[2])/3}')


lista_ord=['primerio', 'segundo', 'terceiro']
lista_dados=[]
opc=int(input("Entre as opções abaixo escolha:\n"+
              '1-Geométrica\n'+
              '2-Ponderada\n'+
              '3-Harmônica\n'+
              '4-Aritmética\n'))
if opc == 1 or opc == 2 or opc == 3 or opc == 4:
    for e in lista_ord:
        num=int(input(f'Escreva o {e}: '))
        lista_dados.append(num)
    opcao_media(opc, lista_dados)
else:
    print("Opção invalida!")

