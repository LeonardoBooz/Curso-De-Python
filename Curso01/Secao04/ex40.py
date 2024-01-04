"""
Uma empresa contrata um encanador por R$30 por dia. Faça um programa que 
solicite o número de dias trabalhados pelo encanador e imprima a quantia 
liquida que deverá ser paga, sabendo que são descontador 8% de imposto de renda
"""
dias=float(input("Digite a quantidade de dias trabalhados: "))
valor_liquido=dias*30-2.4
print(f"O sálario liquído será de: R${valor_liquido}")