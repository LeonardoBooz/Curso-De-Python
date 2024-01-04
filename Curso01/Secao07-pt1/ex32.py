lista1=[]
lista2=[]
for e in range(20):
    num=int(input("Digite um número: "))
    if e < 9:
        lista1.append(num)
    else:
        lista2.append(num)
for e, f in zip(lista1, lista2):
    print(f'Soma{e+f}')
    print(f'Multiplicação{e*f}')
for e in set(lista1):
    if e not in lista2:
        print(f'{e} Não tem na segunda lista')
for e in set(lista1):
    if e in lista2:
        print(f'{e} tem na segunda lista')
tupla=(lista1+lista2)
print(tupla)