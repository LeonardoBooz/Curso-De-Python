def produto_matricial(*args):
    matriz_a, matriz_b=args
    coluna_c=[]
    for a, b in zip(matriz_a, matriz_b):
        linha_c=[]
        for c, d in zip(a, b):
            linha_c.append(c*d)
        coluna_c.append(linha_c)
    return coluna_c

matriz_a=[[1,2,3],[3,2,1],[1,3,2]]
matriz_b=[[3,2,1],[1,2,3],[2,3,1]]

print(produto_matricial(matriz_a, matriz_b))