import math

lista=[]
for L in range(2):
    num=int(input(f'Digite o valor {L+1}/2: '))
    lista.append(num)
print(f"valor da hipoteneusa: {round(math.sqrt(((lista[0]**2)+(lista[1]**2))),2)}")
