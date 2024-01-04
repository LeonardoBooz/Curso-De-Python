'''
Escreva um programa que leia o numero de habitaates de uma determinada cidade, o valor do kwh, e
para cada habitante enre com os seguintes dados: Conjunto d o mês e o cófigodo consumidor
'''


residencia=[]
comercio=[]
industria=[]
cont=False
while cont == False:
    opc=int(input("Escolha entre as opções abaixo:\n"+
                "1-Residencia\n"+
                '2-Comercio\n'+
                '3-Industria\n'+
                '4-Ver o total\n'+
                '5-Sair\n'))
    if opc == 1:
        input("Digite o código da unidade consumidora")
        gasto_kwh=float(input("digite quando foi gasto: "))
        residencia.append(gasto_kwh)
    elif opc == 2:
        gasto_kwh=float(input("digite quando foi gasto: "))
        comercio.append(gasto_kwh)
    elif opc == 3:
        gasto_kwh=float(input("digite quando foi gasto: "))
        industria.append(gasto_kwh)
    elif opc == 4:
        print(f"O total gasto por residencias foi de: {sum(residencia)*0.8}\n"+
              f"O maximo: {max(residencia)}, o minimo: {min(residencia)}, e a média: {sum(residencia)/len(residencia)}")
        print(f"O total gasto por comercio foi de: {sum(comercio)*0.8}\n"+
              f"O maximo: {max(comercio)}, o minimo: {min(comercio)}, e a média: {sum(comercio)/len(comercio)}")
        print(f"O total gasto por industria foi de: {sum(industria)*0.8}\n"+
              f"O maximo: {max(industria)}, o minimo: {min(industria)}, e a média: {sum(industria)/len(industria)}")
    elif opc == 5:
        break