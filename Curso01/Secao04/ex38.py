"""
Leia o sálario de um fúncionario. Calcule e imprima o valor do novo sálario, 
sabendo que ele recebeu um aumento de 25%
"""


num=float(input("Digite o sálario que receberá aumento: "))
print(f"O valor do novo sálario é: R${round(num+(num*0.25),2)}")