from random import randint

lista=[]
for e in range(0, 15):
    lista.append(randint(0, 10))
print(f'A média dos aluno: {sum(lista)/len(lista):.2}')