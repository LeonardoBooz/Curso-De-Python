
nome_arquivo = input('Digite o nome do seu arquivo: ')
contatos=[]
while True:
    nome = input('Digite o nome do contato: ')
    telefone = input('Digite o nº de telefone: ')
    if telefone == '0':
        break
    else:
        contatos.append(f'Nome: {nome}, telefone: {telefone}\n')
with open(rf'C:\Curso\Curso01\Secao13\{nome_arquivo}.txt', 'w') as arquivo:
    for a in contatos:
        arquivo.write(a)