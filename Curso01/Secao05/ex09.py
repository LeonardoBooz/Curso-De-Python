"""
Leia o sálario de um trabalhador e o valor da prestação de um emprestimo. 
Se a prestação for maior que 20% do sálario imprima: 'Emprestimo não concedido',
caso contrario imprima: 'Emprestimo concedido'
"""


salario=float(input("Digite o sálario: "))
prestacao=float(input("Digite o valor da prestação: "))

if prestacao > (salario*0.2):
    print("Empresimo não concedido")
else:
    print("Emprestimo concedido")