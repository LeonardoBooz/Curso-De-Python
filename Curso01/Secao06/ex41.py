"""
Faça um programa que calcula a associação em paralelo de dois resistores R1 e R2
fornecidos pelo usuário via teclado. O programa fica pedindo estes valores e calculando
até que o usuário entre com um valor para resistencia igual a zero.
"""


cont=False
while cont == False:
    r1=int(input("Digite a resistência do primeiro resistor: "))
    r2=int(input("Digite a resistência do segundo resistor: "))
    resistencia=(r1*r2)/(r1+r2)
    print(f"associação em paralelo de dois resistores é: {resistencia}")
    if resistencia == 0:
        cont=True
