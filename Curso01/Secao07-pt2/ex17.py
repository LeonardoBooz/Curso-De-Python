notas=[[1,3,4,5,3,4,3,4,3,5],[1,1,5,5,3,3,3,4,3,5],[2,2,5,4,4,2,2,4,3,5]]

for linha in notas:
    piores_notas=[]
    menor_nota=min(linha)
    qnt_nota_igual=linha.count(menor_nota)
    if qnt_nota_igual == 1:
        piores_notas=[f'O aluno nº{linha.index(menor_nota)+1} tirou a pior nota na prova']
        print(piores_notas)
    if qnt_nota_igual > 1:
        for b in range(qnt_nota_igual):
            star=linha.index(menor_nota)
            if b == 0:
                piores_notas+=[linha.index(menor_nota,star)+1]
            else:
                piores_notas+=[linha.index(menor_nota,piores_notas[-1])+1]
        print(f'Os alunos, {piores_notas} tem a mesma nota: {menor_nota}')
        
