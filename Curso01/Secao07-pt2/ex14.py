from random import randint
lista=[]
lista3=[]
correcao=26
while len(lista) < 25:
    num=randint(0,90)
    if num not in lista:
        lista.append(num)
par1=0
par2=5
for _ in range(5):
    lista2=[]
    for a in lista[par1:par2]:
        a=[a]
        lista2+=a
    par1+=5
    par2+=5
    lista3+=[lista2]
for a in lista3:
    print(a)