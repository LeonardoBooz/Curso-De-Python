"""
Ler os dois conjuntos de números reais, armazenado-os em valores e calcular
o produto escalar entre eles. Os conjuntos tem 5 elementos cada. Imprimir os 
dois conjuntos e o produto escalar, sendo que o produto escalar é dado por:
x1*y1+x2*y2...
"""
tupla1=((1, 2), (2,3), (35, 22), (7,6), (12, 32))
tupla2=((5, 4), (3, 2), (1, 7), (12, 10), (1, 3))
lista=[]
for a, b in zip(tupla1, tupla2):
    for x, y in zip(a, b):
        total=((x*y)+(x*2)*(y*2)+(x*3)*(y*3)+(x*4)*(y*4)+(x*5)*(y*5))
        lista.append(total)
print(f'CA {tupla1}, CB {tupla2}')
print(lista)
