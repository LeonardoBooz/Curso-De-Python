from datetime import date


nome_arquivo1 = input("digite o nome do arquivo de entrada: ")
nome_arquivo2 = input("digite o nome do arquivo de saída: ")
with open(f'{nome_arquivo1}.txt', 'w') as arquivo1:
    arquivo1.write('Larissa, 1988\nGabriel, 2000\nMariana, 1995\nLucas, 2008\nIsabela, 2015\nRafael, 2020')
ano_corrente = int(str(date.today()).split('-')[0])
print(ano_corrente)
with open(f'{nome_arquivo1}.txt') as arquivo1:
    arquivo1 = arquivo1.read().split('\n')
lista=[]
for a in arquivo1:
    nome, ano_nasc = a.split(', ')
    idade = ano_corrente - int(ano_nasc)
    if idade < 18:
        mensagem = 'menor de idade'
    elif idade > 18:
        mensagem = 'maior de idade'
    else:
        mensagem = 'entrando na maior idade'
    lista.append(f'{nome}, {mensagem}\n')
with open(f'{nome_arquivo2}.txt', '+w') as arquivo2:
    for a in lista:
        arquivo2.write(a)
with open(f'{nome_arquivo2}.txt') as arquivo2:
    print(arquivo2.read())