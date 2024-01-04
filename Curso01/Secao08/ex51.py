def soma(matriz):
    soma=0
    for a, b in enumerate(matriz):
        for c, d in enumerate(b):
            if (a == 0 and c == 2)or (a == 1 and c == 1) or (a == 2 and c == 0):
                soma+=d
    return soma


matriz=[[5,6,5],[8,9,5],[4,5,8]]
print(soma(matriz))