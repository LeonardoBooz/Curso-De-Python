"""
Faça um programa que leia 2 notas de um aluno, verifique se as notas são validas
e exiba na tela a média destas notas. Uma nota valída deve ser, obrigatoriamente, 
um valor entre 0 e 10, onde caso a nota não possua um valor válido, este fato deve 
ser informado ao usuário e  o programa termina.
"""


con=False
lista=[]
while con == False:
    for e in range(2):
        nota=float(input(f"Digite a nota {e+1} "))
        if nota >= 0 and nota <= 10:
            lista.append(nota)
        else:
            print("Número invalido, programa encerrado!")
            con=True
            exit()
    print(f"A média das notas é: {(lista[0]+lista[1])/2}")