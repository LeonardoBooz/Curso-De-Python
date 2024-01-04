import pandas as pd

tabela = pd.read_excel('Produtos.xlsx')

#aruazar o multiplicador
tabela.loc[tabela['Tipo'] == 'Serviço', 'Multiplicador Imposto'] = 1.5

tabela['Preço Base Reais'] = tabela['Multiplicador Imposto'] * tabela['Preço Base Original']

tabela.to_excel('produtos_atualizados.xlsx')


from openpyxl import Workbook, load_workbook

planilha = load_workbook('Produtos.xlsx')
aba_ativa = planilha.active


for b in aba_ativa['C']:
    if b.value == 'Serviço':
        linhas = b.row
        aba_ativa[f'D{linhas}'] = 1.5
planilha.save('Produtos_atualizados_2.xlsx')