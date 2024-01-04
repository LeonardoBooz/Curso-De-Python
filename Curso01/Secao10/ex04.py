lista=[5,6,5,8,5,5,9,9,10]
lista_elevado = list(map(lambda numero: numero[0]**numero[1], zip(lista, range(len(lista)))))
print(lista_elevado)