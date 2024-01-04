def verifica_diagonal(*args):
    for c in range(len(args)):
        if args[c][c] != 1:
            return False
    return True

def verifica_abaixo(*args):
    for a in range(len(args)):
        for b in range(len(args)):
            if a != b:
                if args[a][b] != 0:
                    return False
    return True

def recebe_matriz(*args):
    if verifica_diagonal(*args) and verifica_abaixo(*args):
        print('É uma matriz indentidade!')
    else:
        print('Não é uma matriz identidade')

matriz1=[[1,0,0],[0,1,0],[0,0,1]]
matriz2=[[1,0,0],[0,1,0],[6,5,1]]
recebe_matriz(*matriz1)
recebe_matriz(*matriz2)