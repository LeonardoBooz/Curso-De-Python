lista = ['Ana', 'Joao', 'Mateus', 'Fernando', 'Aurora', 'Jaqueline']
lista_caracter=[]
# for a in lista:
#     lista_caracter.extend(list(map(lambda x: x, a)))

#print(lista_caracter)

lista_caracter = list(map(lambda x: list(x), lista))

print(lista_caracter)