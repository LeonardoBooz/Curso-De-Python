from os import listdir


diretorio = listdir(r'C:\Curso\Curso01\Secao13')
nome_arquivo = input(f'Digite o nome do arquivo: \n{diretorio}\nDigite:')
palavra = input('Digite uma palavra para ser procurada: ')

with open(rf'C:\Curso\Curso01\Secao13\{nome_arquivo}') as arquivo:
    print(f'Em {nome_arquivo}, a palavra {palavra} aparece {arquivo.read().count(palavra)}.')