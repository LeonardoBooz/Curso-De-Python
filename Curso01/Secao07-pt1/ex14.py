from random import randint

lista=[]
for _ in range(10):
    lista.append(randint(1,30))
for e in lista:
    if lista.count(e) > 1:
        print(e)