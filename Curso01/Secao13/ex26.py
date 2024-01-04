import os


class CadastroDeAlunos:

    def __init__(self, nome_base_dados):
        self.nome_base_dados = nome_base_dados

    def le_base_dados(self):#Feito, validado
        if self.verifica_existencia_base_dados():
            with open(nome_base_dados[0], 'rb')as arq:
                dados = arq.read().decode()
                contatos = list(map(lambda x: x.split(', '), dados.split('\n')))
                contatos.pop(-1)
                dic={}
                for a in contatos:
                    codigo, sobrenome, ano_nasc = a
                    dic[codigo] = [sobrenome, ano_nasc]
                return dic
        else:
            return f'Não foi possivel encontrar o arquivo {nome_base_dados[1]}'
        
    def verifica_existencia_base_dados(self):#Feito, validado
        if nome_base_dados[1] not in os.listdir(r'C:\Curso\Curso01\Secao13'):
            return False
        else:
            return True
    
    def escreve_base_dados(self, dic):#Feito
        cod = list(dic.keys())[0]
        sobrenome, ano_nasc = dic[cod]
        if self.verifica_existencia_base_dados():
            if self.verifica_valores_repetidos_base_dados(dic):
                with open(nome_base_dados[0], 'ab') as arq:
                    arq.write(f'{cod}, {sobrenome}, {ano_nasc}\n'.encode())
                    return f'{cod} adicionado com sucesso'
            else:
                return f'{cod} ja existe esta matricula'
        else:
           return f'Não foi possivel encontrar o arquivo {nome_base_dados[1]}'
            
    def verifica_valores_repetidos_base_dados(self, dic):#Feito, validado
        cod = list(dic.keys())[0]
        dados = self.le_base_dados()
        if cod in list(dados.keys()):
            return False
        else:
            return True

nome_base_dados = (r'C:\Curso\Curso01\Secao13\alunos_programa.bin', 'alunos_programa.bin')        
cda = CadastroDeAlunos(nome_base_dados)
num = int(input('Digite quantos alunos vai adicionar: '))
for a in range(num):
    cod = input(f"Digite o código do nº{a+1}: ")
    sobrenome = input(f"Digite o sobrenome do nº{a+1}: ")
    ano_nasc = input(f"Digite o ano de nascimento do nº{a+1}: ")
    cda.escreve_base_dados({cod: [sobrenome, ano_nasc]})