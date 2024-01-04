lista=[1, -4, 10, -3, 3, 4, 5, -18, 19, 2]
for e in lista:
    if e < 0:
        lista[lista.index(e)]=0
print(lista)