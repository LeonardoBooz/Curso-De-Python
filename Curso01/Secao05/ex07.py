"""
Faça um programa que receba dois números e mostre o maior. Se por acaso, 
os dois números forem iguais, imprima a mensagem 'números iguais'.
"""

lista=[]

for _ in range(2):
    num=int(input("Digite algum número: "))
    lista.append(num)
if lista[0] > lista[1]:
    print(f"O maior é o {lista[0]} e possue {lista[0]-lista[1]} números a mais que o {lista[1]}")
elif lista[0] == lista[1]:
    print("Números iguais")
else:
    print(f"O maior é o {lista[1]} e possue {lista[1]-lista[0]} números a mais que o {lista[0]}")