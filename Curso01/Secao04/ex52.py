"""
Três amigos jogaram na loteria. Caso eles ganhem, o premio dever ser repartido
proporcionalmente ao valor que cada um deu para a realização da aposta. Faça um programa
que leia quanto cada apostador investiu, o valor do premio, e imprima quanto cada um 
ganharia do premio com base no valor investido.
"""


lista_valor_aposta=[]

print("       Aposteitor 300       ")
valor_premio=float(input("Digite quanto é o valor do prêmio: "))
quant_apostadores=int(input("Em quantas pessoas o prêmio será divido"))
for e in range(quant_apostadores):
    valor_gasto=float(input(f"Quanto apostou o nº{e+1}? "))
    lista_valor_aposta.append(valor_gasto)
j=1
for i in lista_valor_aposta:
    print(f"O apostador nº{j} deverá receber a quantia de: R$"+
          f"{round(valor_premio*(i/sum(lista_valor_aposta)),2)}")
    j+=1