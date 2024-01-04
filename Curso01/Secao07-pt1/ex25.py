"""
Faça um programa que preencha um vetor de tamanho 100 com os 100 primeiros
naturais que não são multiplos de 7 ou que terminam com 7.
"""
vetor=[]
cont=False
while cont == False:
    for e in range(1, 300):
        indice=len(str(e))
        indice-=1
        if e%7 == 0:
            pass
        elif str(e)[indice] == '7':
            pass
        else:
            vetor.append(e)
        if len(vetor) == 100:
            cont=True
            break
print(vetor)
