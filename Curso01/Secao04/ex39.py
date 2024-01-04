"""
A importancia de R$780.000,00 será dividida entre três ganhadores de um concurso.
sendo que da quantia total:
    o primeiro ganhador receberá 46%
    o sengundo receberá 32%
    o terceiro receberá o restante
"""

premio=float(input("Entre com o valor do prêmio: "))
ganhadores=int(input("Digite o numero de ganhadores: "))

lista=[]

for e in range(ganhadores-1):
    porcentagem=float(input(f"Digite a porcentagem do {e+1}: "))
    if porcentagem > 1:
        lista.append(porcentagem/100)
    else:
        lista.append(porcentagem)
lista.append((1-sum(lista)))
f=1
for L in lista:
    print(f"O ganhador nº{f} deverá receber: R${round((premio*L),2)}")
    f+=1