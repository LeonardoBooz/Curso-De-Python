def soma_matriz(*args):
    soma=0
    for a in args:
        for b in a:
            soma+=b
    return soma

print(soma_matriz(*[[1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4]]))
