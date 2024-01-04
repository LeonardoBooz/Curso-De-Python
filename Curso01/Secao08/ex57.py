def soma_linha(*args, coluna=0):
    soma=0
    for a, b in enumerate(args):
        soma+=b[coluna]
    return soma
matriz=[[1,2,3,4,5,6], [1,2,3,4,5,6], [1,2,3,4,5,6], [1,2,3,4,5,6], [1,2,3,4,5,6], [1,2,3,4,5,6], [1,2,3,4,5,6]]
print(soma_linha(*matriz, coluna=5))