matriz=[[1,3,4,5,7,4],[3,4,6,7,8,4],[9,7,6,4,5,1]]
impares=[]
media_aritimetica=[]
soma_sexta_coluna=[]
for a, b in enumerate(matriz):
    for c, d in enumerate(b):
        if c%2 != 0:
            impares.append(d)
        if c == 1 or c == 3:
            media_aritimetica.append(d)
        if c == 0 or c == 1:
            soma_sexta_coluna.append(d)
print(sum(impares))
print(sum(media_aritimetica)/3)
e=0
for a in range(0,6,2):
    soma=soma_sexta_coluna[a]+soma_sexta_coluna[a+1]
    matriz[e][5]=soma
    e+=1
print(matriz)
