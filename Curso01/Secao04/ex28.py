lista=[]
for L in range(3):
    num=int(input(f"Digite um número {L+1}/3: "))
    lista.append(num**2)
print(sum(lista))