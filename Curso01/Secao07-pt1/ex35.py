from random import randint

lista=[]
lista1=[]

num1=randint(0, 10_000)
num2=randint(0, 10_000)

for e, f in zip(str(num1), str(num2)):
    lista.append(e)
    lista1.append(f)
lista.reverse()
lista1.reverse()
nume1=''
nume2=''
for e, f in zip(lista, lista1):
    nume1+=e
    nume2+=f
print(int(nume1)+int(nume2))