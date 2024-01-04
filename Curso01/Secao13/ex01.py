arquivo = open('arq.txt','w')
while True:
    char = input('Digite um caracter: ')
    if char == '0':
        break
    arquivo.write(char)
arquivo.close()

arquivo = open('arq.txt')
for a in arquivo.read():
    print(a)
arquivo.close()