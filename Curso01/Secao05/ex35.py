"""
Leia uma data e determine se ela é valida. Ou seja, verifique se o mês esta entre 1 e 12,
e se o dia existe naquele mês. Note que Fevereiro tem 29 dias em anos bissextos, e 28
dias em anos não bissextos 
"""


data=input("Digite uma data valida: ")
try:
    dia=int(data[0:2])
except ValueError:
    dia=int(data[0:1])
try:
    mes=int(data[3:5])
except ValueError:
    try:
        mes=int(data[3:4])
        
    except ValueError:
        mes=int(data[2:3])
try:
    ano=int(data[6:10])
except ValueError:
    try:
       ano=int(data[5:9])
    except ValueError:
        ano=int(data[4:9])
        
bissexto=False
ano_corrigido=0

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
