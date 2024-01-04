import os
from time import sleep


nome_base_dados= (r'C:\Curso\Curso01\Secao13\contatos_teste.bin', 'contatos_teste.bin')

def verifica_existencia_base_dados():#Feito, validado
    if nome_base_dados[1] not in os.listdir(r'C:\Curso\Curso01\Secao13'):
        return False
    else:
        return True
def cria_base_dados():#Feito, validado
    with open(nome_base_dados[0], 'wb') as arq:
        pass

#Para escrever no arquivo seguir este modelo para passar no construtor do metodo: {'chave': ['telefone', 'aniversario']}    
def escreve_base_dados(dic, param=True):#Feito
    nome = list(dic.keys())[0]
    telefone, aniversario = dic[nome]
    if verifica_existencia_base_dados() and param:
        if verifica_valores_repetidos_base_dados(dic):
            with open(nome_base_dados[0], 'ab') as arq:
                arq.write(f'{nome}, {telefone}, {aniversario}\n'.encode())
                return f'{nome} adicionado com sucesso'
        else:
            return f'{nome} ou {telefone} ja existe nos contatos'
    else:
        with open(nome_base_dados[0], 'wb') as arq:
            arq.write(f'{nome}, {telefone}, {aniversario}\n'.encode())
            return f'{nome} adicionado com sucesso'

#recebe um dicionario com o nome, telefone e aniversario que se pretende adicionar    
def verifica_valores_repetidos_base_dados(dic):#Feito, validado
    nome = list(dic.keys())[0]
    telefone = dic[nome][0]
    dados = le_base_dados()
    if nome in list(dados.keys()):
        return False
    for a in dados.keys():
        if telefone in dados[a][0]:
            return False
    else:
        return True
        
def le_base_dados():#Feito, validado
    if verifica_existencia_base_dados():
        with open(nome_base_dados[0], 'rb')as arq:
            dados = arq.read().decode()
            contatos = list(map(lambda x: x.split(', '), dados.split('\n')))
            contatos.pop(-1)
            dic={}
            for a in contatos:
                nome, telefone, aniversario = a
                dic[nome] = [telefone, aniversario]
            return dic
    else:
        return f'Não foi possivel encontrar o arquivo {nome_base_dados[1]}'
    
def remove_contato(nome):#feito
    dados = le_base_dados()
    if nome in list(dados.keys()):
        del dados[nome]
        for chaves in dados:
            a = dados[chaves]
            escreve_base_dados({chaves: a},param=False)
        return 'Removido com sucesso'
    else:
        return 'Nome não encontrado'
    
def pesquisar_contato(nome):
    dados = le_base_dados()
    #procura pelo nome fornecido e retorna uma tupla com os que tenhão os mesmos caracteres ou parte deles
    chaves = [*dados.keys()]
    nomes_temp = []
    for a in chaves:
        if nome.lower() in a.lower():
            nomes_temp.append(a)
    nomes = tuple(nomes_temp)
    del nomes_temp
    return nomes

def retorna_aniversariante_mes(mes_comp):
    dados = le_base_dados()
    aniversariante_temp=[]
    for chaves in dados:
        a = dados[chaves]
        mes_aniv = a[1].split('/')[1]
        if mes_aniv != '^':
            if int(mes_aniv) == int(mes_comp):
                aniversariante_temp.append(chaves)
    aniversariante = tuple(aniversariante_temp)
    del aniversariante_temp
    return aniversariante


while True:
    os.system('cls')
    print('===============================================================')
    print('===============================================================')
    print('====================Contatos=Telefonicos=======================')
    print('===============================================================')
    print('===============================================================')
    opc = int(input('OPÇÔES:\n--------\n(1)Inserir um novo contato | (4)Listar todos os contatos\n(2)Remover contato         | (5)Procurar Contato\n(3)Aniversariantes do mês  | (6)Sair\n:>'))
    if opc == 1:
        print("Preencha o formulario abaixo:")
        print("=============================")
        nome = input('Digite o nome: ')
        telefone = input('Digite o telefone: ')
        aniversario = input('Digite a data de nascimento: ')
        print(escreve_base_dados({nome.title():[telefone, aniversario]}))
        sleep(2)
    elif opc == 2:
        print('Remover contato')
        print("=============================")
        nome = input('Digite o nome: ')
        print(remove_contato(nome.title()))
        sleep(2)
    elif opc == 3:
        mes = input("Qual mês deseja ver os aniversariantes")
        retorna_aniversariante_mes(mes)
        input("Digite * para voltar")
    elif opc == 4:
        with open(nome_base_dados[0], 'rb') as arq:
            print(arq.read().decode())
            input("Digite * para voltar")
    elif opc == 5:
        nome = input("Digite o nome ou parte dele")
        print(pesquisar_contato(nome))
        esc = input('Escolha um destes, escrevendo o nome completo:')
        dados = le_base_dados()
        print(f'Nome: {esc}, telefone: {dados[esc][0]}, aniversarios: {dados[esc][1]}')
        input("Digite * para voltar")
    elif opc == 6:
        break