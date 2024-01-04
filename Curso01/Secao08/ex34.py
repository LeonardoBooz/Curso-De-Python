def fatorial_duplo(n):
    lista=[]
    produto=1
    if n%2 == 0:
        return 'Número invalido!'
    for a in range(1, n+1):
        if a%2 != 0:
            lista.append(a)
    for a in lista:
        produto=produto*a
    return f'O fatorial duplo de {n} é {produto}'  
        
print(fatorial_duplo(5))