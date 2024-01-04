def entrada_resposta_matricula():
    matricula=int(input("Digite a matricula do aluno(a): "))
    lista=[matricula]
    for e in range(1,11):
        resposta=input(f"Digite a resposta {e}/10 do aluno(a), (a, b, c, d ou e): ")
        while True:
            if resposta in ['a', 'b', 'c', 'd', 'e']:
                break
            else:
                print("resposta invalida!")
                resposta=input(f"Digite a resposta {e}/10 do aluno(a), (a, b, c, d ou e): ")
        lista+=[resposta]
    return lista

resultado=[]
for e in range(1,4):
    print(f'Aluno(a) {e}/3: ')
    gabarito=[0, 'a', 'd', 'e', 'c', 'a', 'a', 'c', 'e', 'e', 'b']
    prova_aluno=entrada_resposta_matricula()
    pontuacao=0
    for a, b in zip(prova_aluno, gabarito):
        if prova_aluno.index(a) != 0 and gabarito.index(b) != 0:
            if a == b:
                pontuacao+=1
        elif prova_aluno.index(a) == 0:
            resultado+=[f'Matricula: {a}']
    resultado+=[f'Nota: {pontuacao}']
print(resultado)
print()
print()