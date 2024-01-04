import os


arq_entrada = input('Digite o nome do arquivo de entrada: ')
os.rename(r'C:\Curso\Curso01\Secao13\temp.txt', f'C:\Curso\Curso01\Secao13\{arq_entrada}.txt')
arq_saida = input('Digite o nome do arquivo de saída: ')

notas_ordenadas = []
nomes_alunos = []
with open(f'C:\Curso\Curso01\Secao13\{arq_entrada}.txt') as arq:
    for a in arq.readlines():
        b = ''.join(a.split('\n'))
        b = b.split(', ')
        nomes_alunos.append(b[0])
        b.pop(0)
        c = list(map(lambda x: float(x), b))
        c.sort()
        notas_ordenadas.append(c)
with open(f'C:\Curso\Curso01\Secao13\{arq_saida}.txt', 'w') as arq:
    for a, b in zip(nomes_alunos, notas_ordenadas):
        arq.write(f'Aluno: {a}, notas: {b}\n')