"""
Programa de estacionamento
"""
cont=False
lista_hora=[]
lista_sequencia=[1,2]


def cobranca(perm):
    min=perm
    apagar=0
    passou1= False
    passou2= False
    while min != 0:
        if min < 60:
            min-=min
            if passou2 == True:
                apagar+=1.4
            elif passou1 == True:
                apagar+=2
            else:
                apagar+=1
            break
        if min >= 60 and min <= 120 and passou1 == False and passou2 == False:
            min-=60
            apagar+=1.0
        elif min > 120 and min <= 240 and passou1 == False or passou2 == True:
            min-=60
            apagar+=1.4
            passou2=True
        else:
            min-=60
            apagar+=2.0
            passou1=True
    return apagar
def converte_minuto(hora):
    lista_hora=hora.split(":")
    total_de_minutos=0
    for e, f in zip(lista_hora, lista_sequencia):
        g=int(e)
        if f == 1:
            total_de_minutos += g*60
        else:
            total_de_minutos += g
    return total_de_minutos


hora=input("Digite a hora de entrada neste formato, (00:00) ")
hora_entrada=converte_minuto(hora)
hora=input("Digite a hora de saída neste formato, (00:00) ")
hora_saida=converte_minuto(hora)
if hora_saida < hora_entrada:
    perm=hora_saida+(1440-hora_entrada)
    print(cobranca(perm))
elif hora_saida == hora_entrada:
    print(cobranca(1440))
else:
    perm=hora_saida-hora_entrada
    #cobranca(perm)
    print(cobranca(perm))