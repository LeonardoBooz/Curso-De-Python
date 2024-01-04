lista1=[23, 4, 4, 5, 53, 4, 5, 5, 6, 47, 8]
lista2=[5, 6, 5, 5, 6, 5, 66, 5, 5, 50 ]
lista3=[5, 6, 5, 5, 52, 6, 5, 6, 8, 8 ]

lista_soma = list(map(lambda x, y, z: x+y+z, lista1, lista2, lista3))
print(lista_soma)