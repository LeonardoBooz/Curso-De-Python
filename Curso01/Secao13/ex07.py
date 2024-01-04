nome_arquivo = input('Digite o nome do arquivo que deseja abrir(default: texto.txt): ')
if nome_arquivo == '':
    nome_arquivo = r'C:\Curso\Curso01\Secao13\texto.txt'
with open(nome_arquivo) as arquivo_entrada:
    ret=''
    for a in arquivo_entrada.read():
        if a in ['a', 'e', 'i', 'o', 'u']:
            ret+= '*'
        else:
            ret+=a
with open('arquivo_Saida.txt', 'w') as arquivo_Saida:
    arquivo_Saida.write(''.join(ret))
with open('arquivo_Saida.txt', 'r') as arquivo_Saida:
    print(arquivo_Saida.read())