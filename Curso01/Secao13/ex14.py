from datetime import date


hoje = str(date.today()).split('-')[::-1]

with open(r'C:\Curso\Curso01\Secao13\nomes_data_nascimento.txt') as data:
    lista_pessoas = data.read().split('\n')

lista=[]
for a in lista_pessoas:
    nome, data, ds = a.split(', ')
    data = data.split('/')
    dia, mes, ano = data
    dia_h, mes_h, ano_h = hoje

    dia, mes, ano = int(dia), int(mes), int(ano)
    dia_h, mes_h, ano_h = int(dia_h), int(mes_h), int(ano_h)

    if dia > dia_h and mes > mes_h or dia > dia_h and mes == mes_h:
        idade = (ano_h-1)-ano
    else:
        idade = ano_h-ano
    lista.append(f'{nome}, {idade}, \n')
with open(r'C:\Curso\Curso01\Secao13\nome_idade.txt', 'w') as arquivo:
    for a in lista:
        arquivo.write(a)
