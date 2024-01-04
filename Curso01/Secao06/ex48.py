"""
Faça um programa que some os termos de valor par da sequência de Fibonacci, cujos
valores não ultrapassem quatro milhoes.
"""


lista=[]
g=0
sequencia=[1, 1]
for e in range(400):
    total=sequencia[e]+sequencia[e+1]
    if total > 4_000_000:
        break
    sequencia.append(total)
for f in sequencia:
    if f%2==0:
        lista.append(f)
print(lista)
