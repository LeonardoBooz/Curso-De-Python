c=1
lista=[]
lista_soma=[]
for a in range(1, 4):
    lista2=[]
    for b in range(1, 4):
        num=int(input(f'Digite um numero {c}/9: '))
        c+=1
        lista2.append(num)
    lista+=[lista2]
print(lista)
for a in range(3):
    soma=0
    for b ,d in enumerate(lista):
        soma+=d[a]
    lista_soma+=[soma]
print(lista_soma)