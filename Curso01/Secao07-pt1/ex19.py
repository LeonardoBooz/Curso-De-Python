from random import randint
lista=[]
i=randint(1, 49)
for e in range(50):
    lista.append(e)
lista[i]=(i+5*i)%(i+1)
print(lista)