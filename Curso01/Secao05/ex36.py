"""
Escreva um programa que, dado o valor da venda, imprima a comissão que deverá ser paga ao
vendedor. Para calcular a comussão.
"""

valor=int(input("Digite o valor da venda"))

if valor >= 100_000:
    valor_comi=(valor*0.16)+700
elif valor < 100_000 and valor >= 80_000:
    valor_comi=(valor*0.14)+650
elif valor < 80_000 and valor >= 60_000:
    valor_comi=(valor*0.14)+600
elif valor < 60_000 and valor >= 40_000:
    valor_comi=(valor*0.14)+550
elif valor < 40_000 and valor >= 20_000:
    valor_comi=(valor*0.14)+500
else:
    valor_comi=(valor*0.14)+400
print(f'O valor da comissão será de: {valor_comi}')