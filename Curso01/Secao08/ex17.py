def soma_num(n1, n2):
    soma=0
    for a in range(n1, n2+1):
        soma+=a
    return soma

print(soma_num(25, 46))