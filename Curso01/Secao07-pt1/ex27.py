'''
Leia 10 números inteiros e armazene em um vetor. Em seguida escreva os elementos
que são primos e suas respectivas posições no vetor.
'''
tupla=2, 3, 5, 7, 11, 13, 17, 19, 23, 29
for e in tupla:
    divisiveis=[]
    for f in range(1, max(tupla)+1):
        if f > e:
            break
        if f == 1:
            divisiveis.append(f'Posição: {tupla.index(e)}')
        if e%f == 0 and f != 1:
            divisiveis.append(f'É primo: {e}')
    if len(divisiveis) == 2:
        print(divisiveis)