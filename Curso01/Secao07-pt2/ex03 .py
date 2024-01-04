"""
Fazer uma matriz 4x4 com valores aleatorios e depois mulplicar a linha pela coluna
"""
lista=[]
for e in range(4):
    num=1
    num+=e
    lista2=[]
    if e == 0:
        for f in range(1,5):
            lista2.append(num)
            num+=1
    else:
        lista2.append(num)
        for h in range(1,4):
            produto=num*lista[0][h]
            lista2.append(produto)
        num+=1
    lista+=[lista2]
for e in lista:
    print(e)
