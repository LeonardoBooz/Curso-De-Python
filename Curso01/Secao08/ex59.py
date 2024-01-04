def uniao(*args):
    matriz_a, matriz_b=args
    coluna=[]
    for a, b in zip(matriz_a, matriz_b):
        linha=[]
        for c, d in zip(a, b):
            linha.append(c+d)
        coluna.append(linha)
    return coluna

matriz_a=[[1,2,3], [3,2,1], [4,5,6]]
matriz_b=[[1,2,3], [3,2,1], [4,5,6]]
print(uniao(matriz_a, matriz_b))