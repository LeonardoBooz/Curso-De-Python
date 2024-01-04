from random import randint
def lista_randint():
    lista=[]
    for a in range(randint(1,50)):
        b=randint(5, 100)
        if b not in lista:
            lista.append(b)
    return lista

print(lista_randint())