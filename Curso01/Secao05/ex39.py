"""
Calculadora de aumentos
"""

salario=float(input("Digite o sálario"))
tempo_servico=float(input("Digite o tempo de serviço"))

if salario <= 500:
    reajuste=+salario+salario*0.25
elif salario > 500 and salario <= 1000:
    reajuste=+salario+salario*0.20
elif salario > 1000 and salario <=1500:
    reajuste=+salario+salario*0.15
elif salario > 1500 and salario <=2000:
    reajuste=+salario+salario*0.10
else:
    reajuste=salario
if tempo_servico >= 1 and tempo_servico <= 3:
    reajuste+=100
elif tempo_servico >= 4 and tempo_servico <= 6:
    reajuste+=200
elif tempo_servico >= 7 and tempo_servico <= 10:
    reajuste+=300
elif  tempo_servico > 10:
    reajuste+=500
if salario > 2000 or tempo_servico < 1:
    print("Não tem direito a nada!")
else:
    print(f"Salário reajustado: {reajuste}")