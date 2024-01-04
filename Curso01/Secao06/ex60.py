cont=False
lista_numero=[]
lista_numero_pares=[]
while cont == False:
    num=int(input('Digite um número: '))
    if num == 0:
        break
    lista_numero.append(num)
    for e in lista_numero:
        if e%2 == 0:
            lista_numero_pares.append(e)
    print(f"Total somado: {sum(lista_numero)}\n"+
          f"A quantidade digitada: {len(lista_numero)}\n"+
          f"A média dos números digitados: {sum(lista_numero)/len(lista_numero)}\n"+
          f"O maior número digitado: {max(lista_numero)}\n"+
          f"O menor número digitado: {min(lista_numero)}\n"+
          f"A média dos pares: {sum(lista_numero_pares)/len(lista_numero_pares)}\n")