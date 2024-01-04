from random import randint


def calcula(matriz):
    nova_matriz=[]
    for a, b in enumerate(matriz):
        if a == 0:
            lista=[]
            for c, d in enumerate(b):
                lista+=[[d]]
            nova_matriz+=lista
        else:
            interador=0
            for c, d in enumerate(b):
                nova_matriz[interador]+=[d]
                interador+=1
    return nova_matriz


matriz=[]
n=3
for a in range(n):
    lista=[]
    for a in range(n):
        lista.append(randint(1,20))
    matriz.append(lista)
for a in matriz:
    print(a)
print()
nova_matriz=calcula(matriz)
for a in nova_matriz:
    print(a)
