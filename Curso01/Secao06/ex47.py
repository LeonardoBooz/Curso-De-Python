"""
Faça um programa que apresente um menu de opções para o cálculo das seguintes operações
entre dois número:
"""


def pede_numero():
    lista=[]
    for e in range(2):
        num=int(input(f'Digite {e+1} número:'))
        lista.append(num)
    return lista


cont=False
while cont == False:
    opc=int(input('Escolha entre as opções abaixo:\n'+
              '(1)-Adição\n'+
              '(2)-Subtração\n'+
              '(3)-Multiplicação\n'+
              '(4)-Divisão\n'+
              '(5)-Saída\n'))
    if opc == 1:
        lista=pede_numero()
        print(f'Resultado da operação: {lista[0]+lista[1]}')
        print("===========================================")
    elif opc == 2:
        lista=pede_numero()
        print(f'Resultado da operação: {lista[0]-lista[1]}')
        print("===========================================")
    elif opc == 3:
        lista=pede_numero()
        print(f'Resultado da operação: {lista[0]*lista[1]}')
        print("===========================================")
    elif opc == 4:
        lista=pede_numero()
        print(f'Resultado da operação: {lista[0]/lista[1]}')
        print("===========================================")
    elif opc == 5:
        break
    else:
        print('Opção invalida!')