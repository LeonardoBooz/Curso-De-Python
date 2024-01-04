nome = ['Joao', 'Mateus', 'Fernando' ]
nota = [8.0, 10.0, 9.0]


with open('pra_curioso_ler.txt', 'w') as arq:
    for a, b in zip(nome, nota):
        if len(a) < 40:
            a = a + ' '*(40-len(a))
        arq.write(f'Aluno: {a}, nota: {b}\n')
with open('pra_curioso_ler.txt') as arq:
    print(arq.read())