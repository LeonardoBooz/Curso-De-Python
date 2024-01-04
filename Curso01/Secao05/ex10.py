"""
Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal, 
utilizando as seguintes fórmulas(onde h corresponde á altura)
"""


altura=float(input("Digite sua altura em metros: "))
sexo=input("Digite seu sexo: ")
sexo.lower()

if sexo == 'masculino' or sexo == 'm':
    print(f"O peso ideal é de {round((72.7*altura)-58)}")
else:
    print(f"O peso ideal é de {round((62.1*altura)-44.7)}")