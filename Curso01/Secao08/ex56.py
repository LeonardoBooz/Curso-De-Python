def soma_linha(*args, linha=0):
    a=args[linha]
    return sum(a)
matriz=[[1,2,5,4,5,6], [1,2,3,4,5,6], [1,2,3,4,5,6], [1,2,3,4,5,6], [1,2,3,4,5,6], [1,2,3,4,5,6], [1,2,3,4,5,6]]
print(soma_linha(*matriz))