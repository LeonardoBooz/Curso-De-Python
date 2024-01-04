with open(r'C:\Curso\Curso01\Secao13\entrada_ex28.txt', encoding='UTF-8') as arq:
    texto = arq.read()

with open(r'C:\Curso\Curso01\Secao13\saida_ex28.txt', 'w', encoding='UTF-8') as arq:
    arq.write(texto[::-1])

with open(r'C:\Curso\Curso01\Secao13\saida_ex28.txt', encoding='UTF-8') as arq:
    print(arq.read())