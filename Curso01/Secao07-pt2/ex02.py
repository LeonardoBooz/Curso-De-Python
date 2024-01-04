lista=[]
h=0
for j in range(5):
    lista2=[]
    for e in range(5):
        if e == h:
            for f in range(1,2):
                lista2.append(f)
        else:
            for f in range(1):
                lista2.append(f)
    h+=1
    lista+=[lista2]
print(lista)