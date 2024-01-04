import os
from time import sleep


base_dados = [r'C:\Curso\Curso01\Secao13\base_dados.bin', 'base_dados.bin']
mensagem_sucesso ='Produto Adicionado!'
mensagem_sem_base_dados = 'Você não possue estoque!'
produtos = 'Banana: 1010, Arroz: 2020, Feijão: 3030, Melancia: 4040\nDigite * para voltar...'


def saida_produto():
    if verifica_existencia_arquivo(base_dados[1]):
        with open(base_dados[0], 'rb') as arq:
            lista = arq.read().decode().split('\n')
            lista.pop(0)
            lista.pop(-1)
            lista1 = list(map(lambda x: x.split(', '), lista))
            codigo_quant = {}
        for a in lista1:
            quant = int(a[2][:-3])
            try:
                codigo_quant[a[0]]+=quant
            except KeyError:
                codigo_quant[a[0]]=quant
        
        print()
    else:
        print(mensagem_sem_base_dados)

def entrada_produto():
    while True:
        os.system('cls')
        print(produtos)
        cod_prdt = input('Digite o código do produto: ')
        lista=list(map(lambda x: x.split(': ') ,produtos.split(', ')))
        produtos = []
        pegar_produto = {}
        for a in range(len(lista)+1):
            produtos.append(lista[a][1])
            pegar_produto[lista[a][1]] = lista[a][0]
        if cod_prdt not in produtos and cod_prdt != '*':
            print('Código invalido!')
            sleep(2)
        elif cod_prdt == '*':
            break
        else:
            quant_prdt = input('Digite a quantidade a ser adicionada: ')
            cont_escrita_base_dados = f'{cod_prdt}, {pegar_produto[cod_prdt]}, {quant_prdt}un.\n'
            if verifica_existencia_arquivo(base_dados[1]):
                with open(base_dados[0], 'ab') as arq:
                    arq.write(cont_escrita_base_dados.encode())
                    print(mensagem_sucesso)
                    sleep(2)
            else:
                with open(base_dados[0], 'wb') as arq:
                    arq.write('Código, Produto, Quantidade\n'.encode())
                    arq.write(cont_escrita_base_dados.encode())
                    print('Base de dados criado!')
                    print(mensagem_sucesso)
                    sleep(2)

def relatorios():
    if verifica_existencia_arquivo(base_dados[1]):
        pass
    else:
        return mensagem_sem_base_dados


def verifica_existencia_arquivo(arquivo):
    if arquivo not in os.listdir("C:\Curso\Curso01\Secao13"):
        return False
    else:
        return True

def verifica_dados():

# while True:
#     print("===============================================")
#     print("==============Controle=de=estoque==============")
#     print("===============================================")
#     print('Opções: \n(1)Retirada de Produto:\n(2)Entrada de Produto: \n(3)Relatório \n(4)Sair')
#     opc = int(input('>:'))
#     if opc == 1:
#         saida_produto()
#     elif opc == 2:
#         entrada_produto()
#     elif opc == 3:
#         print(relatorios())
#     elif opc == 4:
#         exit()
#     else:
#         print('Opção invalida!')
saida_produto()