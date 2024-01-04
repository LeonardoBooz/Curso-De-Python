def verifica_pares(*args):
    lista=[]
    for a in args:
        if a%2 == 0:
            lista.append(a)
    return len(lista)
    
print(verifica_pares(*[1, 25, 6, 5, 8, 6, 0, 58, 5, 6, 5]))