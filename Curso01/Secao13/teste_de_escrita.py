# def reescrita_linha(arquivo, substituido, substituto , exatidao=True):
#     try:
#         with open(arquivo, 'r+') as arq:
#             linhas = arq.readlines()
#             for linha in linhas:
#                 if '\n' in linha or '\r' in linha:
#                     linhas[linhas.index(linha)] = linha[:-1]
#                 if '\n' in linha and '\r' in linha:
#                     linhas[linhas.index(linha)] = linha[:-3]
#             for linha_texto in linhas:
#                 if linha_texto == substituido and exatidao:
#                     linhas[linhas.index(linha_texto)] = substituto
#                 else:
#                     if linha_texto in substituido:
#                         linhas[linhas.index(linha_texto)] = substituto
#             arq.writelines(linhas)
#         return 'Alterado com sucesso...'
#     except FileNotFoundError:
#         return 'Arquivo inexistente'
# from ex29 import leitura_arquivo
# linhas = leitura_arquivo(base_dados)
# linhas = list(map(lambda x: x.split(', '), linhas))
# for linha in linhas:
#     cod, nome, valor_venda, mes = linha
#     mes = int(mes)
#     valor_venda = float(valor_venda)
#     if mes == 1:
#         mes = 'Jan'
#     elif mes == 2:
#         mes = 'Fev'
#     elif mes == 3:
#         mes = 'Mrç'
#     elif mes == 4:
#         mes = 'Abrl'
#     elif mes == 5:
#         mes = 'Maio'
#     elif mes == 6:
#         mes = 'Jnh'
#     elif mes == 7:
#         mes = 'Jlh'
#     elif mes == 8:
#         mes = 'Agst'
#     elif mes == 9:
#         mes = 'Stmbr'
#     elif mes == 10:
#         mes = 'Otbr'
#     elif mes == 11:
#         mes = 'Nvmbr'
#     elif mes == 12:
#         mes = 'Dzmbr'
#     print(f'Código: {cod}, Vendedor: {nome}, Valor de venda em {mes}: R${valor_venda}')

from ex29 import pesquisa_por_codigo, listar_registros_de_mesmo_código

base_dados = r'C:\Curso\Curso01\Secao13\teste_de_reescrita.txt'
cod = input('Alterar valor de venda pelo código:\nDigite o código:>')
registros = pesquisa_por_codigo(base_dados, cod)
registros = [*registros]
listar_registros_de_mesmo_código(base_dados, cod)
indice = input('Digite qual deseja alterar:>')
novo_registro = float(input(f'Digite o novo valor de venda de {cod}'))
ld1 = registros[indice].split(', ')
