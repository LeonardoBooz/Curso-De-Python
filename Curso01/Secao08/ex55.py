def soma_diagonais(*args):
    soma1=0
    soma2=0
    for a in range(len(args)):
        soma1+=args[a][a]
        soma2+=args[a][(len(args[0])-1)-a]
    return soma1, soma2

print(soma_diagonais(*[[7,2,5],[7,5,3],[7,2,3]]))