from random import randint

soma=0
lista=[]
for a in range(3):
    lista2=[]
    for b in range(3):
        lista2.append(randint(1,50))
    lista+=[lista2]
transposta=[]
for a, b in enumerate(lista):
    indice=0
    for c, d in enumerate(b):
        if a == 0:
            transposta1=[]
            transposta1.append(d)
            transposta+=[transposta1]
        if a > 0:
            d=[d]
            transposta[indice]+=d
            indice+=1
for a in lista:
    print(a)
print("transposta:")
for a in transposta:
    print(a)
