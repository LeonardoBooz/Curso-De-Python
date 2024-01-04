"""
Faça um programa que leia o valor da hora de trabalho (em reais) e número de horas trabalhadas no mês.
Imprima o valor a ser pago ao funcionario. adicionado 10% sobre o valor calculado.
"""

valor_das_horas=float(input("Digite o valor das horas em reais: "))
quant_de_horas=float(input("Digite o número de horas trabalhas: "))
total=(valor_das_horas*quant_de_horas)
print(f"O valor a ser pago ao funcionário será de: R${(total*0.10)+total}")
