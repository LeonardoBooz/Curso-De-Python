"""
Dados n e dois números inteiros positivos, i e j, diferente de 0, imprimir em ordem
crescente os n primeiros naturais que são multiplos de i ou j e ou ambos. Exemplo:
"""
i=[]
j=[]

lista_numeros=[50, 85]
num=int(input("Digite um número: "))
for e in range(1, num):
    for f in lista_numeros:
        if f%e == 0:
            if f == 50:
                i.append(e)
            elif f == 85:
                j.append(e)
print(i, j)