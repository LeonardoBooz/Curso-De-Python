"""
Receba a altura do degrau de uma escada e a altura que o usuario deseja alcançar
subindo a escada. Calcule e mostre quantos degraus o usuario deverá subir para 
atingir seu objetivo.
"""

alt_degrau=float(input("Insira a altura do degrau em centimetros: "))/100
alt_desejada=float(input("Insira a altura que deseja ir em metros: "))
quant_degraus=round(alt_desejada/alt_degrau)
print(f"Você terá de subir {quant_degraus}")