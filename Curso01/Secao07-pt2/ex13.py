from random import randint

lista=[]
lista3=[]
for a in range(4):
    lista2=[]
    for a in range(4):
        lista2.append(randint(1,21))
    lista+=[lista2]
for a in lista:
    print(a)
print("Matriz triangular: ")
for a, b in enumerate(lista):
    lista3+=[b[:a+1]]
qnt=3
for a, b in enumerate(lista3):
        for _ in range(qnt):
            b+=[0]    
        qnt-=1
for a in lista3:
    print(a)
