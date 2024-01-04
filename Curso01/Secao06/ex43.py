"""
Faça um programa que leia um número inderminado de idades de indivíduos (pare quando 
for informada a idade 0), e calcule a média desse grupo.
"""


cont=False
lista=[]
while cont == False:
    idade=int(input("Informe sua idade: "))
    lista.append(idade)
    if idade <= 0:
        print("programa encerrado")
        print(f"A média de idade deste grupo é {sum(lista)/len(lista)}")