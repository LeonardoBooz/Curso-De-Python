from random import randint


def gabarito():
    lista=[['1','2','3','4','5'],
    ['a', 'a', 'c', 'c', 'd'],
    ['b', 'c', 'c', 'a', 'a'],
    ['d', 'a', 'd', 'c', 'd'],
    ['a', 'c', 'a', 'c', 'b'],
    ['a', 'b', 'a', 'a', 'b'],
    ['c', 'b', 'd', 'a', 'b'],
    ['d', 'b', 'b', 'a', 'b'],
    ['d', 'b', 'a', 'b', 'a'],
    ['b', 'd', 'c', 'd', 'd'],
    ['d', 'a', 'b', 'd', 'b']]
    return lista

lista=[['1','2','3','4','5']]
for a in range(10):
    lista2=[]
    for a in range(5):
        ass=randint(1, 4)
        if ass == 1:
            lista2.append('a')
        elif ass == 2:
            lista2.append('b')
        elif ass == 3:
            lista2.append('c')
        elif ass == 4:
            lista2.append('d')
        else:
            print("Erro...")
            exit()
    lista+=[lista2]
resultado=[['1','2','3','4','5'],[],[],[],[],[],[],[],[],[],[]]
gab=gabarito()
for a, b in zip(lista, gab):
    if lista.index(a) != 0 and gab.index(b) != 0:
        for c in range(0, 5): 
            if a[c] == b[c]:
                resultado[lista.index(a)]+=['ac']
            else:
                resultado[lista.index(a)]+=['er']
for a in lista:
    print(a)
print()
for a in gab:
    print(a)
print()
for a in resultado:
    print(a)