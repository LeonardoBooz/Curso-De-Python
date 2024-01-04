"""
Escreva um programa que verifique quais números entre 1000 e 9999(inclusive) possuem a 
proprieda seguinte: a soma dos dois digitos de mais baixa ordem com os dois digitos
de mais alta ordem elevada ao quadrado é igual ao próprio número.
"""

for e in range(1000, 9999):
    num=str(e)
    total=int(num[0:2])+int(num[2:4])
    if e == total**2:
        print(f"A soma de {e} ao quadrado é igual a ele mesmo")