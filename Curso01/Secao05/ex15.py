"""
Usando switch, escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia
da semana correspondente a este número. Isto é, domingo se 1, segunda-feira, e assim
por diante.
"""


def switch(dia_semana):
    return{
        1:"Domingo",
        2:"Segunda",
        3:"Terça",
        4:"Quarta",
        5:"Quinta",
        6:"Sexta",
        7:"Sabado"
    }.get(dia_semana, "Opção inválida")


dia=int(input("Digite de 1 á 7 o dia da semana:"))
print(switch(dia))