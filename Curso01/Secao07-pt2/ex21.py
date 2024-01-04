matriz=[[2,3],[5,6]]
matriz2=[[4,8],[2,4]]
matriz3=[[],[],[]]
operacao=[]
opc=input("Escolha entre as opções abaixo: \n"+
          '(A)-Soma as duas matrizes\n'+
          '(B)-Subtrair a primeira matriz pela segunda\n'+
          '(C)-Adicionar uma constante ás duas matrizes\n'+
          '(D)Imprimir as matrizes\n')
if opc == 'a' or 'A':
    for a, b in zip(matriz, matriz2):
        for c, d in zip(a, b):
            operacao+=[c+d]
elif opc == 'b' or 'B':
    for a, b in zip(matriz, matriz2):
        for c, d in zip(a, b):
            operacao+=[c-d]
elif opc == 'c' or 'C':
    pass
elif opc == 'd' or 'D':
    print(matriz)
    print(matriz)
if opc == 'a' or 'A' or opc == 'b' or 'B':
    matriz+=matriz2
    # matriz[0]+=[operacao[0:2]]
    # matriz[1]+=[operacao[2:4]]
print(matriz)
