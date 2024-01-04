import os
from datetime import datetime
from time import sleep


nome_base_dados_alunos = (r'C:\Curso\Curso01\Secao13\registro_de_alunos.bin', 'registro_de_alunos.bin')

def verifica_existencia_base_dados(nome_base_dados):#Feito, validado
        if nome_base_dados not in os.listdir(r'C:\Curso\Curso01\Secao13'):
            return False
        else:
            return True
        
def definir_informacoes_turma(informações):
    with open(r'C:\Curso\Curso01\Secao13\informações_da_turma.bin', 'ab') as arq:
        arq.write(f'{informações}\n{datetime.now()}'.encode())
    
def inserir_aluno_nota(base_dados, aluno, nota=0, opc=2,):
    if opc == 1:
        inserir_aluno(base_dados, aluno)
    else:
        inserir_nota(base_dados, aluno, nota)

def inserir_aluno(base_dados, aluno):
     with open(base_dados, 'ab') as arq:
          arq.write(f'{aluno}\n'.encode())
          
def inserir_nota(base_dados, aluno, nota):
    with open(base_dados, 'rb') as arq:
        conteudo = list(map(lambda x: x.decode() , arq.readlines()))
        for aluno_notas in conteudo:
            if aluno in aluno_notas:
                aluno_notas_ant = aluno_notas
                aluno_notas_mod = list(map(lambda x: x.split(', '), aluno_notas.split('\n')))
                aluno_notas_mod.pop(-1)
                aluno_notas_mod[0].append(nota)
                aluno_notas_mod = ', '.join(*aluno_notas_mod)

    with open(base_dados, 'wb') as arq:
        for linhas in conteudo:
            if linhas != aluno_notas_ant:
                arq.write(linhas.encode())
            else:
                arq.write(f'{aluno_notas_mod}\n'.encode())

def exibir_alunos_media(base_dados):
    with open(base_dados, 'rb') as arq:
        aluno_notas_sep = []
        conteudo = list(map(lambda x: x.decode() , arq.readlines()))
        for aluno_notas in conteudo:
            aluno_notas = list(map(lambda x: x.split(', '), aluno_notas.split('\n')))
            aluno_notas.pop(-1)
            aluno_notas_sep.append(aluno_notas[0])
    medias = []
    for a in aluno_notas_sep:
        media = 0
        for nota in a[1:]:
            media+= int(nota)
        media = media / len(a[1:])
        medias.append(f'{a[0]}, {media}') 
    return medias


def exibir_alunos_aprovados(base_dados):
    alunos = []
    media_alunos = exibir_alunos_media(base_dados)
    for a in media_alunos:
        nome, media = a.split(', ')
        if float(media) >= 7:
            alunos.append(nome)
    return alunos

def exibir_alunos_reprovados(base_dados):
    alunos = []
    media_alunos = exibir_alunos_media(base_dados)
    for a in media_alunos:
        nome, media = a.split(', ')
        if float(media) < 7:
            alunos.append(nome)
    return alunos

def salvar_dado():
    print('Dados Salvos')
    sleep(2)
    

def sair():
    exit()

while True:
    os.system('cls')
    print('===============================================================')
    print('===============================================================')
    print('====================Contatos=Telefonicos=======================')
    print('===============================================================')
    print('===============================================================')
    opc = int(input('OPÇÔES:\n--------\n(1)Definir informações da turma | (4)Exibir aprovados\n(2)Inserir aluno e notas         | (5)Exibir reprovados\n(3)Exibir alunos e médias  | (6)Salvar\n(7)Sair\n:>'))
    if opc == 1:
        informações = input(':>')
        definir_informacoes_turma(informações)

    elif opc == 2:
        opc = int(input('(1)Cadastrar novo aluno\n(2)Inserir notas'))
        if opc == 1:
            aluno = input('Digite o nome do aluno para cadastrar: ')
            inserir_aluno_nota(nome_base_dados_alunos[0], opc=opc, aluno=aluno)
        else:
            aluno = input('Digite o nome do aluno: ')
            nota = input('Digite a nota: ')
            inserir_aluno_nota(nome_base_dados_alunos[0], opc=opc, aluno=aluno, nota=nota)
        
    elif opc == 3:
        print(exibir_alunos_media(nome_base_dados_alunos[0]))
        input('Digite * para voltar:>')

    elif opc == 4:
        print(exibir_alunos_aprovados(nome_base_dados_alunos[0]))
        input('Digite * para voltar:>')

    elif opc == 5:
        print(exibir_alunos_reprovados(nome_base_dados_alunos[0]))
        input('Digite * para voltar:>')

    elif opc == 6:
        salvar_dado()

    elif opc == 7:
        break
    else:
        print('Opção invalida!')