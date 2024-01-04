#Peça ao usuário para digitar três valores inteiros e imprima a soma deles

lista=[]

for _ in range(3):
    num=input('Digite um número ')
    lista.append(int(num))
print(sum(lista))
