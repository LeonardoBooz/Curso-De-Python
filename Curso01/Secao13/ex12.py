from collections import Counter


with open(r'C:\Curso\Curso01\Secao13\alunos_programa.bin') as arquivo:
    arquivo = arquivo.read()
    numero_char = arquivo
    n=0
    for a in numero_char:
        n+=1
    print(n)
    print(arquivo.count('\n')+1)
    ' '.join(arquivo.split('\n'))
    print(len(arquivo.split(' ')))
    lista = ''.join(list(map(lambda x : x if ord(x) >= 65 and ord(x) <=90 or ord(x) >= 97 and ord(x) <= 122 else '', arquivo)))
    print(Counter(lista))
