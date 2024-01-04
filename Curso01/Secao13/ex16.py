vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
with open(r'C:\Curso\Curso01\Secao13\numeros_binarios.txt', 'w') as arquivo:
    for a in vetor:
        arquivo.write(f'{bin(a)}\n')
