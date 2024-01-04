tupla= 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
lista=[]
for e in tupla:
    if e%2==0:
        lista.append(e)
print(len(lista))