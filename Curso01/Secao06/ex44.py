"""
Leia um número positivo do usuario, então, calcule e imprima a sequencia Fibonacci até o
primeiro número superior lido.
"""


num=int(input("Digite um número: "))
sequencia=[1, 1]
for e in range(num):
    total=sequencia[e]+sequencia[e+1]
    sequencia.append(total)
    if total > num:
        break
print(sequencia)