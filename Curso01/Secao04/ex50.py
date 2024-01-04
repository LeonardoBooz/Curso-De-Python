"""
Implemente um programa que calcule o ano de nascimento de uma pessoa a partir 
de sua idade e do ano atual
"""


from datetime import datetime

idade=int(input("Informe sua idade:"))
ano=int(str(datetime.now())[0:4])
print(f"Essa pessoa nasceu no ano de {ano-idade}")