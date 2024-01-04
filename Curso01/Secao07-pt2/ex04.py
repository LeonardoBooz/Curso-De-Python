from random import randint
lista3=[]
lista=[]
for a in range(4):
    lista2=[]
    for b in range(4):
        lista2.append(randint(1,50))
    lista+=[lista2]
    lista3+=[max(lista2)]
for a in lista:
    print(a)
print(max(lista3))
