#Faça um programa que receba dois números de mostre qual deles é o maior


lista=[]

for _ in range(2):
    num=int(input("Digite algum número: "))
    lista.append(num)
if lista[0] > lista[1]:
    print(f"O maior é o {lista[0]}")
else:
    print(f"O maior é o {lista[1]}")