"""
Dados três valores, A, B, C, verificar se eles podem ser valores dos lados de um triângulo
e, se forem, se é um triângulo escaleno, equilatero ou isóscele.
"""
lista_ord=['primeiro', 'segundo', 'terceito']
lista_num=[]
for e in lista_ord:
    num=int(input(f"Digite o {e} número"))
    lista_num.append(num)
if lista_num[0]+lista_num[1] > lista_num[2]:
    print("É um triãngulo")
else:
    print('não é um triãngulo')
if lista_num[0] == lista_num[1] and lista_num[1] == lista_num[2]:
    print("É um triângulo equilátero(Todos os lados são iguais)")
elif lista_num[0] == lista_num[1] or lista_num[0] == lista_num[2] or lista_num[1] == lista_num[2]:
    print("É um triãngulo isósceles(o comprimento de dois lados são iguais)")
else:
    print('É um triângulo escaleno(Tem os três lados diferentes)')