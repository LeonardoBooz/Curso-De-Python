nome_arquivo = input('Digite o nome do arquivo que deseja abrir(default: texto.txt): ')
if nome_arquivo == '':
    nome_arquivo = r'C:\Curso\Curso01\Secao13\texto.txt'
while True:
    car= input('Digite um caracter: ')
    if len(car) == 1:
        break
    print('digite apenas um caracter...')
with  open(nome_arquivo) as arquivo_usuario:
   ret=0
   for a in arquivo_usuario.read():
        if car == a:
           ret+=1
print(f'Quantidade de vezes que o caracter {car} aparece, {ret}')