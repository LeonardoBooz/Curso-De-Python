from random import randint

soma=0
lista=[]
for a in range(3):
    lista2=[]
    for b in range(3):
        lista2.append(randint(1,50))
    lista+=[lista2]
print(lista)
for a, b in enumerate(lista):
    for c, d in enumerate(b):
        if c == 2 and a ==0 or c == 1 and a ==1 or c == 0 and a == 2:
            soma+=d
print(soma)