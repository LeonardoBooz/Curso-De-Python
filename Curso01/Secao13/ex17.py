with open(r'C:\Curso\Curso01\Secao13\dimensoes_matriz.txt') as arquivo:
    dados_matriz = str(*arquivo.readlines(1)).split(', ')
    coluna, linhas, nulos = dados_matriz
    coluna, linhas, nulos = int(coluna), int(linhas), int(nulos)
    posi_nulos = []
    for a in range(2, nulos+2): 
        for a in arquivo.readlines(a):
            posi_nulos.append(a.split(', '))

lista=[]
for a in range(linhas):
    lista1=[]
    for a in range(coluna):
        lista1.append(1)
    lista.append(lista1)
for a in posi_nulos:
    n1, n2 = a
    n1, n2 = int(n1), int(n2)
    lista[n1][n2]=0
for a in lista:
    print(a)
