lista=[]
for e in range(1, 11):
    num=int(input(f"Digite algum inteiro {e}/10: "))
    lista.append(num)
print(max(lista), min(lista))