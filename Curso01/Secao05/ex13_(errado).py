"""
Faça um algoritomo que calcule a média ponderada das notas de 3 provas. A primeira e
a segunda prova tem peso 1 e a terceira tem peso 2. Ao final, mostrar a média do aluno
e indicar se o aluno foi aprovado ou reprovado. A nota para aprovação deve ser igual 
ou superior a 60 pontos
"""


lista=[]
total=0

for e in range(3):
    num=float(input(f"Digite a nota da prova nº{e+1} "))
    if num > 2 or num < 0:
        print("nota invalida")
        exit()
    
    else:
        lista.append(num)
if sum(lista) > 4:
        print("O peso de uma nota foi excedido! ")
        exit()
for f in lista:
    total+=f*25
print(f"A média de pontos foi: {total}")