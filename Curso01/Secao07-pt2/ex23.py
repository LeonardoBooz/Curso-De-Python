matriz_a=[[1,5,6],[3,5,7],[9,2,4]]
lista=[]
for a, b in enumerate(matriz_a):
    for c,d in enumerate(b):
        lista.append(d**2)
matriz_b=[[lista[0],lista[1],lista[2]],[lista[3],lista[4],lista[5]],[lista[6],lista[7],lista[8]]]
print(matriz_b)