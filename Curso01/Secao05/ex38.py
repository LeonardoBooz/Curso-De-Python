

from datetime import datetime

data=input("Digite a data de nascimento neste formato DD/MM/AA: ").split("/")
dia=int(data[0])
mes=int(data[1])
ano=int(data[2])
ano_atual=str(datetime.now()).split('-')[1]
bissexto=False
ano_corrigido=0

if ano < 1903 and ano > int(ano_atual):
    print("Data invalida")
    exit()
if dia < 1 and dia > 31:
    print("Data invalida")
    exit()
elif mes < 1 and mes > 12:
    print("Data invalida")
    exit()
if len(str(ano)) == 2:
    ano_corrigido=int("20"+str(ano))
else:
    ano_corrigido=ano
if ano_corrigido%4 == 0 and ano_corrigido%100 != 0:
    bissexto=True
if mes == 4 or mes == 6 or mes == 9 or mes == 11:
    if dia <= 30:
        print('Data valida')
    else:
        print('Data invalida')
elif mes == 2:
    if bissexto == True:
        if dia <= 29:
            print('Data valida')
        else:
            print('Data invalida')
    else:
        if dia <= 28:
            print('Data valida')
        else:
            print('Data invalida')
else:
    if dia <= 31:
        print('Data valida')
    else:
        print("Dia inválido")
