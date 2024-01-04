"""
Faça um programa que calcule a área de um triângulo, cuja base e altura são fornecidas
pelo usuário. Esse programa não pode permitir a entrada de dados invalidos, ou seja,
medidas menores ou iguais a 0.
"""


base=float(input("Digite o valor da base: "))
altura=float(input("Digite o valor da base: "))
if base == 0 or altura == 0:
    print("Insira dados maiores que 0!")
else:
    area=(base*altura)/2
    print(f"O valor de area do triângulo é: {area}")