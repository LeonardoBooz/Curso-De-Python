def verifica(*args):
    validacao=all(arg != 0 for arg in args)
    if validacao == False:
        print("Nímero invalido!")
        return validacao
    return validacao

def triangulo(n1, n2, n3):
    if n1 + n2 > n3 or n1 + n3 > n2 or n2 + n3 > n1:
        print('É um triângulo')
        return True
    else:
        print('Não é um triângulo')
        return False

def tipo_de_triangulo(*args):
    n1, n2, n3 = args
    if n1 == n2 and n2 == n3:
        print('É um equilátero')
    elif n1 == n2 or n1 == n3 or n2 == n3:
        print('É um isóceles')
    elif n1 != n2 and n1 != n3 and n2 != n3:
        print('É um escaleno')

lista=[]
for a in range(3):
    num=int(input("Digite um número:"))
    lista.append(num)

if verifica(*lista):
    if triangulo(*lista):
        tipo_de_triangulo(*lista)