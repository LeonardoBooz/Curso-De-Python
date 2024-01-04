lista=[12,5,54,5,1,45,5,45,545,45,45]
lista1=[1,21,51,45,45,45,5,45,45,51,5,12]
i = list(map(lambda x, y: x/y, lista, lista1))
print(*i)