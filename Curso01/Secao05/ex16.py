"""
Usando switch, escreva um programa que leia um inteiro entre 1 e 12 e imprima o mês
correspondente a este número. Isto é, janeiro se 1, fevererio se 2, e assim por diante.
"""
def switch(nu_mes):
    return{
        1:'Janeiro',
        2:'Fevereiro',
        3:'Março',
        4:'Abril',
        5:'Maio',
        6:'Junho',
        7:'Julho',
        8:'Agosto',
        9:'Setembro',
        10:'Outubro',
        11:'Novembro',
        12:'Dezembro'
    }.get(nu_mes, "Opção invalida")


num_mes=int(input("Digite de 1 á 12 o mês desejado "))
print(switch(num_mes))