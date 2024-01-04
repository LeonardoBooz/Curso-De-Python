from random import randint

def criador_de_matrizes(tamanho):
    lista=[]
    for linha in range(tamanho):
        lista2=[]
        for coluna in range(tamanho):
            lista2.append(randint(1, 50))
        lista+=[lista2]
    print("matriz")
    for a in lista:
        print(a)
    return lista


matriz1=criador_de_matrizes(4)
matriz2=criador_de_matrizes(4)
matriz3=[]

for a, b in zip(matriz1, matriz2):
    elemento=[]
    for d in range(4):
        if a[d] > b[d]:
            elemento.append(a[d])
        else:
            elemento.append(b[d])
    matriz3+=[elemento]
print("Matriz3")
for a in matriz3:
    print(a)