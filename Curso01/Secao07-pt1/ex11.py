from random import randint

lista=[]
lista_negativos=[]
lista_positivos=[]
for e in range(10):
    lista.append(randint(-100, 100))
for e in lista:
    if e < 0:
        lista_negativos.append(e)
    else:
        lista_positivos.append(e)
print(f'A soma dos positivos: {sum(lista_positivos)}, a quantidade de negativos: {len(lista_negativos)}')