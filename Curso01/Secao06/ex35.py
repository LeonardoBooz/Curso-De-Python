num=input("Digite o intervalo de calculo, assim 10,23: ").split(',')
total=0

if int(num[0]) > int(num[1]):
    print("Intervalo invalido!")
    exit()


for e in range(int(num[0]), int(num[1])):
    if e%2==1:
        total+=e
print(total)