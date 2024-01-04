"""
Leia a altura e o raio de um cilindro circular e imprima o volume do cilindro.
O volume do cilindro circular pe calculado por meio da seguinte formula: V = 3.141592*raio²*altura.
"""

alt=float(input("Digite a altura do cilindro: "))
raio=float(input("Digite a raio do cilindro: "))

print(f"O volume deste cilindro é: {3.141592*(raio**2)*alt}")