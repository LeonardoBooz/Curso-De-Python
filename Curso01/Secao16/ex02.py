class Agenda:
    def __init__(self):
        pass

    def escreve_base_dados(self, arquivo, conteudo, indice=True):
        if indice == True:
            with open(arquivo, 'a', encoding='UTF-8') as arq:
                arq.write(f'{conteudo}\n')
        elif type(indice) == int: 
            indice -= 1
            with open(arquivo, 'r', encoding='UTF-8') as arq:
                linhas = arq.readlines()
            with open(arquivo, 'w', encoding='UTF-8') as arq:
                linhas[indice] = f'{conteudo}\n'
                arq.writelines(linhas)
        else:
            return f'Indice invalido: {indice}'
    
    def le_base_dados(self, base_dados):
        with open(base_dados, encoding='UTF-8') as arq:
            linhas = arq.readlines()
        linhas = list(map(lambda x: x.split('\n'), linhas))
        linhas = list(map(lambda x: ''.join(x), linhas))
        linhas = (*linhas,)
        return linhas

    def busca_pelo_nome(self, base_dados, nome):
        linhas = self.le_base_dados(base_dados)
        linhas = list(map(lambda x, e: f'({e+1}){x}', linhas, range(len(linhas))))
        ld1 = []
        for pessoa in linhas:
            if nome.lower() in pessoa.lower():
                ld1.append(pessoa)
        pessoas_possiveis = (*ld1,)
        return pessoas_possiveis
    
    def retorna_agenda(self, base_dados):
        linhas = self.le_base_dados(base_dados)
        pessoas_formatadas = []
        for linha in linhas:
            nome, idade, altura = linha.split(', ')
            pessoas_formatadas.append(f'Nome: {nome}, Idade: {idade}, Altura: {altura}\n')
        pessoas_formatadas = ''.join(pessoas_formatadas)
        return pessoas_formatadas

    def busca_pelo_indice(self, base_dados, indice):
        linhas = self.le_base_dados(base_dados)
        linhas = list(map(lambda x, e: f'({e+1}){x}', linhas, range(len(linhas))))
        ld1 = []
        for pessoa in linhas:
            if indice in pessoa:
                ld1.append(pessoa)
        pessoas_possiveis = str(*ld1)
        return pessoas_possiveis
    
    def criar_pessoa(self, base_dados, nome, idade, altura):
        nome = nome.title()
        conteudo = f'{nome}, {idade}, {altura}'
        self.escreve_base_dados(self, base_dados, conteudo)
        return f'{nome} adicionada com sucesso'

    def remove_pessoa(self, base_dados, nome_indice, escolha = True):
        linhas = self.le_base_dados(self, base_dados)
        linhas = list(linhas)
        #por nome
        if escolha:
            for linha in linhas:
                nome, idade, altura = linha.split(', ')
                del idade, altura
                if nome_indice == nome:
                    linhas.pop(linhas.index(linha))
        #por indice
        else:
            try:
                linhas.pop(int(nome_indice)-1)
            except TypeError:
                return f'Remoção por indice é feita apenas por inteiros. Indice informado: {nome_indice}'
        with open(base_dados, 'w', encoding='UTF-8') as arq:
            linhas = list(map(lambda x: f'{x}\n', linhas))
            arq.writelines(linhas)
        return 'Removido com sucesso'
