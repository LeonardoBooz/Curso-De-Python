lista=[]
for L in range(4):
    num=float(input(f"Digite a nota {L+1}/4: "))
    lista.append(num)
print(f"A média das notas: {sum(lista)/4}")