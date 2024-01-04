"""
Leia a nota e o número de faltas de um aluno, e escreva seu conceito.
De acordo com a tabela abaixo, quando o aluno tem mais de 20 faltas ocorre uma redução de conceito.
"""

lista_nome_dado=['a nota', 'o número faltas']
lista_dados=[]

for e in lista_nome_dado:
    num=float(input(f"Digite {e}: "))
    lista_dados.append(num)

if lista_dados[0] >= 9 and lista_dados[0] <=10:
    if lista_dados[1] <= 20:
        print("O conceito do aluno é A")
    else:
        print("O conceito do aluno é B")
elif lista_dados[0] >= 7.5 and lista_dados[0] <=8.9:
    if lista_dados[1] <= 20:
        print("O conceito do aluno é B")
    else:
        print("O conceito do aluno é C")
elif lista_dados[0] >= 5 and lista_dados[0] <=7.4:
    if lista_dados[1] <= 20:
        print("O conceito do aluno é C")
    else:
        print("O conceito do aluno é D")
elif lista_dados[0] >= 4 and lista_dados[0] <=4.9:
    if lista_dados[1] <= 20:
        print("O conceito do aluno é D")
    else:
        print("O conceito do aluno é E")
else:
    print("O conceito do aluno é E")