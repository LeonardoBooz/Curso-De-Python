from collections import Counter


lista=[]
nome_arquivo = input('Digite o nome do arquivo que deseja abrir(default: texto.txt): ')
if nome_arquivo == '':
    nome_arquivo = r'C:\Curso\Curso01\Secao13\texto.txt'
with  open(nome_arquivo) as arquivo_usuario:
    for a in arquivo_usuario.read():
        if ord(a) >= 97 and ord(a) <= 122:
            lista.append(a)
print(Counter(lista))