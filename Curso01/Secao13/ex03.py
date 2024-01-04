nome_arquivo = input('Digite o nome do arquivo que deseja abrir(nome meu arquivo): ')
if nome_arquivo == '':
    nome_arquivo = r'C:\Curso\Curso01\Secao13\texto.txt'
with  open(nome_arquivo) as arquivo_usuario:
   vo=0
   con=0
   for a in arquivo_usuario.read():
        if a in ['a', 'e', 'i', 'o', 'u']:
           vo+=1
        else:
           con+=1
print(f'vogais {vo} e consoantes {con}')