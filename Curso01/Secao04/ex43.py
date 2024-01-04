"""
Escreva um programa de ajuda oara vendedores. Apartir de um valor total lido, mostre:
    O total a pagar com desconto de 10%
    o valor de cada parcela, no parcelamento de 3x sem juros
    a comissão do vendedor, no caso da venda ser a vista(5% sobre o valor com desconto)
    a comissão do vendedor no caso da venda ser parcelada (5% sobre o valor total)
"""

valor=float(input("Digite o valor do produto: "))
valor_desconto=round(valor-(valor*0.10),2)
print(f"O valor do produto é: R${valor}\n"+ 
    f"A vista -10% OFF: R${valor_desconto}\n"+
    "-----------------------------------------------\n"+
    f"Ou em 3x sem juros de: R${round((valor/3),2)}\n"+
    "=======================================================\n"+
    f"Comissão vendedor se pago vista: {round((valor_desconto*0.05),2)}\n"+
    f"Comissão vendedor se pago a prazo: {round((valor*0.05),2)}"
    )