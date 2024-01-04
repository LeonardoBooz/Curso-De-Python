from random import randint

lista=[]
for _ in range(20):
    lista.append(randint(1,10))
tupla=set(tuple(lista))
print(lista)
print(tupla)