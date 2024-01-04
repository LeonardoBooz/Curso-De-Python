"""
Faça um programa que leia dois vetores de 10 elementos. Crie um vetor que seja a
intersecção entre os 2 vetores anteriores, ou seja, que contém apenas os números
que estão em ambos os vetores. Não deve conter números repetidos.
"""
vetor1=1, 343, 54, 43, 4, 62, 4, 6, 2, 45
vetor2=2, 343, 5, 3, 4, 3, 5, 6, 3, 23, 45
lista=[]
for e in vetor1:
    for f in vetor2:
        if e == f:
            lista.append(e)
print(set(lista))