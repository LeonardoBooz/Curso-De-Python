produto=[]
matriz_a=[[1,5,6],[3,5,7],[9,2,4]]
matriz_b=[[4,6,1],[3,5,4],[9,0,7]]
for a,b in zip(matriz_a, matriz_b):
    for c, d in zip(a, b):
        produto+=[c*d]
print(produto)