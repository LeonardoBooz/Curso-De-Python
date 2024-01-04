from random import randint

encontrado=False
lista=[]
for a in range(5):
    lista2=[]
    for b in range(5):
        lista2.append(randint(1,50))
    lista+=[lista2]
for a in lista:
    print(a)
num=int(input("Digite um valor mostrado na lista: "))
for a, b in enumerate(lista):
    for c, d in enumerate(b):
        if num == d:
            print(f'Linha: {a}, coluna: {c}')
            encontrado=True
if encontrado == False:
    print("Não encontrado")
