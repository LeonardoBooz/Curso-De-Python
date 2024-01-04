lista=[]
e=1
while len(lista) != 10:
    num=int(input(f"Digite um número {e}/10: "))
    if num in lista:
        print("Digite um valor que não foi digitado ainda!")
    else:
        lista.append(num)
        e+=1
print(lista)