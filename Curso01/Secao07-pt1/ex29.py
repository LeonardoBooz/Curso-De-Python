lista_par=[]
lista_impar=[]
for e in range(1, 7):
    num=int(input(f'Digite um numero {e}/6'))
    if e%2 == 0:
        lista_par.append(e)
    else:
        lista_impar.append(e)
print(lista_par, sum(lista_par))
print(lista_impar, sum(lista_impar))