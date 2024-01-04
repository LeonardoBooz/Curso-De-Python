"""
Faça um algoritimo que encontre o primeiro multiplo de 11, 13 ou 17 após um número dado
"""
num11=[]
num13=[]
num17=[]

lista_numeros=[11,13,17]
num=int(input("Digite um número: "))
for e in range(num, 100):
    for f in lista_numeros:
        if e%f == 0:
            if f == 11:
                num11.append(e)
            elif f == 13:
                num13.append(e)
            elif f == 17:
                num17.append(e)
print(num11[0], num13[0], num17[0])