"""
Receba o salário de um funcionário . Calcule e imprima o salário a receber, sabendo-se que esse funcioário
tem uma gratificação de 5% sobre o salário-base. Além disso, ele paga 7% de imposto sobre o salario-base.
"""

salario=float(input("Digite o salário a ser calculado: "))
salario_liq=((salario*0.05)+salario)-salario*0.07
print(f"O salario liquido será de: R${salario_liq}")