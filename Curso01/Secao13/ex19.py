with open(r'C:\Curso\Curso01\Secao13\alunos_notas.txt') as alunos_notas:
    alunos_notas1=[]
    for a in alunos_notas:
        alunos_notas1.append(a.split(' '))
    lista_maiores = []
    maior = 0
    for a in alunos_notas1:
        b = float(a[1])
        if b > maior:
            maior = b
            maior_nota = (a)
aluno, nota = maior_nota
print(f'O {aluno} obteve a maior nota, sendo ela {nota}.')