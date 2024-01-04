import os 
from time import sleep


base_dados_registros = r'C:\Curso\Curso01\base_dados_ex29.txt', 'base_dados_ex29.txt'

def verifica_existencia_base_dados(base_dados):#Feito, validado
    if base_dados not in os.listdir(r'C:\Curso\Curso01\Secao13'):
        return False
    else:
        return True

def criar_arquivo_dados(base_dados):
    if verifica_existencia_base_dados(base_dados) == False:
        with open(base_dados, 'w') as arq:
            return 'Base de dados criada'

def incluir_registro(base_dados, codigo, nome_vendedor, valor_venda, mes):
    with open(base_dados, 'a') as arq:
        arq.write(f"{codigo}, {nome_vendedor}, {valor_venda}, {mes}\n")
        return 'Registro adicionado a base de dados'
    
def excluir_linha(base_dados, substituto):
    linhas = leitura_arquivo(base_dados)
    with open(base_dados, 'w') as arq:
        for linha_texto in linhas:
            if linha_texto == substituto:
                linhas.pop(linhas.index(linha_texto))
        linhas = list(map(lambda x: f'{x}\n', linhas))
        arq.writelines(linhas)

def alterar_valor_venda(base_dados, substituido, substituto = '', exatidao = True):
    linhas = leitura_arquivo(base_dados)
    with open(base_dados, 'w') as arq:
        for linha_texto in linhas:
            if linha_texto == substituido and exatidao:
                linhas[linhas.index(linha_texto)] = substituto
            else:
                if linha_texto in substituido:
                    linhas[linhas.index(linha_texto)] = substituto
        linhas = list(map(lambda x: f'{x}\n', linhas))
        arq.writelines(linhas)
    return 'Alterado com sucesso...'


def leitura_arquivo(arquivo):
    try:
        with open(arquivo) as arq:
                linhas = arq.readlines()
                for linha in linhas:
                    if '\n' in linha or '\r' in linha:
                        linhas[linhas.index(linha)] = linha[:-1]
                    if '\n' in linha and '\r' in linha:
                        linhas[linhas.index(linha)] = linha[:-3]
        return linhas
    except FileNotFoundError:
        return 'Arquivo inexistente'

def retorno_registros(base_dados):
    linhas = leitura_arquivo(base_dados)
    linhas = list(map(lambda x: x.split(', '), linhas))
    for linha in linhas:
        cod, nome, valor_venda, mes = linha
        mes = int(mes)
        valor_venda = float(valor_venda)
        if mes == 1:
            mes = 'Jan'
        elif mes == 2:
            mes = 'Fev'
        elif mes == 3:
            mes = 'Mrç'
        elif mes == 4:
            mes = 'Abrl'
        elif mes == 5:
            mes = 'Maio'
        elif mes == 6:
            mes = 'Jnh'
        elif mes == 7:
            mes = 'Jlh'
        elif mes == 8:
            mes = 'Agst'
        elif mes == 9:
            mes = 'Stmbr'
        elif mes == 10:
            mes = 'Otbr'
        elif mes == 11:
            mes = 'Nvmbr'
        elif mes == 12:
            mes = 'Dzmbr'
        print(f'Código: {cod}, Vendedor: {nome}, Valor de venda em {mes}: R${valor_venda}')

def pesquisa_por_codigo(base_dados, cod):
    linhas = leitura_arquivo(base_dados)
    registros_possiveis_l = []
    for linha in linhas:
        if cod in linha:
            registros_possiveis_l.append(linha)
    registros_possiveis = tuple(registros_possiveis_l)
    del registros_possiveis_l
    return registros_possiveis

def listar_registros_de_mesmo_código(base_dados, cod):
    ld1 = pesquisa_por_codigo(base_dados, cod)
    ld2 = []
    e=0
    for registro in ld1:
        e+=1
        ld2.append(f'({e}){registro}')
    print(f'Registros possiveis:\n{ld2}')
    del ld1, ld2

def excluir_base_dados(base_dados):
    os.remove(base_dados)

def sair():
    print ('Encerrando')
    sleep(3)
    exit()

while True:
    os.system('cls')
    print('===============================================================')
    print('===============================================================')
    print('=======================Registro=de=Vendas======================')
    print('===============================================================')
    print('===============================================================')
    opc = int(input('OPÇÔES:\n--------\n(1)Criar o arquivo de dados | (4)Alterar valor de venda\n(2)Incluir registro         | (5)Mostrar registros\n(3)Excluir Registro         | (6)Apagar arquivo de dados\n(7)Sair:>'))
    if opc == 1:
        print(criar_arquivo_dados(base_dados_registros[0]))
        sleep(2)

    elif opc == 2:
        nome_dados = ('código do Vendedor', 'nome do vendedor', 'valor total de vendas', 'mes de referência')
        dados = list(map(lambda x: input(f"Digite o {x}"), nome_dados))
        cod, nome, valor_venda, mes = dados
        incluir_registro(base_dados_registros[0], cod, nome, valor_venda, mes)

    elif opc == 3:
        cod = input('Excluir registro pelo código:\nDigite o código:>')
        registros = pesquisa_por_codigo(base_dados_registros[0], cod)
        listar_registros_de_mesmo_código(base_dados_registros[0], cod)
        indice = int(input('Digite qual deseja apagar:>'))
        indice -= 1
        print(excluir_linha(base_dados_registros[0], registros[indice]))

    elif opc == 4:
        cod = input('Alterar valor de venda pelo código:\nDigite o código:>')
        registros = pesquisa_por_codigo(base_dados_registros[0], cod)
        registros = [*registros]
        listar_registros_de_mesmo_código(base_dados_registros[0], cod)
        indice = int(input('Digite qual deseja alterar:>'))
        indice -= 1
        novo_registro = float(input(f'Digite o novo valor de venda de {cod}:>'))
        ld1 = registros[indice].split(', ')
        ld1[2]=str(novo_registro)
        novo_registro = ', '.join(ld1)
        del ld1
        alterar_valor_venda(base_dados_registros[0], registros[indice], novo_registro)
        print(f"Alteração realizada com sucesso!\nRegistro velho:{registros[indice]}\nNovo registro:{novo_registro}")
    elif opc == 5:
        retorno_registros(base_dados_registros[0])
        input("Digite * para voltar...")

    elif opc == 6:
        os.remove(base_dados_registros[0])
        print('Todos os registros foram deltados com sucesso...')
        sleep(2)

    elif opc == 7:
        sair()